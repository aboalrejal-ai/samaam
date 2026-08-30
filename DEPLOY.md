# نشر صِمَام على VPS — رابط حيّ بلا دومين

**الخلاصة:** الواجهة والـ API صارا يُقدَّمان من **خدمة واحدة على منفذ واحد**.
لا CORS، ولا خلط `http/https`، ولا حاجة لضبط `VITE_API_BASE_URL`، **ولا حاجة
للدومين إطلاقاً** — عنوان الـ VPS نفسه هو الرابط.

```
http://<IP-الخاص-بالسيرفر>          ← يشتغل فوراً
https://srvXXXXXX.hstgr.cloud       ← اسم المضيف المجاني من Hostinger، إن وُجد
```

---

## متطلبات السيرفر

| | |
| :--- | :--- |
| النظام | Ubuntu 22.04 أو 24.04 |
| الذاكرة | **٢ جيجا فأكثر.** لو ١ جيجا، أضف ملف تبادل (الخطوة صفر) |
| المساحة | **٥ جيجا فارغة** — مكتبة `torch` وحدها ٥٣٥ ميجا |
| المنافذ | `80` مفتوح |

---

## ٠ · ملف تبادل — فقط لو الذاكرة ١ جيجا

```bash
fallocate -l 2G /swapfile && chmod 600 /swapfile && mkswap /swapfile && swapon /swapfile
echo '/swapfile none swap sw 0 0' >> /etc/fstab
```

## ١ · الأدوات

```bash
apt update && apt install -y python3 python3-venv python3-pip git curl
curl -fsSL https://deb.nodesource.com/setup_22.x | bash - && apt install -y nodejs
```

## ٢ · المشروع

```bash
git clone https://github.com/aboalrejal-ai/samaam.git /opt/samaam
cd /opt/samaam
```

## ٣ · الخلفية

```bash
python3 -m venv .venv
# مهم: النسخة الافتراضية من torch على لينكس تجرّ تعريفات CUDA بحجم ~٢٫٥ جيجا.
# هذا السطر يجلب نسخة المعالج فقط — أصغر وأسرع، والنظام لا يحتاج كرت رسوميات.
.venv/bin/pip install torch --index-url https://download.pytorch.org/whl/cpu
.venv/bin/pip install -r requirements.txt
```

**المفتاح اختياري.** بدونه كل شيء يعمل — الاسترجاع والحجب والـ `403` — ويغيب
الشرح النصّي وحده. ولو أردته:

```bash
cp .env.example .env
nano .env        # ضع مفتاحك في SAMAAM_LLM_API_KEY
```

## ٤ · قاعدة المعرفة والواجهة

```bash
.venv/bin/python -m app.ingest --reset      # ينزّل نموذج التضمين (~١٢٠ ميجا) ويبني الفهرس
cd web && npm ci && npm run build && cd ..  # ينتج web/dist الذي تقدّمه الخدمة
```

## ٥ · تشغيلها كخدمة دائمة

```bash
cat > /etc/systemd/system/samaam.service <<'EOF'
[Unit]
Description=Samaam — ITU Y.3172 policy gateway
After=network.target

[Service]
WorkingDirectory=/opt/samaam
ExecStart=/opt/samaam/.venv/bin/uvicorn app.main:app --host 0.0.0.0 --port 80
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
EOF

systemctl daemon-reload && systemctl enable --now samaam
systemctl status samaam --no-pager
ufw allow 80/tcp 2>/dev/null || true
```

**افتح `http://<IP>` — انتهى.**

```bash
curl -s http://localhost/health          # تحقّق سريع
journalctl -u samaam -f                  # السجل الحيّ عند أي عطل
```

---

## ٦ · الدومين (اختياري تماماً — بعد التسجيل)

الدومين على حساب آخر ومنطقته في Cloudflare؟ **لا يحتاج نقل الدومين ولا شهادة
ولا لمس السيرفر.** سجل واحد في Cloudflare:

| النوع | الاسم | القيمة | الوكيل |
| :--- | :--- | :--- | :--- |
| `A` | `samaam` | `<IP-السيرفر>` | 🟠 **مفعّل** |

الغيمة البرتقالية تجعل Cloudflare يقدّم `https` للزائر ويكلّم سيرفرك على `http`
— فتحصل على `https://samaam.نطاقك` بلا شهادة على السيرفر. اضبط
**SSL/TLS → Flexible**، وانتظر دقيقتين.

---

## عند التحديث

```bash
cd /opt/samaam && git pull
cd web && npm ci && npm run build && cd ..
systemctl restart samaam
```

> `app.ingest` لا يُعاد إلا إذا تغيّر متن قاعدة المعرفة.
