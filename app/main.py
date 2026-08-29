"""خدمة صمّام — FastAPI.

نقاط النهاية مصمَّمة لتستهلكها واجهة React مباشرة.
    GET  /health              حالة النظام والقاعدة والمزوّد
    GET  /scenarios           السيناريوهات الثلاثة المعدّة
    POST /evaluate            تقييم طلب تصوير عبر خط الأنابيب كاملاً
    POST /device/execute      تسليم للجهاز — يرد 403 عند الحجب
    POST /data/request        مسار الخصوصية — حظر صارم بلا تجاوز
    GET  /kb/search           بحث في قاعدة المعرفة
    GET  /kb/record/{id}      سجل بعينه
    GET  /kb/gaps             الثغرات التنظيمية
    GET  /audit               سجل التدقيق
    GET  /framework           أبعاد جاهزية ITU الـ 13
"""

from __future__ import annotations

import json
from typing import Any

from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from app.config import settings
from app.kb import GAPS, POLICIES, SOURCES, KnowledgeBase
from app.pipeline import Samaam

SYNTHETIC_NOTICE = "بيانات محاكاة لأغراض الهاكاثون فقط — Synthetic data, hackathon use only"

app = FastAPI(
    title="Samaam — AI-Hardware Policy Gateway",
    description="ITU-T Y.3172 policy gateway for oncology radiology. " + SYNTHETIC_NOTICE,
    version="0.1.0",
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

samaam = Samaam()
kb = samaam.kb


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


class EvaluationRequest(BaseModel):
    worklist_id: str | None = None
    patient: Patient
    requested: Requested
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
            "requested": body.requested.model_dump(exclude_none=False),
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


class DataRequest(BaseModel):
    request_id: str | None = None
    actor: str
    action: str
    stated_purpose: str
    record_count: int = 0
    destination_outside_kingdom: bool = False
    care_purpose: bool = False
    override_by: str | None = None


@app.post("/data/request")
def data_request(body: DataRequest) -> dict[str, Any]:
    """مسار الخصوصية — السيناريو الثالث. لا يقبل تجاوزاً إكلينيكياً."""
    result = samaam.run_data_request(
        body.model_dump(exclude={"override_by"}), override_by=body.override_by
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
