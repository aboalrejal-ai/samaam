"""خط أنابيب صمّام — العقد السبع في معيار ITU-T Y.3172.

    SRC → C → PP → M → P → D → SINK

  SRC   وثائق الأنظمة السعودية + ملف المريض + إعدادات الفني
  C     استقبال قائمة العمل (تحاكي DICOM Modality Worklist)
  PP    حساب eGFR بمعادلة وزارة الصحة + إخفاء المعرّفات + التضمين
  M     استرجاع النصوص النظامية وصياغة الشرح  (النموذج اللغوي هنا فقط)
  P     الفحص الحتمي والحجب                    (لا نموذج لغوي إطلاقاً)
  D     إرفاق الاستشهادات وكتابة سجل التدقيق
  SINK  الجهاز أو شاشة متخذ القرار
"""

from __future__ import annotations

from typing import Any

from app.device_api import DevicePolicyViolation, MockCTScanner
from app.kb import KnowledgeBase
from app.policy_node import Decision, PolicyNode, Verdict, egfr_ckd_epi

# معرّفات مباشرة يجب استبعادها قبل أي معالجة — نظام حماية البيانات، المادة 23
DIRECT_IDENTIFIERS = {
    "name", "national_id", "iqama", "mrn", "phone", "email", "address",
}

EXPLAIN_SYSTEM = """You are the explanation layer of Samaam, a policy gateway that sits \
between a radiology technologist and a CT scanner in Saudi Arabia.

A deterministic policy node has ALREADY decided. You do not decide anything. You explain \
a decision that has been made, to the technologist standing at the console.

Absolute rules:
- Use ONLY the provided decision and citations. Never introduce a threshold, a statute, \
an article number, or a URL that is not in them.
- Preserve the distinction in `basis`. STATUTORY means binding by Royal Decree. \
NATIONAL_PROTOCOL means a Saudi Ministry of Health protocol, which is a national clinical \
practice instrument and not a penalty provision. Never call a protocol breach a legal one.
- Say what the technologist should do next.
- If the verdict is INSUFFICIENT_EVIDENCE, state plainly what is missing and that no \
determination can be made without it. Do not speculate.
- Six sentences maximum. Plain professional English. No preamble, no headings."""


class Samaam:
    def __init__(self, kb: KnowledgeBase | None = None) -> None:
        self.kb = kb or KnowledgeBase()
        self.policy = PolicyNode(self.kb)
        self.device = MockCTScanner()

    # ── PP ────────────────────────────────────────────────────
    def preprocess(self, request: dict[str, Any]) -> dict[str, Any]:
        """إخفاء المعرّفات وحساب eGFR. لا يغادر أي معرّف مباشر هذه العقدة."""
        patient = {k: v for k, v in request.get("patient", {}).items()
                   if k not in DIRECT_IDENTIFIERS}
        stripped = sorted(set(request.get("patient", {})) & DIRECT_IDENTIFIERS)

        if patient.get("egfr") is None and patient.get("serum_creatinine_umol_l"):
            patient["egfr"] = round(
                egfr_ckd_epi(patient["serum_creatinine_umol_l"],
                             patient["age"], patient["sex"]), 1
            )
            patient["egfr_method"] = "CKD-EPI, per MOH-CM-EGFR-METHOD"

        return {**request, "patient": patient, "_identifiers_removed": stripped}

    # ── M ─────────────────────────────────────────────────────
    def explain(self, decision: Decision) -> str:
        """يصوغ الشرح. القرار سبق واتُّخذ — هذه صياغة لا حكم.

        عند تعذّر الوصول للنموذج يُرَد شرح مبني من نص السجلات نفسها،
        فالنظام لا يتوقف لغياب مزوّد خارجي.
        """
        from app.llm import complete

        payload = {
            "verdict": decision.verdict.value,
            "checks": [c for c in decision.to_dict()["checks"]
                       if c["status"] in ("FAIL", "WARN", "NO_EVIDENCE")],
            "citations": decision.citations,
        }
        try:
            import json
            return complete(EXPLAIN_SYSTEM, json.dumps(payload, ensure_ascii=False)).strip()
        except Exception:
            return self._explain_offline(decision)

    @staticmethod
    def _explain_offline(decision: Decision) -> str:
        lines = []
        for c in decision.checks:
            if c.status.value in ("FAIL", "WARN", "NO_EVIDENCE"):
                lines.append(f"[{c.status.value}] {c.detail}")
        if not lines:
            lines.append("All checks passed against the cited Saudi provisions.")
        return "\n".join(lines)

    # ── التشغيل الكامل ────────────────────────────────────────
    def run(
        self,
        request: dict[str, Any],
        *,
        override_by: str | None = None,
        explain: bool = True,
    ) -> dict[str, Any]:
        clean = self.preprocess(request)              # PP
        decision = self.policy.evaluate(clean)        # P
        payload = decision.to_dict()                  # D

        if explain:
            payload["explanation"] = self.explain(decision)

        worklist = {
            "worklist_id": request.get("worklist_id"),
            "study": clean["requested"].get("study"),
            **clean["requested"],
        }
        try:                                          # SINK
            device = self.device.submit(worklist, payload, override_by=override_by)
        except DevicePolicyViolation as exc:
            device = {
                "status": exc.http_status,
                "error": "Policy Violation",
                "message": str(exc),
                "decision": exc.decision,
            }

        return {
            "verdict": payload["verdict"],
            "blocked": payload["blocked"],
            "device_response": device,
            "policy": payload,
            "privacy": {
                "identifiers_removed": clean["_identifiers_removed"],
                "note": "Synthetic data. Direct identifiers are dropped at the "
                        "preprocessor per PDPL Article 23.",
            },
        }

    def run_data_request(self, request: dict[str, Any], *,
                         override_by: str | None = None,
                         explain: bool = True) -> dict[str, Any]:
        """مسار الخصوصية — السيناريو الثالث.

        explain=False يعيد القرار وحده. الشرح يُطلب بعده من /explain، فالحظر
        يظهر فوراً بدل أن ينتظر النموذج عشرات الثواني.
        """
        decision = self.policy.evaluate_data_request(request)
        payload = decision.to_dict()
        if explain:
            payload["explanation"] = self.explain(decision)

        wid = request.get("request_id") or "DATA-REQ"
        if decision.blocked:
            self.device._log("SECURITY_OVERRIDE", wid, payload["verdict"],
                             actor=request.get("actor") or "unknown",
                             session_terminated=True,
                             attempted=request.get("action"))
            if override_by:
                self.device._log("OVERRIDE_REFUSED", wid, payload["verdict"],
                                 actor=override_by,
                                 reason="Privacy violations admit no clinical override.")
            response = {
                "status": 403, "error": "Policy Violation",
                "message": "Hard security override. Session terminated and logged.",
                "session_terminated": True, "decision": payload,
            }
        else:
            self.device._log("DATA_ACCESS_GRANTED", wid, payload["verdict"],
                             actor=request.get("actor", "unknown"))
            response = {"status": 200, "message": "Access granted.", "decision": payload}

        return {"verdict": payload["verdict"], "blocked": payload["blocked"],
                "device_response": response, "policy": payload}

    def audit_trail(self) -> list[dict[str, Any]]:
        return self.device.audit_trail()
