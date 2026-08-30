"""خادم قائمة العمل — DICOM Modality Worklist، عقدة C الحقيقية.

هذا هو الربط بالجهاز، وهو ليس واجهة برمجية بل معيار. جهاز الأشعة لا يُؤمر:
هو يسأل. يرسل C-FIND في بداية المناوبة — «ما فحوصاتي المجدولة؟» — فمن يجيبه
هو من يتحكم بما يظهر على شاشة الفني.

فصمّام يصير خادم قائمة العمل نفسه. والجهاز يبقى كما هو حرفياً: لا تحديث،
ولا برنامج مثبَّت، ولا موافقة من الشركة المصنّعة.

وهنا يقع الحجب فعلياً:

    كل قيد يمرّ على عقدة السياسات قبل تسليمه.
    المطابق يُسلَّم. والمحجوب لا يظهر في القائمة إطلاقاً.

أي أن الفني لا يرى الفحص غير الآمن على شاشة جهازه أصلاً — لا أنه يراه
فيُمنع منه. وكلا الحالين يُكتب في سجل التدقيق.

الحدّ الصادق: هذا حجب للمسار المعتمد لا قطع للتيار. يبقى بيد الفني الإدخال
اليدوي في وضع الطوارئ — وهو الصواب تنظيمياً: معيار NEMA XR 25 نفسه تنبيه
يستوجب إقراراً، لا قفلاً، لأن قفل جهاز على مريض حرج قد يقتله.

التشغيل يدوياً للتجربة:
    python -m pynetdicom echoscu localhost 11112 -aec SAMAAM
    python -m pynetdicom findscu localhost 11112 -aec SAMAAM -w -k "(0010,0010)="
"""

from __future__ import annotations

import json
import threading
import uuid
from datetime import datetime
from typing import Any, Iterator

from pydicom.dataset import Dataset
from pynetdicom import AE, evt
from pynetdicom.sop_class import ModalityWorklistInformationFind, Verification

from app.config import settings

# حالات C-FIND المعرَّفة في المعيار.
PENDING = 0xFF00
SUCCESS = 0x0000
FAILURE = 0xC001

_MODALITY = "CT"

# جذر UID مشتقّ من UUID، وهو ما يجيزه المعيار (PS3.5 ملحق B.2) بلا تسجيل.
# مكوّنات الـ UI رقمية حصراً، فلا يصحّ حشو معرّف السيناريو نصّاً فيها —
# جهاز حقيقي يرفض القيمة، وهو خطأ لا يظهر إلا عند أول اختبار مع جهاز.
_UID_NAMESPACE = uuid.UUID("6ba7b811-9dad-11d1-80b4-00c04fd430c8")   # RFC 4122 URL


def _study_uid(scenario_id: str) -> str:
    return f"2.25.{uuid.uuid5(_UID_NAMESPACE, f'samaam:{scenario_id}').int}"


class WorklistServer:
    """خادم DICOM يعمل في خيط جانبي، ويستشير عقدة السياسات قبل كل تسليم."""

    def __init__(self, samaam: Any) -> None:
        self.samaam = samaam
        self.ae: AE | None = None
        self.thread: threading.Thread | None = None
        self.error: str | None = None
        # كل استعلام يصلنا يسجّل الجهاز الذي سأل. هكذا تُملأ بطاقة «جهاز
        # الأشعة» في شاشة الموصّلات: لا تُكتب يدوياً، بل تُكتشف من الشبكة.
        self.callers: list[dict[str, Any]] = []
        self.queries = 0
        self.served = 0
        self.withheld = 0

    # ── القيود ────────────────────────────────────────────────
    def entries(self) -> list[dict[str, Any]]:
        """قائمة العمل المجدولة — من السيناريوهات المعدّة، بيانات محاكاة."""
        out = []
        for path in sorted(settings.scenarios_dir.glob("sc-*.json")):
            data = json.loads(path.read_text())
            if "patient" not in data:      # سيناريو الخصوصية ليس فحصاً مجدولاً
                continue
            out.append(data)
        return out

    def _dataset(self, scenario: dict[str, Any]) -> Dataset:
        """يبني قيد قائمة عمل بالسمات التي يقرأها جهاز حقيقي."""
        requested = scenario.get("requested", {})
        patient = scenario.get("patient", {})
        now = datetime.now()

        ds = Dataset()
        ds.SpecificCharacterSet = "ISO_IR 192"          # UTF-8
        # اسم اصطناعي معلن. لا اسم مريض في هذا المشروع، لا هنا ولا غيره.
        ds.PatientName = f"SYNTHETIC^{scenario['id']}"
        ds.PatientID = scenario["id"]
        ds.PatientSex = "F" if str(patient.get("sex", "")).lower().startswith("f") else "M"
        ds.PatientBirthDate = ""
        ds.AccessionNumber = f"ACC-{scenario['id']}"
        ds.StudyInstanceUID = _study_uid(scenario["id"])
        ds.RequestedProcedureID = scenario["id"]
        ds.RequestedProcedureDescription = requested.get("study", "")

        step = Dataset()
        step.Modality = _MODALITY
        step.ScheduledStationAETitle = settings.mwl_ae_title
        step.ScheduledProcedureStepStartDate = now.strftime("%Y%m%d")
        step.ScheduledProcedureStepStartTime = now.strftime("%H%M%S")
        step.ScheduledProcedureStepDescription = requested.get("study", "")
        step.ScheduledProcedureStepID = scenario["id"]
        step.ScheduledPerformingPhysicianName = ""
        ds.ScheduledProcedureStepSequence = [step]
        return ds

    # ── المعالجات ─────────────────────────────────────────────
    def _on_find(self, event: evt.Event) -> Iterator[tuple[int, Dataset | None]]:
        self.queries += 1
        requestor = event.assoc.requestor
        self.callers.append({
            "ae_title": requestor.ae_title,
            "address": requestor.address,
            "at": datetime.now().astimezone().isoformat(timespec="seconds"),
        })
        del self.callers[:-10]

        try:
            for scenario in self.entries():
                decision = self.samaam.policy.evaluate(
                    self.samaam.preprocess({
                        "patient": scenario["patient"],
                        "requested": scenario["requested"],
                    })
                )
                if decision.blocked:
                    # لا يُسلَّم، ولا يظهر على شاشة الجهاز. ويُقيَّد في التدقيق.
                    self.withheld += 1
                    self.samaam.device.note(
                        "MWL_WITHHELD", scenario["id"], decision.verdict.value,
                        actor=requestor.ae_title,
                        action=decision.action.value,
                        via="DICOM Modality Worklist C-FIND",
                    )
                    continue

                self.served += 1
                self.samaam.device.note(
                    "MWL_SERVED", scenario["id"], decision.verdict.value,
                    actor=requestor.ae_title,
                    action=decision.action.value,
                    via="DICOM Modality Worklist C-FIND",
                )
                yield PENDING, self._dataset(scenario)
            yield SUCCESS, None
        except Exception:
            yield FAILURE, None

    # ── دورة الحياة ───────────────────────────────────────────
    def start(self) -> None:
        if not settings.mwl_enabled or self.thread is not None:
            return
        try:
            ae = AE(ae_title=settings.mwl_ae_title)
            ae.supported_contexts = []
            ae.add_supported_context(Verification)
            ae.add_supported_context(ModalityWorklistInformationFind)
            handlers = [(evt.EVT_C_FIND, self._on_find)]
            self.ae = ae
            self.thread = threading.Thread(
                target=ae.start_server,
                args=(("0.0.0.0", settings.mwl_port),),
                kwargs={"block": True, "evt_handlers": handlers},
                daemon=True,
                name="samaam-mwl",
            )
            self.thread.start()
        except Exception as exc:
            # منفذ مأخوذ أو صلاحية ناقصة: تُسجَّل وتُعرض في شاشة الموصّلات.
            # فشل خادم DICOM لا يُسقط الـ API ولا الكونسول.
            self.error = f"{type(exc).__name__}: {exc}"
            self.ae = None
            self.thread = None

    def stop(self) -> None:
        if self.ae is not None:
            self.ae.shutdown()
        self.ae, self.thread = None, None

    @property
    def running(self) -> bool:
        return self.thread is not None and self.thread.is_alive()

    def status(self) -> dict[str, Any]:
        return {
            "enabled": settings.mwl_enabled,
            "running": self.running,
            "ae_title": settings.mwl_ae_title,
            "port": settings.mwl_port,
            "sop_classes": [
                {"name": "Verification (C-ECHO)", "uid": str(Verification)},
                {"name": "Modality Worklist Information Model — FIND",
                 "uid": str(ModalityWorklistInformationFind)},
            ],
            "queries": self.queries,
            "served": self.served,
            "withheld": self.withheld,
            "callers": list(reversed(self.callers)),
            "error": self.error,
        }
