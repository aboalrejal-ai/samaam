"""عقدة النموذج (M) — عميل واحد يخدم GLM و OpenRouter و DashScope.

الثلاثة يتكلمون بروتوكول OpenAI، فالتبديل بينهم تغييرُ متغيّرَي بيئة
لا تغييرُ كود. عقدة السياسات (P) لا تستدعي هذا الملف إطلاقاً — قرار
الحظر حتميّ ولا يُترك لنموذج لغوي.
"""

from __future__ import annotations

from openai import OpenAI

from app.config import settings

_client: OpenAI | None = None


def client() -> OpenAI:
    global _client
    if _client is None:
        if not settings.llm_api_key:
            raise RuntimeError(
                "SAMAAM_LLM_API_KEY غير مضبوط. انسخ .env.example إلى .env وضع المفتاح."
            )
        _client = OpenAI(
            base_url=settings.llm_base_url,
            api_key=settings.llm_api_key,
        )
    return _client


def complete(system: str, user: str, *, json_mode: bool = False) -> str:
    """استدعاء واحد للنموذج. يرجع النص الخام."""
    kwargs = {}
    if json_mode:
        kwargs["response_format"] = {"type": "json_object"}

    response = client().chat.completions.create(
        model=settings.llm_model,
        temperature=settings.llm_temperature,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
        **kwargs,
    )
    return response.choices[0].message.content or ""


def health_check() -> tuple[bool, str]:
    """تحقّق سريع من أن المزوّد يستجيب. يُستخدم قبل العرض."""
    try:
        reply = complete("Reply with the single word: ok", "ping")
        return True, f"{settings.llm_model} @ {settings.llm_base_url} → {reply.strip()[:40]}"
    except Exception as exc:
        return False, f"{type(exc).__name__}: {exc}"
