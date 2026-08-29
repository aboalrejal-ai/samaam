# تسليم الواجهة — صِمَام

مرجع من يبني الواجهة (Cursor). اقرأه كاملاً قبل أول سطر.

الخلفية جاهزة ومختبرة. مهمة الواجهة عرض ما تنتجه، لا إعادة إنتاج منطقها.

---

## ⚠️ تناقضان في حزمة التصميم — محسومان هنا

الحزمة الأصلية تحمل تعارضين. `tokens.css` هو مصدر الحقيقة كما تنص الحزمة نفسها:

| | `DESIGN.md` و `USAGE.md` يقولان | ✅ الصحيح (`tokens.css`) |
| :--- | :--- | :--- |
| اللون الأساسي | `#0C5CAB` أزرق داكن | **`#0ea5e9` سماوي** |
| السمة | "dark theme" | **فاتحة** — `--bg: #f4f7fb` |

**لا تستخدم `#0C5CAB` ولا تبنِ سمة داكنة.** إن تعارض وصف مع توكن، فالتوكن يفوز.

---

## ١. التقنيات

```
Vite + React + TypeScript + Tailwind v4 + shadcn/ui
```

**لا Next.js.** الخلفية FastAPI مستقلة، فلا حاجة لعرض من الخادم ولا لمسارات API.

### ربط التوكنز
```css
/* src/index.css */
@import "tailwindcss";
@import "./design/tokens.css";
```
ثم انسخ كتلة `@theme` من `design/dashboard/tailwind-v4.css`.

**ممنوع:** أي قيمة hex خارج `:root` في `tokens.css`. استخدم `bg-surface` و `text-fg` و `border-border` و `text-accent`.

### تعيين ألوان shadcn
```
--primary        → var(--accent)        #0ea5e9
--background     → var(--bg)            #f4f7fb
--card           → var(--surface)       #ffffff
--foreground     → var(--fg)            #111827
--muted-foreground → var(--muted)       #64748b
--border         → var(--border)        #d8e2ee
--destructive    → var(--danger)        #ef4444
```
ألوان الحالات: `--success: #10b981` · `--warn: #f59e0b` · `--danger: #ef4444`
الخط `Inter`. الانحناء `--radius-md: 12px`.

---

## ٢. تشغيل الخلفية

```bash
cd /Users/aboarejal/Desktop/Project/samaam
.venv/bin/uvicorn app.main:app --reload --port 8000
```

يستغرق الإقلاع ~15 ثانية (تحميل نموذج التضمين). `CORS` مفتوح لـ `localhost:5173`.

---

## ٣. عقد الواجهة البرمجية

| الطريقة | المسار | الغرض |
| :--- | :--- | :--- |
| `GET` | `/health` | عدّادات القاعدة وحالة المزوّد |
| `GET` | `/scenarios` | السيناريوهات الثلاثة المعدّة |
| `POST` | `/evaluate` | تقييم — يرد 200 دائماً، والحكم في الجسم |
| `POST` | `/device/execute` | **يرد HTTP 403 فعلياً عند الحجب** |
| `GET` | `/kb/search?q=&collection=&top_k=` | بحث (عربي وإنجليزي) |
| `GET` | `/kb/record/{id}` | سجل بعينه |
| `GET` | `/kb/gaps` | الثغرات الست |
| `GET` | `/audit` | سجل التدقيق |
| `GET` | `/framework` | 13 بُعد · 6 عوامل · 111 مقياس |

توثيق تفاعلي كامل: `http://localhost:8000/docs`

### الطلب
```jsonc
{
  "worklist_id": "MWL-001",
  "patient": {
    "sex": "female", "age": 63, "weight_kg": 68,
    "serum_creatinine_umol_l": 168,     // eGFR يُحسب في الخادم
    "on_metformin": true, "aki": false,
    "medications": ["oxaliplatin", "metformin 1000mg BD"],
    "diagnosis": "Metastatic colorectal cancer"
  },
  "requested": {
    "study": "CT Abdomen & Pelvis with contrast",
    "body_region": "abdomen_pelvis",     // head | chest | abdomen_pelvis
    "kvp": 120, "mas": 260,
    "ctdivol_mgy": 18.0, "dlp_mgy_cm": 900,
    "contrast_agent": "Iohexol", "volume_ml": 120,
    "prophylaxis_ordered": false, "metformin_held": false
  },
  "override_by": null,   // اسم الاستشاري عند التجاوز
  "explain": true
}
```

### الرد
```jsonc
{
  "verdict": "VIOLATION",
  "blocked": true,
  "device_response": { "status": 403, "error": "Policy Violation", "message": "…" },
  "policy": {
    "verdict": "VIOLATION",
    "overridable": true,
    "override_reason": "A named consultant may override…",
    "checks": [
      { "rule": "national_drl", "status": "FAIL",
        "basis": "STATUTORY", "detail": "CTDIvol 18.0 mGy exceeds…",
        "cites": ["SFDA-MDS-G008-DRL", "SFDA-DRL-BINDING"] }
    ],
    "citations": [
      { "record_id": "SFDA-MDS-G008-DRL", "title": "…", "authority": "SFDA",
        "section": "Annex (2), Table 1, p. 7", "url": "https://…", "content": "…" }
    ],
    "explanation": "نص من النموذج اللغوي"
  },
  "privacy": { "identifiers_removed": ["name", "national_id"], "note": "…" }
}
```

### مسار الخصوصية — `POST /data/request`
```jsonc
{ "actor": "integration service account",
  "action": "Bulk export of oncology patient records to an external endpoint",
  "stated_purpose": "Targeted outreach for a private imaging centre campaign",
  "record_count": 4200, "destination_outside_kingdom": true, "care_purpose": false }
```
يرد **403** مع `overridable: false`. مرِّر `override_by` لتُظهر أن التجاوز **يُرفض** —
هذه هي اللقطة التي تفرّق السيناريو الثالث عن الثاني.

---

## ٤. القيم المعدودة — لا تخترع غيرها

**`verdict`** — ستة، والهاكاثون يشترطها نصاً:
`COMPLIANT` · `VIOLATION` · `AMBIGUITY` · `CONFLICT` · `POTENTIAL_GAP` · `INSUFFICIENT_EVIDENCE`

**`status`** لكل فحص:
| القيمة | اللون | الأيقونة |
| :--- | :--- | :--- |
| `PASS` | `--success` | ✓ |
| `FAIL` | `--danger` | ✕ |
| `WARN` | `--warn` | ⚠ |
| `NO_EVIDENCE` | `--muted` | ? |
| `NOT_APPLICABLE` | `--border` باهت | — |

**`basis`** — 🔴 **أهم تمييز بصري في المشروع كله:**

| القيمة | المعنى | كيف يُعرض |
| :--- | :--- | :--- |
| `STATUTORY` | ملزِم بمرسوم ملكي (٦٠٠٥٧) | شارة **ممتلئة** بـ `--danger` · «مخالفة نظامية» |
| `NATIONAL_PROTOCOL` | بروتوكول وزارة الصحة — وطني لكنه أداة ممارسة | شارة **محدَّدة الإطار** بـ `--warn` · «خروج عن البروتوكول الوطني» |
| `CLINICAL_GUIDANCE` | إرشاد مهني دولي | شارة رمادية باهتة |

**لا تسمِّ خرق بروتوكول «مخالفة نظام».** هذا ادعاء قانوني كاذب، والمشروع كله قائم على هذا التمييز.

---

## ٥. الشاشات — أربع

### أ. وحدة تحكم الفني *(الشاشة الرئيسية للفيديو)*
شاشة مقسومة: يسار إدخال، يمين نتيجة.

- بطاقة المريض: العمر، الوزن، التشخيص، الأدوية
- **`eGFR` بارز**، وتحته `المصدر: CKD-EPI — بروتوكول وزارة الصحة ص21`
- إعدادات التصوير: `kVp` · `mAs` · `CTDIvol` · `DLP` · الصبغة
- زر **«إرسال إلى الجهاز»**
- عند الحجب: لافتة `HTTP 403 — Policy Violation` عريضة بـ `--danger`
- قائمة الفحوص الأربعة، لكل فحص أيقونته وشارة سنده
- **بطاقة استشهاد** لكل مرجع: الجهة · الموضع · النص · **رابط مباشر يفتح فعلاً**
- زر «تجاوز استشاري» — يظهر فقط عند `overridable: true`، ويطلب اسماً

### ب. قاعدة المعرفة
بحث حي على `/kb/search`. جرّب بالعربية والإنجليزية. اعرض شارة التحقق:
`VERIFIED` أخضر · `UNVERIFIED` كهرماني · `HISTORICAL` رمادي.

### ج. مصفوفة الثغرات
`/kb/gaps` — ست بطاقات: ما وُجد · الأثر · التوصية.

### د. سجل التدقيق
`/audit` — جدول زمني. أبرز `EXECUTED_UNDER_OVERRIDE` و `OVERRIDE_REFUSED`؛
هما ما يثبتان أن التجاوز منسوب لشخص.

---

## ٦. إلزامي في كل شاشة

```
بيانات محاكاة لأغراض الهاكاثون فقط
```
شرط تسليم مُقيَّم. ضعه في تذييل ثابت أو شريط علوي.

---

## ٧. لا تفعل

- ❌ لا تكرر منطق الحجب في الواجهة. العتبات في الخادم وحده. الواجهة تعرض.
- ❌ لا تكتب رقماً (30 · 706 · 14) في كود الواجهة. كلها تصل في الرد.
- ❌ لا تخترع استشهاداً ولا رابطاً. اعرض ما في `citations` فقط.
- ❌ لا تخفِ `WARN`. التحذير جزء من القرار.
- ❌ لا تعرض `INSUFFICIENT_EVIDENCE` كخطأ. هو حكم مقصود: «الأدلة لا تكفي، تُحال لمختص».
- ❌ لا hex خارج التوكنز.

---

## ٨. أول أمر تشغّله

```bash
curl -s localhost:8000/scenarios | head -60
```
ثم ابنِ الشاشة (أ) على السيناريو الثاني. هو الحالة الأصعب: ثلاثة إخفاقات
وتحذير واحد وسندان مختلفان — إن عُرض صحيحاً، فالباقي أسهل.
