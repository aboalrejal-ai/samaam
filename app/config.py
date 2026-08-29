"""إعدادات صمّام — كل شيء يُقرأ من البيئة، لا مفاتيح في الكود."""

from pathlib import Path

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # نموذج الاستدلال (M) — أي مزوّد متوافق مع OpenAI
    llm_base_url: str = "https://api.z.ai/api/paas/v4"
    llm_api_key: str = ""
    llm_model: str = "glm-4.6"
    llm_temperature: float = 0.1

    # التضمين (PP) — محلي داخل ChromaDB، بلا مفتاح
    embed_model: str = "all-MiniLM-L6-v2"

    # المسارات
    base_dir: Path = Path(__file__).resolve().parent.parent
    kb_dir: Path = base_dir / "kb"
    sources_dir: Path = kb_dir / "sources"
    chroma_dir: Path = kb_dir / "chroma"
    framework_file: Path = kb_dir / "framework" / "dimensions.json"
    scenarios_dir: Path = base_dir / "scenarios"

    # التقطيع والاسترجاع
    chunk_size: int = 900
    chunk_overlap: int = 120
    retrieval_top_k: int = 6
    # تحت هذه العتبة تُعد الأدلة غير كافية ويرفض النظام الإفتاء
    min_similarity: float = 0.35

    class Config:
        env_prefix = "SAMAAM_"
        env_file = ".env"


settings = Settings()
