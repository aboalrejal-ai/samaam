"""موصّل نظام المستشفى — HL7 FHIR R4، قراءة فقط.

هذا اتصال حقيقي بخادم حقيقي، لا محاكاة. الافتراضي خادم HAPI العام
(https://hapi.fhir.org/baseR4) وبياناته اختبارية تُمسح دورياً — فلا مريض
حقيقي يمرّ من هنا، بما يوافق شرط المحاكاة الكاملة.

مبدآن يحكمان هذا الملف:

  ١. قراءة فقط. بوابة السلامة لا تعدّل السجل الطبي بحال. لا PUT ولا POST.
  ٢. الاسم لا يُقرأ أصلاً. عقدة PP تُسقط المعرّفات المباشرة، لكن إسقاطها
     هنا — عند الحدّ — يعني أنها لم تدخل النظام لحظةً واحدة. المادة 23 من
     نظام حماية البيانات تقصر الوصول على الحد الأدنى اللازم، والحد الأدنى
     لقرار جرعة صبغة لا يشمل اسم المريض.
"""

from __future__ import annotations

import time
from dataclasses import dataclass, field
from datetime import date, datetime, timezone
from typing import Any

import httpx

from app.config import settings

# معامل التحويل المعياري للكرياتينين. هو نفسه المستخدم في سيناريو SC-02.
MG_DL_TO_UMOL_L = 88.4

LOINC_CREATININE = "2160-0"      # Creatinine [Mass/volume] in Serum or Plasma
LOINC_BODY_WEIGHT = "29463-7"    # Body weight

# حقول لا تُقرأ من مورد Patient إطلاقاً — تُسجَّل لتُعرض، لا لتُخزَّن.
WITHHELD_FIELDS = ("name", "telecom", "address", "identifier", "photo", "contact")


@dataclass
class ProbeResult:
    """نتيجة فحص اتصال حيّ. لا تُخمَّن ولا تُخزَّن — تُنفَّذ عند الطلب."""

    ok: bool
    detail: str
    latency_ms: int | None = None
    fhir_version: str | None = None
    software: str | None = None
    endpoint: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "ok": self.ok, "detail": self.detail, "latency_ms": self.latency_ms,
            "fhir_version": self.fhir_version, "software": self.software,
            "endpoint": self.endpoint,
            "checked_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        }


@dataclass
class PulledPatient:
    """ما وصل من المستشفى، وما اشتُقّ منه — مفصولين.

    الفصل مقصود: الفني يجب أن يرى القيمة كما صدرت من المختبر (mg/dL) إلى
    جانب القيمة التي حسبها صمّام (µmol/L)، لا الثانية وحدها. رقم محسوب
    بلا أصله رقم لا يمكن التحقق منه.
    """

    patient: dict[str, Any]
    raw: dict[str, Any]
    identifiers_withheld: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "patient": self.patient,
            "raw": self.raw,
            "identifiers_withheld": self.identifiers_withheld,
            "warnings": self.warnings,
        }


def _client() -> httpx.Client:
    return httpx.Client(
        base_url=settings.fhir_base_url.rstrip("/"),
        timeout=settings.fhir_timeout,
        headers={"Accept": "application/fhir+json"},
        follow_redirects=True,
    )


def probe() -> ProbeResult:
    """يسأل الخادم عن بيان قدراته. هذا هو 'اختبار الاتصال' في FHIR."""
    endpoint = settings.fhir_base_url.rstrip("/")
    started = time.perf_counter()
    try:
        with _client() as client:
            response = client.get("/metadata", params={"_summary": "true"})
        elapsed = int((time.perf_counter() - started) * 1000)
        if response.status_code != 200:
            return ProbeResult(False, f"HTTP {response.status_code}", elapsed,
                               endpoint=endpoint)
        body = response.json()
        software = body.get("software") or {}
        return ProbeResult(
            ok=body.get("resourceType") == "CapabilityStatement",
            detail="CapabilityStatement returned"
            if body.get("resourceType") == "CapabilityStatement"
            else f"Unexpected resourceType: {body.get('resourceType')}",
            latency_ms=elapsed,
            fhir_version=body.get("fhirVersion"),
            software=" ".join(x for x in (software.get("name"), software.get("version")) if x)
            or None,
            endpoint=endpoint,
        )
    except Exception as exc:  # الشبكة، أو مهلة، أو ردّ غير JSON
        elapsed = int((time.perf_counter() - started) * 1000)
        return ProbeResult(False, f"{type(exc).__name__}: {exc}", elapsed, endpoint=endpoint)


def _age_from_birth_date(birth_date: str | None) -> int | None:
    if not birth_date:
        return None
    try:
        born = date.fromisoformat(birth_date[:10])
    except ValueError:
        return None
    today = date.today()
    # الطرح المعتاد ثم خصم سنة إن لم يمرّ الميلاد بعدُ هذا العام.
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


def _latest_observation(client: httpx.Client, patient_id: str, loinc: str) -> dict[str, Any] | None:
    response = client.get(
        "/Observation",
        params={
            "patient": patient_id,
            "code": f"http://loinc.org|{loinc}",
            "_sort": "-date",
            "_count": 1,
        },
    )
    if response.status_code != 200:
        return None
    entries = response.json().get("entry") or []
    return entries[0]["resource"] if entries else None


def _days_since(effective: str | None) -> int | None:
    if not effective:
        return None
    try:
        taken = datetime.fromisoformat(effective.replace("Z", "+00:00"))
    except ValueError:
        return None
    if taken.tzinfo is None:
        taken = taken.replace(tzinfo=timezone.utc)
    return max(0, (datetime.now(timezone.utc) - taken).days)


def fetch_patient(patient_id: str) -> PulledPatient:
    """يسحب مريضاً وآخر كرياتينين له، بالشكل الذي يفهمه كونسول صمّام."""
    warnings: list[str] = []

    with _client() as client:
        response = client.get(f"/Patient/{patient_id}")
        if response.status_code == 404:
            raise LookupError(f"No Patient/{patient_id} on {settings.fhir_base_url}")
        response.raise_for_status()
        resource = response.json()

        withheld = [f for f in WITHHELD_FIELDS if resource.get(f)]

        creatinine = _latest_observation(client, patient_id, LOINC_CREATININE)
        weight = _latest_observation(client, patient_id, LOINC_BODY_WEIGHT)

    gender = (resource.get("gender") or "").lower()
    if gender not in ("male", "female"):
        # الجنس يدخل في معادلة CKD-EPI. لا يُخمَّن؛ يُترك فارغاً ليكمله الفني.
        warnings.append("FHIR gender is not male/female; the eGFR equation needs one.")
        gender = ""

    age = _age_from_birth_date(resource.get("birthDate"))
    if age is None:
        warnings.append("No birthDate on the Patient resource; age is required for eGFR.")

    umol: float | None = None
    raw_creatinine: dict[str, Any] | None = None
    if creatinine:
        quantity = creatinine.get("valueQuantity") or {}
        value, unit = quantity.get("value"), (quantity.get("unit") or "").strip()
        age_days = _days_since(creatinine.get("effectiveDateTime"))
        raw_creatinine = {
            "observation_id": creatinine.get("id"),
            "loinc": LOINC_CREATININE,
            "display": (creatinine.get("code") or {}).get("text"),
            "value": value, "unit": unit or None,
            "status": creatinine.get("status"),
            "effective": creatinine.get("effectiveDateTime"),
            "age_days": age_days,
        }
        if value is None:
            warnings.append("The creatinine Observation carries no valueQuantity.")
        elif unit.lower() in ("mg/dl", "mg/dl.", "mg per dl"):
            umol = round(float(value) * MG_DL_TO_UMOL_L, 1)
            raw_creatinine["converted_umol_l"] = umol
            raw_creatinine["conversion_factor"] = MG_DL_TO_UMOL_L
        elif unit.lower() in ("umol/l", "µmol/l", "μmol/l"):
            umol = round(float(value), 1)
        else:
            # وحدة غير معروفة لا تُحوَّل بالتخمين — تُعرَض ويُترك الحقل فارغاً.
            warnings.append(f"Unrecognised creatinine unit '{unit}'. Not converted.")
    else:
        warnings.append("No creatinine Observation (LOINC 2160-0) for this patient.")

    weight_kg: float | None = None
    if weight:
        quantity = weight.get("valueQuantity") or {}
        if (quantity.get("unit") or "").lower() in ("kg", "kgs", "kilogram"):
            weight_kg = quantity.get("value")

    return PulledPatient(
        patient={
            "sex": gender,
            "age": age,
            "weight_kg": weight_kg,
            "serum_creatinine_umol_l": umol,
            "egfr": None,          # يُحسب في PP بمعادلة وزارة الصحة، لا يُستورد
            "on_metformin": False,  # الأدوية ليست في هذا الاستعلام — يؤكدها الفني
            "aki": False,
            "medications": [],
        },
        raw={
            "source": settings.fhir_base_url.rstrip("/"),
            "patient_id": patient_id,
            "gender": resource.get("gender"),
            "birth_date": resource.get("birthDate"),
            "creatinine": raw_creatinine,
            "weight": (weight.get("valueQuantity") if weight else None),
        },
        identifiers_withheld=withheld,
        warnings=warnings,
    )
