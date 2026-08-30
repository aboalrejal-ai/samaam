# ═══════════════════════════════════════════════════════════════════
#  صِمَام — صورة واحدة تحمل البوابة كاملة
#
#  الواجهة تُبنى في مرحلة، والخدمة تقدّمها من نفس الأصل في المرحلة
#  الثانية: عملية واحدة على منفذ واحد، بلا CORS وبلا مضيف ثابت منفصل.
#
#  وقاعدة المعرفة تُبنى داخل الصورة، فنموذج التضمين والفهرس محزومان:
#  الحاوية تقلع جاهزة، ولا تحتاج شبكة لتسترجع أو تحجب.
# ═══════════════════════════════════════════════════════════════════

# ── ١ · بناء الواجهة ───────────────────────────────────────────────
FROM node:22-slim AS web

WORKDIR /web
COPY web/package.json web/package-lock.json ./
RUN npm ci
COPY web/ ./
RUN npm run build


# ── ٢ · الخدمة ─────────────────────────────────────────────────────
FROM python:3.13-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    HF_HOME=/opt/hf

WORKDIR /opt/samaam

# نسخة المعالج من torch: ٥٣٥ ميجا بدل ~٢٫٥ جيجا لنسخة CUDA الافتراضية،
# والنظام لا يستخدم كرت رسوميات. تُثبَّت قبل باقي المتطلبات لتُلتقط
# كطبقة مخبَّأة لا يعيدها كل بناء.
RUN pip install --no-cache-dir torch --index-url https://download.pytorch.org/whl/cpu

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ app/
COPY kb/ kb/
COPY scenarios/ scenarios/
COPY run_demo.py .
COPY --from=web /web/dist web/dist

# الفهرس والنموذج يُحزمان هنا، لا عند الإقلاع.
RUN python -m app.ingest --reset

# مستخدم غير جذر. ChromaDB يفتح قاعدته للكتابة، فيُملَّك مجلدها وحده.
RUN useradd --system --create-home samaam \
 && chown -R samaam:samaam /opt/samaam/kb/chroma
USER samaam

# 8000 للواجهة والـ API، و11112 لخادم قائمة العمل الذي يسأله الجهاز.
EXPOSE 8000 11112

HEALTHCHECK --interval=30s --timeout=5s --start-period=40s --retries=3 \
  CMD python -c "import urllib.request;urllib.request.urlopen('http://127.0.0.1:8000/health').read()"

CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}"]
