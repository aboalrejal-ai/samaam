"""قاعدة المعرفة — ChromaDB مع تضمين محلي.

ثلاث مجموعات:
  policies  سجلات تنظيمية مُهيكلة، لكل سجل معرّف ثابت وحالة تحقق
  sources   مقاطع من الوثائق الأصلية (PDF) لإسناد الاستشهاد
  gaps      الثغرات التنظيمية — تحليلنا لا نص تنظيمي، ولذلك تُعزَل
            حتى لا تزاحم السجلات في استرجاع عقدة السياسات

القاعدة الحاكمة: لا يُسترجَع سجل حالته UNVERIFIED للاستناد إليه في
الحجب. الاسترجاع يفلتر عليها افتراضياً.
"""

from __future__ import annotations

from typing import Any

import chromadb
from chromadb.utils import embedding_functions

from app.config import settings

POLICIES = "policies"
SOURCES = "sources"
GAPS = "gaps"

# نماذج e5 مدرَّبة على هاتين البادئتين؛ إغفالهما يخفض الدقة.
_Q, _P = "query: ", "passage: "


class KnowledgeBase:
    def __init__(self, persist_dir: str | None = None) -> None:
        self._client = chromadb.PersistentClient(
            path=persist_dir or str(settings.chroma_dir)
        )
        # نموذج متعدد اللغات — الافتراضي في ChromaDB إنجليزي فقط،
        # وقد ثبت بالاختبار أنه يفشل تماماً على الاستعلامات العربية.
        self._embed = embedding_functions.SentenceTransformerEmbeddingFunction(
            model_name=settings.embed_model
        )
        self._cache: dict[str, chromadb.Collection] = {}

    def collection(self, name: str) -> chromadb.Collection:
        if name not in self._cache:
            self._cache[name] = self._client.get_or_create_collection(
                name=name,
                embedding_function=self._embed,
                metadata={"hnsw:space": "cosine"},
            )
        return self._cache[name]

    # ── كتابة ────────────────────────────────────────────────
    def reset(self) -> None:
        for name in (POLICIES, SOURCES, GAPS):
            try:
                self._client.delete_collection(name)
            except Exception:
                pass
        self._cache.clear()

    def add(self, name: str, ids, documents, metadatas) -> None:
        # البادئة تدخل في التضمين فقط؛ النص المخزَّن يبقى نظيفاً للعرض.
        self.collection(name).upsert(
            ids=ids,
            documents=[_P + d for d in documents],
            metadatas=metadatas,
        )

    # ── قراءة ────────────────────────────────────────────────
    def search(
        self,
        query: str,
        *,
        name: str = POLICIES,
        top_k: int | None = None,
        verified_only: bool = True,
        category: str | None = None,
    ) -> list[dict[str, Any]]:
        """بحث دلالي. verified_only=True هو الوضع الآمن الافتراضي."""
        where: dict[str, Any] = {}
        if verified_only:
            where["verification"] = "VERIFIED"
        if category:
            where["category"] = category

        res = self.collection(name).query(
            query_texts=[_Q + query],
            n_results=top_k or settings.retrieval_top_k,
            where=where or None,
        )
        out = []
        for doc, meta, dist in zip(
            res["documents"][0], res["metadatas"][0], res["distances"][0]
        ):
            similarity = 1 - dist
            if similarity < settings.min_similarity:
                continue
            out.append({
                **meta,
                "content": doc.removeprefix(_P),
                "similarity": round(similarity, 3),
            })
        return out

    def get(self, record_id: str, *, name: str = POLICIES) -> dict[str, Any] | None:
        """جلب سجل بمعرّفه — الطريق الذي تستخدمه عقدة السياسات.

        الحجب الحتمي يستشهد بمعرّف صريح، لا بنتيجة بحث دلالي، حتى لا
        يتغيّر السند القانوني بتغيّر صياغة السؤال.
        """
        res = self.collection(name).get(ids=[record_id])
        if not res["ids"]:
            return None
        return {
            **res["metadatas"][0],
            "content": res["documents"][0].removeprefix(_P),
        }

    def count(self, name: str) -> int:
        return self.collection(name).count()
