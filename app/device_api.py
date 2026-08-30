"""عقدتا التجميع والمصرف (C + SINK) — محاكي الجهاز الطبي.

يمثّل جهاز الأشعة المقطعية وحاقن الصبغة. لا جهاز حقيقي في الهاكاثون،
لكن العقد (contract) هو نفسه الذي يستخدمه جهاز فعلي:

    قائمة عمل (Modality Worklist) تصل →
    صمّام يفحصها قبل تمريرها →
    إما تُنفَّذ، أو يُرَد 403 Policy Violation

السابقة الصناعية: معيار NEMA XR 25 (CT Dose Check) يوجب على أجهزة
الأشعة المقطعية منذ 2010 أن تنبّه قبل التصوير عند تجاوز عتبات الجرعة،
وأن يؤكد المشغّل أو يصحّح. صمّام يوسّع الآلية نفسها: Dose Check يقارن
الجهاز بنفسه، وصمّام يقارنه بحالة المريض.
"""

from __future__ import annotations

import uuid
from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Any


class DeviceState(str, Enum):
    IDLE = "IDLE"
    ARMED = "ARMED"
    EXECUTED = "EXECUTED"
    LOCKED = "LOCKED"


class DevicePolicyViolation(Exception):
    """تُرفع حين ترفض عقدة السياسات الأمر. تُترجَم إلى HTTP 403."""

    http_status = 403

    def __init__(self, decision: dict[str, Any]) -> None:
        self.decision = decision
        super().__init__("Policy Violation — execution withheld by the Samaam policy node")


@dataclass
class AuditEntry:
    """قيد في سجل التدقيق. عقدة التوزيع (D) تكتب هنا.

    السجل هو ما يحوّل التجاوز من فعل مجهول إلى قرار منسوب لشخص —
    وهو جوهر ما تعالجه الثغرة GAP-02 حول المسؤولية.
    """
    event: str
    worklist_id: str
    verdict: str
    at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    actor: str = "system"
    detail: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "at": self.at, "event": self.event, "worklist_id": self.worklist_id,
            "verdict": self.verdict, "actor": self.actor, "detail": self.detail,
        }


class MockCTScanner:
    """جهاز أشعة مقطعية وحاقن صبغة — محاكاة.

    لا ينفّذ أمراً إلا عبر بوابة صمّام. الاستدعاء المباشر لـ execute
    ممنوع عمداً: لو كان بالإمكان الالتفاف على البوابة، لما كانت بوابة.
    """

    model = "Samaam Reference CT + Contrast Injector (simulated)"

    def __init__(self) -> None:
        self.state = DeviceState.IDLE
        self.audit: list[AuditEntry] = []
        self.executed: list[dict[str, Any]] = []

    # ── سجل التدقيق ───────────────────────────────────────────
    def _log(self, event: str, wid: str, verdict: str, actor: str = "system",
             **detail: Any) -> None:
        self.audit.append(AuditEntry(event, wid, verdict, actor=actor, detail=detail))

    def note(self, event: str, worklist_id: str, verdict: str, *,
             actor: str = "system", **detail: Any) -> None:
        """قيد تدقيق من موصّل خارجي — ولا يغيّر حالة الجهاز.

        قائمة العمل تُستعلم قبل أن يبدأ فحص، فالجهاز لم يُؤمر بعدُ بشيء.
        الحجب هناك منعُ ظهور على الشاشة، لا إيقافُ تنفيذٍ جارٍ.
        """
        self._log(event, worklist_id, verdict, actor=actor, **detail)

    # ── البوابة ───────────────────────────────────────────────
    def submit(
        self,
        worklist: dict[str, Any],
        decision: dict[str, Any],
        *,
        override_by: str | None = None,
    ) -> dict[str, Any]:
        """تسليم قائمة عمل مصحوبة بقرار عقدة السياسات.

        override_by: اسم الاستشاري المعتمِد. يُقبل فقط حين يكون القرار
        قابلاً للتجاوز — انتهاكات الخصوصية ليست كذلك.
        """
        wid = worklist.get("worklist_id") or f"MWL-{uuid.uuid4().hex[:8].upper()}"
        verdict = decision.get("verdict", "UNKNOWN")

        if not decision.get("blocked"):
            self.state = DeviceState.EXECUTED
            self.executed.append(worklist)
            self._log("EXECUTED", wid, verdict)
            return {
                "status": 200,
                "worklist_id": wid,
                "device_state": self.state.value,
                "message": "Acquisition parameters accepted. Scan may proceed.",
                "decision": decision,
            }

        if override_by:
            if not decision.get("overridable", False):
                self.state = DeviceState.LOCKED
                self._log("OVERRIDE_REFUSED", wid, verdict, actor=override_by,
                          reason="This verdict class admits no clinical override.")
                raise DevicePolicyViolation({
                    **decision,
                    "override_refused": True,
                    "override_refused_reason":
                        "No clinical override path exists for this verdict class.",
                })
            self.state = DeviceState.EXECUTED
            self.executed.append({**worklist, "overridden_by": override_by})
            self._log("EXECUTED_UNDER_OVERRIDE", wid, verdict, actor=override_by,
                      accepted_risk=[c for c in decision.get("checks", [])
                                     if c.get("status") == "FAIL"])
            return {
                "status": 200,
                "worklist_id": wid,
                "device_state": self.state.value,
                "message": (
                    f"Acquisition released under documented override by {override_by}. "
                    "The accepted risk is recorded in the audit trail."
                ),
                "overridden_by": override_by,
                "decision": decision,
            }

        self.state = DeviceState.LOCKED
        self._log("BLOCKED", wid, verdict,
                  failed=[c.get("rule") for c in decision.get("checks", [])
                          if c.get("status") == "FAIL"])
        raise DevicePolicyViolation({**decision, "worklist_id": wid})

    def reset(self) -> None:
        self.state = DeviceState.IDLE

    def audit_trail(self) -> list[dict[str, Any]]:
        return [a.to_dict() for a in self.audit]
