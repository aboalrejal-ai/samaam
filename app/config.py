"""إعدادات صمّام — كل شيء يُقرأ من البيئة، لا مفاتيح في الكود."""

from pathlib import Path

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # نموذج الاستدلال (M) — أي مزوّد متوافق مع OpenAI
    llm_base_url: str = "https://api.z.ai/api/coding/paas/v4"
    llm_api_key: str = ""
    llm_model: str = "glm-5.3-flash"
    llm_temperature: float = 0.1

    # التضمين (PP) — محلي، بلا مفتاح. لا بد أن يكون متعدد اللغات:
    # قاعدة المعرفة عربية وإنجليزية، والعرض سيكون بالعربية.
    embed_model: str = "intfloat/multilingual-e5-small"

    # المسارات
    base_dir: Path = Path(__file__).resolve().parent.parent
    kb_dir: Path = base_dir / "kb"
    sources_dir: Path = kb_dir / "sources"
    chroma_dir: Path = kb_dir / "chroma"
    framework_file: Path = kb_dir / "framework" / "dimensions.json"
    scenarios_dir: Path = base_dir / "scenarios"

    # موصّل نظام المستشفى (عقدة C) — HL7 FHIR R4، قراءة فقط.
    # الافتراضي خادم HAPI العام: بياناته اختبارية وتُمسح دورياً، فلا مريض
    # حقيقي يمرّ من هنا. في مستشفى فعلي يُستبدل بعنوان الشبكة الداخلية.
    fhir_base_url: str = "https://hapi.fhir.org/baseR4"
    fhir_timeout: float = 15.0

    # خادم قائمة العمل (عقدة C أيضاً) — DICOM MWL. الجهاز يسأل، ونحن نجيب.
    mwl_enabled: bool = True
    mwl_ae_title: str = "SAMAAM"
    mwl_port: int = 11112

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
