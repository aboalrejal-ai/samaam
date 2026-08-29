"""عقدة السياسات (P) — الحارس التنظيمي في معيار ITU-T Y.3172.

مبدأ حاكم: **لا نموذج لغوي في هذا الملف.**
قرار الحجب منطق شرطي حتمي، يعطي النتيجة نفسها في كل مرة، ويمكن تدقيقه.
النموذج اللغوي يصوغ الشرح فقط (app/llm.py) بعد أن يكون القرار قد اتُّخذ.

كل قاعدة تستشهد بسجل من قاعدة المعرفة بمعرّفه الصريح، لا بنتيجة بحث
دلالي — حتى لا يتغيّر السند القانوني بتغيّر صياغة السؤال.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any

from app.kb import KnowledgeBase


class Verdict(str, Enum):
    """التصنيفات الستة المطلوبة في الهاكاثون."""
    COMPLIANT = "COMPLIANT"
    VIOLATION = "VIOLATION"
    AMBIGUITY = "AMBIGUITY"
    CONFLICT = "CONFLICT"
    POTENTIAL_GAP = "POTENTIAL_GAP"
    INSUFFICIENT_EVIDENCE = "INSUFFICIENT_EVIDENCE"


class Basis(str, Enum):
    """قوة السند — الفرق الذي يجب ألا تخلطه الواجهة.

    STATUTORY يستند إلى المرسوم الملكي (٦٠٠٥٧) وقرار المجلس الصحي (٣/٨٨).
    NATIONAL_PROTOCOL يستند إلى بروتوكول وزارة الصحة، وهو وطني لكنه
    أداة ممارسة إكلينيكية لا نص عقوبة.
    """
    STATUTORY = "STATUTORY"
    NATIONAL_PROTOCOL = "NATIONAL_PROTOCOL"
    CLINICAL_GUIDANCE = "CLINICAL_GUIDANCE"


class Status(str, Enum):
    PASS = "PASS"
    FAIL = "FAIL"
    WARN = "WARN"
    NOT_APPLICABLE = "NOT_APPLICABLE"
    NO_EVIDENCE = "NO_EVIDENCE"


# المستويات المرجعية التشخيصية الوطنية — SFDA MDS-G008 v2.0، الملحق (2)، جدول 1
# ملزِمة بالمرسوم الملكي رقم (60057) المعتمِد لقرار المجلس الصحي رقم (3/88).
NATIONAL_DRL: dict[str, dict[str, float]] = {
    "head":            {"ctdivol": 55.0, "dlp": 1026.0},
    "abdomen_pelvis":  {"ctdivol": 14.0, "dlp": 706.0},
    "chest":           {"ctdivol": 12.0, "dlp": 430.0},
}
PEDIATRIC_HEAD_DRL = {
    (0, 5):  {"ctdivol": 28.0, "dlp": 482.0},
    (6, 15): {"ctdivol": 42.0, "dlp": 697.0},
}

# عتبة وظائف الكلى — بروتوكول وزارة الصحة 2021، القسم 5.2، ص22 و ص28
EGFR_PROPHYLAXIS_THRESHOLD = 30.0

# نطاقات خطر الاعتلال الكلوي المرتبط بالصبغة — بروتوكول وزارة الصحة ص22
CA_AKI_RISK_BANDS: list[tuple[float, float, str]] = [
    (60.0, float("inf"), "≈5%"),
    (45.0, 60.0, "≈10%"),
    (30.0, 45.0, "≈15%"),
    (0.0, 30.0, "≈30%"),
]

# الأدوية السامة للكلى التي يسمّيها البروتوكول — ص24
NEPHROTOXIC = {
    "nsaid", "ibuprofen", "diclofenac", "naproxen", "diuretic", "furosemide",
    "aminoglycoside", "gentamicin", "amphotericin", "zoledronate", "methotrexate",
    "cisplatin", "carboplatin", "oxaliplatin",  # مركّبات البلاتين — "platins"
}


@dataclass
class Check:
    rule: str
    status: Status
    detail: str
    cites: list[str] = field(default_factory=list)
    basis: Basis | None = None

    @property
    def blocking(self) -> bool:
        return self.status is Status.FAIL


@dataclass
class Decision:
    verdict: Verdict
    checks: list[Check]
    citations: list[dict[str, Any]] = field(default_factory=list)
    overridable: bool = True
    override_reason: str = ""

    @property
    def blocked(self) -> bool:
        return self.verdict is not Verdict.COMPLIANT

    def to_dict(self) -> dict[str, Any]:
        return {
            "verdict": self.verdict.value,
            "blocked": self.blocked,
            "overridable": self.overridable,
            "override_reason": self.override_reason,
            "checks": [
                {
                    "rule": c.rule, "status": c.status.value, "detail": c.detail,
                    "basis": c.basis.value if c.basis else None, "cites": c.cites,
                }
                for c in self.checks
            ],
            "citations": self.citations,
        }


def egfr_ckd_epi(scr_umol_l: float, age: int, sex: str) -> float:
    """معادلة CKD-EPI كما تنص عليها وثيقة وزارة الصحة ص21 حرفياً."""
    if sex.lower().startswith("f"):
        exp = -0.329 if scr_umol_l <= 62 else -1.209
        return 144 * (scr_umol_l / 62) ** exp * 0.993 ** age
    exp = -0.411 if scr_umol_l <= 80 else -1.209
    return 141 * (scr_umol_l / 80) ** exp * 0.993 ** age


def ca_aki_risk(egfr: float) -> str:
    for low, high, risk in CA_AKI_RISK_BANDS:
        if low <= egfr < high:
            return risk
    return "unknown"


class PolicyNode:
    def __init__(self, kb: KnowledgeBase | None = None) -> None:
        self.kb = kb or KnowledgeBase()

    # ── القواعد ───────────────────────────────────────────────
    def _check_drl(self, req: dict[str, Any], patient: dict[str, Any]) -> Check:
        body = req.get("body_region")
        cites = ["SFDA-MDS-G008-DRL", "SFDA-DRL-BINDING"]

        if body == "head" and patient.get("age", 99) <= 15:
            limits = next(
                (v for (lo, hi), v in PEDIATRIC_HEAD_DRL.items()
                 if lo <= patient["age"] <= hi), None
            )
        else:
            limits = NATIONAL_DRL.get(body)

        if limits is None:
            return Check(
                "national_drl", Status.NO_EVIDENCE,
                f"No national diagnostic reference level is published for '{body}'. "
                "Samaam does not invent a limit where none is verified.",
                cites,
            )

        ctdi, dlp = req.get("ctdivol_mgy"), req.get("dlp_mgy_cm")
        if ctdi is None or dlp is None:
            return Check(
                "national_drl", Status.NO_EVIDENCE,
                "Dose parameters (CTDIvol / DLP) absent from the request.", cites,
            )

        over = []
        if ctdi > limits["ctdivol"]:
            over.append(f"CTDIvol {ctdi} mGy exceeds the national level of {limits['ctdivol']} mGy")
        if dlp > limits["dlp"]:
            over.append(f"DLP {dlp} mGy-cm exceeds the national level of {limits['dlp']} mGy-cm")

        if over:
            return Check(
                "national_drl", Status.FAIL,
                "; ".join(over) + ". Compliance is binding on healthcare providers under "
                "Royal Decree 60057 approving Saudi Health Council Resolution 3/88.",
                cites, Basis.STATUTORY,
            )
        return Check(
            "national_drl", Status.PASS,
            f"CTDIvol {ctdi} <= {limits['ctdivol']} and DLP {dlp} <= {limits['dlp']}.",
            cites, Basis.STATUTORY,
        )

    def _check_prophylaxis(self, req: dict[str, Any], patient: dict[str, Any]) -> Check:
        cites = ["MOH-CM-PROPHYLAXIS", "MOH-CM-RISK-BANDS"]
        if not req.get("contrast_agent"):
            return Check("renal_prophylaxis", Status.NOT_APPLICABLE,
                         "No iodinated contrast requested.", cites)

        egfr = patient.get("egfr")
        if egfr is None:
            return Check(
                "renal_prophylaxis", Status.NO_EVIDENCE,
                "No eGFR available. The MOH protocol requires eGFR-based screening "
                "before contrast administration; the decision cannot be made without it.",
                cites + ["MOH-CM-SCREENING"],
            )

        risk = ca_aki_risk(egfr)
        if egfr >= EGFR_PROPHYLAXIS_THRESHOLD:
            return Check(
                "renal_prophylaxis", Status.PASS,
                f"eGFR {egfr:.1f} >= {EGFR_PROPHYLAXIS_THRESHOLD}. Prophylaxis is not "
                f"indicated for stable renal function. CA-AKI risk in this band {risk}.",
                cites, Basis.NATIONAL_PROTOCOL,
            )
        if patient.get("maintenance_dialysis"):
            return Check(
                "renal_prophylaxis", Status.NOT_APPLICABLE,
                f"eGFR {egfr:.1f} but patient is on maintenance dialysis; the protocol "
                "excludes this group from prophylaxis eligibility.",
                cites, Basis.NATIONAL_PROTOCOL,
            )
        if req.get("prophylaxis_ordered"):
            return Check(
                "renal_prophylaxis", Status.PASS,
                f"eGFR {egfr:.1f} < {EGFR_PROPHYLAXIS_THRESHOLD} and prophylaxis is ordered.",
                cites, Basis.NATIONAL_PROTOCOL,
            )
        return Check(
            "renal_prophylaxis", Status.FAIL,
            f"eGFR {egfr:.1f} < {EGFR_PROPHYLAXIS_THRESHOLD} and not on maintenance dialysis: "
            f"the patient is eligible for prophylaxis, but none is ordered. "
            f"CA-AKI risk in this band {risk}.",
            cites, Basis.NATIONAL_PROTOCOL,
        )

    def _check_metformin(self, req: dict[str, Any], patient: dict[str, Any]) -> Check:
        cites = ["MOH-CM-METFORMIN"]
        if not req.get("contrast_agent") or not patient.get("on_metformin"):
            return Check("metformin", Status.NOT_APPLICABLE,
                         "Patient is not on metformin, or no contrast requested.", cites)

        egfr = patient.get("egfr")
        if egfr is None:
            return Check("metformin", Status.NO_EVIDENCE,
                         "Metformin category cannot be assigned without an eGFR.", cites)

        category_two = egfr < EGFR_PROPHYLAXIS_THRESHOLD or patient.get("aki")
        if not category_two:
            return Check(
                "metformin", Status.PASS,
                f"Category I: eGFR {egfr:.1f} > {EGFR_PROPHYLAXIS_THRESHOLD} with no AKI. "
                "Metformin need not be discontinued.",
                cites, Basis.NATIONAL_PROTOCOL,
            )
        if req.get("metformin_held"):
            return Check(
                "metformin", Status.PASS,
                "Category II and metformin is held as the protocol requires.",
                cites, Basis.NATIONAL_PROTOCOL,
            )
        return Check(
            "metformin", Status.FAIL,
            f"Category II (eGFR {egfr:.1f} < {EGFR_PROPHYLAXIS_THRESHOLD} or AKI) but metformin "
            "is not held. It must be stopped at or before the exam and suspended for 48 hours, "
            "and not reinstituted until renal function normalises.",
            cites, Basis.NATIONAL_PROTOCOL,
        )

    def _check_nephrotoxic(self, req: dict[str, Any], patient: dict[str, Any]) -> Check:
        cites = ["MOH-CM-NEPHROTOXIC"]
        egfr = patient.get("egfr")
        if egfr is None or egfr >= EGFR_PROPHYLAXIS_THRESHOLD and not patient.get("aki"):
            return Check("nephrotoxic_meds", Status.NOT_APPLICABLE,
                         "Renal function does not trigger the medication review.", cites)

        found = [
            m for m in patient.get("medications", [])
            if any(n in m.lower() for n in NEPHROTOXIC)
        ]
        if not found:
            return Check("nephrotoxic_meds", Status.PASS,
                         "No named nephrotoxic agents in the medication list.", cites)
        # تحذير لا حجب: البروتوكول يقول "قد يكون من الحصافة" لا "يجب"
        return Check(
            "nephrotoxic_meds", Status.WARN,
            f"Nephrotoxic agents present at eGFR < {EGFR_PROPHYLAXIS_THRESHOLD}: "
            f"{', '.join(found)}. The protocol advises withholding non-essential agents "
            "24-48 hours before and 48 hours after exposure where clinically feasible.",
            cites, Basis.NATIONAL_PROTOCOL,
        )

    # ── التقييم ───────────────────────────────────────────────
    def evaluate(self, request: dict[str, Any]) -> Decision:
        patient = dict(request.get("patient", {}))
        req = dict(request.get("requested", {}))

        # احسب eGFR إن لم يُعطَ، بالمعادلة التي تفرضها وزارة الصحة
        if patient.get("egfr") is None and patient.get("serum_creatinine_umol_l"):
            patient["egfr"] = egfr_ckd_epi(
                patient["serum_creatinine_umol_l"], patient["age"], patient["sex"]
            )

        checks = [
            self._check_drl(req, patient),
            self._check_prophylaxis(req, patient),
            self._check_metformin(req, patient),
            self._check_nephrotoxic(req, patient),
        ]

        if any(c.blocking for c in checks):
            verdict = Verdict.VIOLATION
        elif any(c.status is Status.NO_EVIDENCE for c in checks):
            # الامتناع عن الإفتاء عند نقص الدليل — لا تخمين
            verdict = Verdict.INSUFFICIENT_EVIDENCE
        else:
            verdict = Verdict.COMPLIANT

        decision = Decision(verdict=verdict, checks=checks)
        decision.citations = self._resolve(checks)

        if verdict is Verdict.VIOLATION:
            # التجاوز مسموح دائماً في المسار الإكلينيكي: البروتوكول يجعل
            # المرحلتين 4-5 مانعاً نسبياً لا مطلقاً، ويمنع حجب الصبغة عن
            # تشخيص منقذ للحياة. الحجب الدائم يخالف البروتوكول نفسه.
            decision.overridable = True
            decision.override_reason = (
                "A named consultant may override, recorded in the audit trail. "
                "MOH-CM-CKD45 makes stage 4-5 CKD a relative, not absolute, "
                "contraindication and forbids withholding contrast from a "
                "life-threatening indication on renal grounds."
            )
        return decision

    def _resolve(self, checks: list[Check]) -> list[dict[str, Any]]:
        """يجلب نص كل سجل مُستشهَد به من قاعدة المعرفة، بالمعرّف لا بالبحث."""
        seen, out = set(), []
        for c in checks:
            if c.status in (Status.NOT_APPLICABLE,):
                continue
            for cid in c.cites:
                if cid in seen:
                    continue
                seen.add(cid)
                rec = self.kb.get(cid)
                if rec is None:
                    # سجل مفقود = خلل في القاعدة، يُصرَّح به ولا يُبتلع
                    out.append({"record_id": cid, "error": "record not found in knowledge base"})
                    continue
                if rec.get("verification") != "VERIFIED":
                    out.append({"record_id": cid, "error": "record is not VERIFIED; not citable"})
                    continue
                out.append({
                    "record_id": cid, "title": rec["title"], "authority": rec["authority"],
                    "section": rec["section"], "url": rec["url"], "content": rec["content"],
                })
        return out
