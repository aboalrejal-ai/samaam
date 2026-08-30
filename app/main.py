"""خدمة صمّام — FastAPI.

نقاط النهاية مصمَّمة لتستهلكها واجهة React مباشرة.
    GET  /health              حالة النظام والقاعدة والمزوّد
    GET  /scenarios           السيناريوهات الثلاثة المعدّة
    POST /evaluate            تقييم طلب تصوير عبر خط الأنابيب كاملاً
    POST /device/execute      تسليم للجهاز — يرد 403 عند الحجب
    POST /data/request        مسار الخصوصية — حظر صارم بلا تجاوز
    POST /explain             صياغة شرح لقرار اتُّخذ — منفصل عمداً عن القرار
    GET  /kb/search           بحث في قاعدة المعرفة
    GET  /kb/record/{id}      سجل بعينه
    GET  /kb/gaps             الثغرات التنظيمية
    GET  /audit               سجل التدقيق
    GET  /framework           أبعاد جاهزية ITU الـ 13
"""

from __future__ import annotations

import json
from contextlib import asynccontextmanager
from typing import Any

from fastapi import FastAPI, HTTPException, Query, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

from app.config import settings
from app.connectors import fhir
from app.connectors.mwl import WorklistServer
from app.kb import GAPS, POLICIES, SOURCES, KnowledgeBase
from app.pipeline import Samaam

SYNTHETIC_NOTICE = "بيانات محاكاة لأغراض الهاكاثون فقط — Synthetic data, hackathon use only"

samaam = Samaam()
kb = samaam.kb
worklist = WorklistServer(samaam)


@asynccontextmanager
async def lifespan(_: FastAPI) -> Any:
    """يُقلع خادم قائمة العمل مع الخدمة، ويُطفأ معها.

    الإقلاع داخل try في WorklistServer.start: منفذ مأخوذ أو صلاحية ناقصة
    تُسجَّل وتُعرض في شاشة الموصّلات، ولا تمنع الـ API من العمل.
    """
    worklist.start()
    yield
    worklist.stop()


app = FastAPI(
    title="Samaam — AI-Hardware Policy Gateway",
    description="ITU-T Y.3172 policy gateway for oncology radiology. " + SYNTHETIC_NOTICE,
    version="0.1.0",
    lifespan=lifespan,
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Patient(BaseModel):
    sex: str
    age: int
    weight_kg: float | None = None
    serum_creatinine_umol_l: float | None = None
    egfr: float | None = None
    on_metformin: bool = False
    aki: bool = False
    maintenance_dialysis: bool = False
    medications: list[str] = Field(default_factory=list)
    diagnosis: str | None = None


class Requested(BaseModel):
    study: str | None = None
    body_region: str
    kvp: float | None = None
    mas: float | None = None
    ctdivol_mgy: float | None = None
    dlp_mgy_cm: float | None = None
    contrast_agent: str | None = None
    iodine_mg_per_ml: float | None = None
    volume_ml: float | None = None
    flow_rate_ml_s: float | None = None
    prophylaxis_ordered: bool = False
    metformin_held: bool = False


class SafeAlternative(BaseModel):
    """بديل أدنى جرعةً يقترحه السيناريو. عرضٌ محض — لا تقرأه أي قاعدة."""
    ctdivol_mgy: float | None = None
    dlp_mgy_cm: float | None = None


class EvaluationRequest(BaseModel):
    worklist_id: str | None = None
    patient: Patient
    requested: Requested
    safe_alternative: SafeAlternative | None = None
    override_by: str | None = None
    explain: bool = True


@app.get("/health")
def health() -> dict[str, Any]:
    from app.llm import health_check

    ok, msg = health_check()
    return {
        "status": "ok",
        "notice": SYNTHETIC_NOTICE,
        "knowledge_base": {
            "policies": kb.count(POLICIES),
            "gaps": kb.count(GAPS),
            "source_chunks": kb.count(SOURCES),
        },
        "embedding": {"model": settings.embed_model, "local": True},
        "model": {"reachable": ok, "detail": msg,
                  "note": "Explanation only. The policy node never calls it."},
    }


@app.get("/scenarios")
def scenarios() -> list[dict[str, Any]]:
    out = []
    for path in sorted(settings.scenarios_dir.glob("sc-*.json")):
        out.append(json.loads(path.read_text()))
    return out


@app.post("/evaluate")
def evaluate(body: EvaluationRequest) -> dict[str, Any]:
    return samaam.run(
        {
            "worklist_id": body.worklist_id,
            "patient": body.patient.model_dump(exclude_none=False),
            "requested": {
                **body.requested.model_dump(exclude_none=False),
                "_safe_alternative": (
                    body.safe_alternative.model_dump() if body.safe_alternative else None
                ),
            },
        },
        override_by=body.override_by,
        explain=body.explain,
    )


@app.post("/device/execute", status_code=200)
def device_execute(body: EvaluationRequest) -> dict[str, Any]:
    """يعكس رمز حالة الجهاز في استجابة HTTP — 403 عند الحجب."""
    result = evaluate(body)
    status = result["device_response"]["status"]
    if status != 200:
        raise HTTPException(status_code=status, detail=result)
    return result


class ExplainRequest(BaseModel):
    """A decision already made, to be put into words."""
    policy: dict[str, Any]


@app.post("/explain")
def explain(body: ExplainRequest) -> dict[str, Any]:
    """Drafts the prose for a decision that has already been taken.

    Separate from /evaluate on purpose. The policy node reaches a verdict in
    milliseconds and the model takes tens of seconds, so binding them into one
    request would make a refusal look slow — and a refusal has to land the
    instant the technologist presses the button. Splitting them also makes the
    architecture visible: the block arrives with its citations before the model
    has said anything at all.
    """
    import json as _json

    payload = {
        "verdict": body.policy.get("verdict"),
        "checks": [
            c for c in body.policy.get("checks", [])
            if c.get("status") in ("FAIL", "WARN", "NO_EVIDENCE")
        ],
        "citations": body.policy.get("citations", []),
    }
    try:
        from app.llm import complete
        from app.pipeline import EXPLAIN_SYSTEM

        text = complete(EXPLAIN_SYSTEM, _json.dumps(payload, ensure_ascii=False)).strip()
        return {"explanation": text, "source": "model"}
    except Exception as exc:
        # The decision stands without it. Say plainly that the prose is missing
        # rather than implying the verdict is incomplete.
        return {
            "explanation": "",
            "source": "unavailable",
            "detail": f"{type(exc).__name__}: {exc}",
        }


class DataRequest(BaseModel):
    request_id: str | None = None
    actor: str
    action: str
    stated_purpose: str
    record_count: int = 0
    destination_outside_kingdom: bool = False
    care_purpose: bool = False
    override_by: str | None = None
    explain: bool = True


@app.post("/data/request")
def data_request(body: DataRequest) -> dict[str, Any]:
    """مسار الخصوصية — السيناريو الثالث. لا يقبل تجاوزاً إكلينيكياً."""
    result = samaam.run_data_request(
        body.model_dump(exclude={"override_by", "explain"}),
        override_by=body.override_by,
        explain=body.explain,
    )
    if result["device_response"]["status"] != 200:
        raise HTTPException(status_code=403, detail=result)
    return result


@app.get("/kb/search")
def kb_search(
    q: str = Query(..., min_length=2),
    collection: str = Query(POLICIES, pattern="^(policies|sources|gaps)$"),
    top_k: int = Query(6, ge=1, le=20),
    verified_only: bool = True,
) -> dict[str, Any]:
    hits = kb.search(q, name=collection, top_k=top_k, verified_only=verified_only)
    return {"query": q, "collection": collection, "count": len(hits), "results": hits}


@app.get("/kb/record/{record_id}")
def kb_record(record_id: str) -> dict[str, Any]:
    rec = kb.get(record_id)
    if rec is None:
        raise HTTPException(404, f"No record '{record_id}' in the knowledge base.")
    return rec


@app.get("/kb/gaps")
def kb_gaps() -> list[dict[str, Any]]:
    data = json.loads((settings.kb_dir / "records" / "health-regulatory.json").read_text())
    return data["gaps"]


@app.get("/audit")
def audit() -> list[dict[str, Any]]:
    return samaam.audit_trail()


@app.get("/framework")
def framework() -> dict[str, Any]:
    """أبعاد ITU AI Readiness 2.0 — من ملف المنظمين الرسمي."""
    return json.loads(settings.framework_file.read_text())


# ── الموصّلات (عقدة C) ──────────────────────────────────────────────
# مستشفيات حقيقية بأسمائها ومدنها، وحقول اتصالها فارغة عمداً: عناوين FHIR
# وأسماء الأجهزة داخل شبكات المستشفيات ولا تُنشر، واختراعها هو بالضبط
# الهلوسة التي بُني هذا النظام ليمنعها. لا انتساب ولا تكامل قائم.
SITE_PROFILES = [
    {"id": "kfshrc-riyadh", "name": "King Faisal Specialist Hospital & Research Centre",
     "name_ar": "مستشفى الملك فيصل التخصصي ومركز الأبحاث", "city": "Riyadh"},
    {"id": "kfmc-riyadh", "name": "King Fahad Medical City",
     "name_ar": "مدينة الملك فهد الطبية", "city": "Riyadh"},
    {"id": "kauh-jeddah", "name": "King Abdulaziz University Hospital",
     "name_ar": "مستشفى جامعة الملك عبدالعزيز", "city": "Jeddah"},
    {"id": "kfhu-khobar", "name": "King Fahd Hospital of the University",
     "name_ar": "مستشفى الملك فهد الجامعي", "city": "Al Khobar"},
]


class PullRequest(BaseModel):
    patient_id: str = Field(min_length=1, max_length=64)


def _connector_cards() -> list[dict[str, Any]]:
    mwl = worklist.status()
    return [
        {
            "id": "fhir",
            "standard": "HL7 FHIR R4",
            "direction": "inbound",
            "endpoint": settings.fhir_base_url.rstrip("/"),
            "live": True,
            "testable": True,
            "state": "configured",
            "detail": {
                "resources": ["Patient", "Observation"],
                "loinc": {"creatinine": fhir.LOINC_CREATININE,
                          "body_weight": fhir.LOINC_BODY_WEIGHT},
                "conversion": f"mg/dL x {fhir.MG_DL_TO_UMOL_L} -> umol/L",
                "read_only": True,
                "identifiers_never_read": list(fhir.WITHHELD_FIELDS),
            },
        },
        {
            "id": "mwl",
            "standard": "DICOM Modality Worklist (C-FIND)",
            "direction": "outbound",
            "endpoint": f"{settings.mwl_ae_title}@:{settings.mwl_port}",
            "live": True,
            "testable": True,
            "state": "running" if mwl["running"] else ("error" if mwl["error"] else "stopped"),
            "detail": mwl,
        },
        {
            "id": "modality",
            "standard": "DICOM — calling AE",
            "direction": "inbound",
            # لا يُكتب يدوياً: يُكتشف من أول استعلام يصل الخادم.
            "endpoint": mwl["callers"][0]["ae_title"] if mwl["callers"] else None,
            "live": False,
            "testable": False,
            "state": "discovered" if mwl["callers"] else "awaiting",
            "detail": {"callers": mwl["callers"],
                       "note": "Populated by the first C-FIND that reaches the server."},
        },
        {
            "id": "injector",
            "standard": "Injector protocol limits (local)",
            "direction": "outbound",
            "endpoint": None,
            "live": False,
            "testable": False,
            "state": "local",
            "detail": {"model": samaam.device.model,
                       "enforced_by": "policy_node — volume, flow rate, iodine load"},
        },
    ]


@app.get("/connectors")
def connectors() -> dict[str, Any]:
    return {
        "notice": SYNTHETIC_NOTICE,
        "connectors": _connector_cards(),
        "site_profiles": SITE_PROFILES,
        "site_profiles_note": (
            "Real institutions, listed as deployment targets only. Endpoints and AE "
            "titles live on hospital networks and are not public; they are filled in "
            "on installation. No affiliation or integration is claimed."
        ),
    }


@app.post("/connectors/{connector_id}/test")
def connector_test(connector_id: str) -> dict[str, Any]:
    """فحص اتصال حيّ. يُنفَّذ عند الطلب ولا يُخزَّن ولا يُخمَّن."""
    if connector_id == "fhir":
        return fhir.probe().to_dict()
    if connector_id == "mwl":
        status = worklist.status()
        return {
            "ok": status["running"],
            "detail": status["error"] or (
                f"Listening on {status['ae_title']}@:{status['port']} — "
                f"{status['queries']} queries, {status['served']} served, "
                f"{status['withheld']} withheld"
                if status["running"] else "Server is not running."
            ),
            "endpoint": f"{status['ae_title']}@:{status['port']}",
            "sop_classes": status["sop_classes"],
        }
    raise HTTPException(404, f"No testable connector '{connector_id}'.")


@app.post("/connectors/fhir/pull")
def connector_fhir_pull(body: PullRequest) -> dict[str, Any]:
    """يسحب مريضاً حقيقياً من خادم FHIR، بالشكل الذي يفهمه الكونسول."""
    try:
        pulled = fhir.fetch_patient(body.patient_id)
    except LookupError as exc:
        raise HTTPException(404, str(exc)) from exc
    except Exception as exc:
        raise HTTPException(502, f"FHIR request failed: {type(exc).__name__}: {exc}") from exc
    return {**pulled.to_dict(), "notice": SYNTHETIC_NOTICE}



# ── تقديم الواجهة من الخدمة نفسها (عقدة SINK) ──────────────────────
# في النشر تُقدَّم الواجهة المبنية من هذه الخدمة، لا من استضافة منفصلة:
# فتصير الواجهة والـ API على أصل واحد — بلا CORS، وبلا خلط http/https،
# وبلا الحاجة إلى ضبط VITE_API_BASE_URL أصلاً.
#
# يُسجَّل هذا آخر شيء عمداً: FastAPI يطابق المسارات بالترتيب، فكل نقاط
# النهاية أعلاه تفوز، والباقي يسقط على index.html كما يقتضي توجيه SPA.
# وإن لم يكن هناك بناء (تطوير محلي بـ vite dev) فلا يُسجَّل شيء.

WEB_DIST = (settings.base_dir / "web" / "dist").resolve()

if (WEB_DIST / "index.html").is_file():
    if (WEB_DIST / "assets").is_dir():
        app.mount("/assets", StaticFiles(directory=WEB_DIST / "assets"), name="assets")

    # الواجهة والـ API يتشاركان مسارات بعينها: /audit و/connectors صفحتان
    # ونقطتا نهاية في آنٍ واحد، ونقاط النهاية مسجَّلة أولاً فتفوز. النتيجة أن
    # تحديث صفحة سجل التدقيق كان يعرض JSON خاماً بدل التطبيق — وهو عطل قائم
    # من قبل هذه الشاشة، لا يظهر بالتنقّل داخل الواجهة بل بأول إعادة تحميل.
    #
    # الفرق بين الطلبين ليس في المسار بل في نيّة الطالب: المتصفح ينتقل بـ
    # Accept: text/html، بينما عميل الواجهة يطلب application/json صراحةً في
    # كل نداء. فالتفاوض على المحتوى هو الفصل الصحيح هنا.
    _SPA_EXEMPT = {"/docs", "/redoc", "/openapi.json", "/docs/oauth2-redirect"}

    @app.middleware("http")
    async def serve_spa_navigations(request: Request, call_next: Any) -> Any:
        accept = request.headers.get("accept", "")
        if (
            request.method == "GET"
            and "text/html" in accept
            and request.url.path not in _SPA_EXEMPT
            and not request.url.path.startswith("/assets/")
            and "." not in request.url.path.rsplit("/", 1)[-1]
        ):
            return FileResponse(WEB_DIST / "index.html")
        return await call_next(request)

    @app.get("/{path:path}", include_in_schema=False)
    def spa(path: str) -> FileResponse:
        candidate = (WEB_DIST / path).resolve()
        # الشرط الأخير يمنع الخروج من مجلد البناء عبر مسار مُلفَّق.
        if path and candidate.is_file() and WEB_DIST in candidate.parents:
            return FileResponse(candidate)
        return FileResponse(WEB_DIST / "index.html")
