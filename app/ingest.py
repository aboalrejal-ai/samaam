"""عقدة المعالجة المسبقة (PP) — حقن قاعدة المعرفة.

مصدران:
  ١. kb/records/health-regulatory.json  سجلات مُهيكلة محققة يدوياً
  ٢. kb/sources/*.pdf|*.txt             نص الوثائق الأصلية، مقطَّع

التشغيل:  python -m app.ingest [--reset]
"""

from __future__ import annotations

import argparse
import json
import re
import sys

from app.config import settings
from app.kb import GAPS, POLICIES, SOURCES, KnowledgeBase


def chunk(text: str, size: int, overlap: int) -> list[str]:
    """تقطيع على حدود الجُمل قدر الإمكان، لئلا يُبتر نص نظامي في منتصفه."""
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text).strip()
    parts, buf = [], ""
    for sentence in re.split(r"(?<=[.!?؟।])\s+", text):
        if len(buf) + len(sentence) + 1 > size and buf:
            parts.append(buf.strip())
            buf = buf[-overlap:] if overlap else ""
        buf += " " + sentence
    if buf.strip():
        parts.append(buf.strip())
    return [p for p in parts if len(p) > 80]


def load_records(kb: KnowledgeBase) -> int:
    data = json.loads((settings.kb_dir / "records" / "health-regulatory.json").read_text())
    ids, docs, metas = [], [], []
    for r in data["records"]:
        ids.append(r["id"])
        # النص المُضمَّن يشمل العنوان والجهة، والملاحظة العربية إن وُجدت:
        # السجلات إنجليزية والعرض عربي، والملاحظة هي المرساة التي تربط
        # الاستعلام العربي بالسجل الإنجليزي.
        doc = f"{r['title']} — {r['authority']} — {r['section']}\n{r['content']}"
        if r.get("note"):
            doc += f"\n{r['note']}"
        docs.append(doc)
        metas.append({
            "record_id": r["id"], "title": r["title"], "authority": r["authority"],
            "section": r["section"], "url": r["url"], "year": r["year"],
            "language": r["lang"], "verification": r["verification"],
            "category": r["category"], "node": r["node"],
            "note": r.get("note", ""), "kind": "record",
        })
    kb.add(POLICIES, ids, docs, metas)

    # الثغرات تُحقن أيضاً — التقرير والواجهة يستعلمان عنها
    gids, gdocs, gmetas = [], [], []
    for g in data["gaps"]:
        gids.append(g["id"])
        gdocs.append(f"{g['title']}\n{g['finding']}\n{g['implication']}\n{g['recommendation']}")
        gmetas.append({
            "record_id": g["id"], "title": g["title"], "authority": "Samaam analysis",
            "section": "Policy gap", "url": "", "year": 2026, "language": "Arabic",
            "verification": "VERIFIED", "category": "policy_gap", "node": "D",
            "note": "", "kind": "gap",
        })
    kb.add(GAPS, gids, gdocs, gmetas)
    return len(ids), len(gids)


def load_sources(kb: KnowledgeBase) -> int:
    try:
        from pypdf import PdfReader
    except ImportError:
        print("pypdf غير مثبت — تخطّي وثائق PDF", file=sys.stderr)
        PdfReader = None

    total = 0
    for path in sorted(settings.sources_dir.iterdir()):
        if path.suffix.lower() == ".pdf" and PdfReader:
            reader = PdfReader(str(path))
            pages = [(i + 1, p.extract_text() or "") for i, p in enumerate(reader.pages)]
        elif path.suffix.lower() in (".txt", ".md"):
            pages = [(1, path.read_text(errors="ignore"))]
        else:
            continue

        ids, docs, metas = [], [], []
        for page_no, text in pages:
            for j, piece in enumerate(chunk(text, settings.chunk_size, settings.chunk_overlap)):
                ids.append(f"{path.stem}::p{page_no}::c{j}")
                docs.append(piece)
                metas.append({
                    "record_id": f"{path.stem}::p{page_no}", "title": path.stem,
                    "authority": "primary source document", "section": f"page {page_no}",
                    "url": "", "year": 0, "language": "mixed",
                    "verification": "VERIFIED", "category": "source_text",
                    "node": "SRC", "note": "", "kind": "source_chunk",
                })
        if ids:
            # دفعات صغيرة: التضمين المحلي يستهلك ذاكرة مع الملفات الكبيرة
            for i in range(0, len(ids), 200):
                kb.add(SOURCES, ids[i:i+200], docs[i:i+200], metas[i:i+200])
            total += len(ids)
            print(f"  {path.name:<48} {len(pages):>4} صفحة → {len(ids):>5} مقطع")
    return total


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--reset", action="store_true", help="حذف القاعدة وإعادة بنائها")
    args = ap.parse_args()

    kb = KnowledgeBase()
    if args.reset:
        kb.reset()
        print("أُفرغت القاعدة.\n")

    print("حقن السجلات التنظيمية…")
    n, g = load_records(kb)
    print(f"  {n} سجل تنظيمي · {g} ثغرة\n")

    print("حقن الوثائق الأصلية…")
    m = load_sources(kb)
    print(f"  {m} مقطع\n")

    print(f"policies={kb.count(POLICIES)}  gaps={kb.count(GAPS)}  sources={kb.count(SOURCES)}")


if __name__ == "__main__":
    main()
