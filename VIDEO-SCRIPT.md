# Samaam — Demo Video Script

**Target 5:15. Hard ceiling 7:00 (hackathon rule).**
The spoken text below is **731 words ≈ 5:00** at an unhurried pace; the screen
pauses take it to roughly **5:15**. That leaves nearly two minutes of margin
against the limit, which is where you want to be — recordings always run longer
than the page. To land nearer **4:40**, cut the one marked block (see the end).

**Format: screen recording with voice-over.** The organisers require the *real
interface* to be shown and the three scenarios to be run live. A face is not
required anywhere in the rules. A small webcam bubble during the opening and
the closing is optional and costs nothing; the screen must carry the rest.

Everything in this script is on screen and reproducible. No number here is
rounded up, and no claim is made that the system does not demonstrate.

---

## Before you record

| | |
| :--- | :--- |
| Servers | Backend on `:8000`, frontend on `:5173`. Sidebar footer must read **Connected · 43 · 6 · 1338** |
| Window | 1920×1080, browser zoom **125%**, **light theme**, **English** |
| Start state | **Console page, freshly loaded, no case selected** — the empty form is the first beat |
| Second tab | `https://www.moh.gov.sa/en/Ministry/MediaCenter/Publications/Documents/Protocols-of-CM.pdf` pre-opened, so the live link click resolves instantly |
| Rehearse once | The block is instant; the written explanation takes ~40 s and lands while you keep talking. **Never wait for it** — its lateness is a point you make at 4:25 |
| Audio | One clean take per section is better than one long take. Cut between sections |

Every screen carries **بيانات محاكاة لأغراض الهاكاثون فقط**. Do not crop it out.

---

## 0:00 – 0:30 · The problem

> **[Screen: the console, empty. Optional webcam bubble.]**

"Samaam is the Arabic word for a valve.

It is a policy gateway that sits between the radiology console and the CT
scanner. Every day a technologist types acquisition parameters and sends them to
the machine. Between that keyboard and the scanner, nothing reads the patient's
renal function, and nothing checks the request against Saudi regulation.

Samaam does both — before the exposure."

---

## 0:30 – 1:05 · What is actually missing

> **[Screen: stay on the console. Slow scroll down the form.]**

"Our track is health and radiology. The problem is not diagnosis — it is
enforcement.

The Kingdom already has the rules: the Ministry of Health contrast protocol, the
national reference levels bound by Royal Decree six-zero-zero-five-seven, and
the Personal Data Protection Law. What is missing is an instrument that applies
them at the moment of acquisition — today they are checked afterwards, by
periodic report.

Samaam makes that check prospective, in deterministic code. No language model
can allow or block anything."

---

## 1:05 – 1:40 · The knowledge base

> **[Click: Knowledge base. Type in Arabic: متى يوقف الميتفورمين؟]**

"Everything it enforces comes from here — forty-three verified records from
Saudi primary sources, one thousand three hundred chunks across seven documents.

Asked in Arabic when metformin must be held before contrast, retrieval returns
the Ministry protocol first: section five point three, page twenty-eight."

> **[Click the citation link. The government PDF opens.]**

"And that link opens the document itself, on the Ministry's own domain.

Retrieval, not conversation. Ask what the corpus does not cover and it returns
nothing — which is also an answer."

---

## 1:40 – 2:05 · Insufficient evidence

> **[Back to the console. The form is still empty. Click: Send to the device.]**

"Before the clinical cases, the empty request. No creatinine, no dose.

**Evidence does not suffice. Four hundred and three.**

Samaam will not estimate a renal function it was never given, nor invent a
reference level where none is published. Missing data stops here."

---

## 2:05 – 2:30 · The compliant case

> **[Click: SC-01. Then Send to the device.]**

"Now a real request. Fifty-eight years old, lung cancer surveillance, eGFR
eighty-one. Chest CT at nine point five milligray.

Within the national reference level. Prophylaxis not indicated. **Compliant —
two hundred.** The worklist reaches the scanner with its citations attached."

---

## 2:30 – 3:35 · The refusal

> **[Click: SC-02. Point at the renal panel.]**

"Case two was written by a consultant radiologist.

Sixty-two, metastatic colorectal cancer, creatinine two point six. Samaam
computes the eGFR itself, with the CKD-EPI equation the Ministry protocol prints
on page twenty-one: **nineteen.** Stage four chronic kidney disease, on
metformin and on oxaliplatin.

At the end of a long shift the standard adult protocol is loaded: one hundred
and fifty millilitres, CTDIvol eighteen, DLP nine hundred."

> **[Click: Send to the device. Let the rail animate.]**

"Watch the rail. The request crosses the seven nodes — and stops at P.

**Four hundred and three. The scanner never received it.**

Four findings. The dose exceeds the national reference level — red, and
statutory. Prophylaxis indicated and not ordered — high risk. But read the
wording: **held for review, not prohibited.**

That is deliberate. No eGFR value forbids contrast outright; the protocol makes
stage four to five a relative contraindication. A system that refuses at a lab
value replaces the physician — and that is what physicians reject.

Two amber findings — metformin, and a nephrotoxic agent — confirm and proceed.
Every finding carries its article and a working link."

---

## 3:35 – 4:00 · The override

> **[Click: Override and release → type a consultant name → confirm.]**

"So a radiologist reviews it, and releases it under their own name. **Two
hundred.** The valve reopens, and keeps the mark.

That is the second gap we documented: no Saudi provision allocates liability
when a fatigued technologist accepts an automated recommendation. Samaam does
not fix the law — it puts a name on the decision."

---

## 4:00 – 4:25 · The breach

> **[Click: Data request → Load the exploitation attempt → Submit request.]**

"Case three. A service account exporting four thousand two hundred oncology
records outside the Kingdom, for a marketing campaign.

Three statutory violations — Articles twenty-three, one and twenty-nine of the
Personal Data Protection Law. **Session terminated.**

And note the difference: here the same consultant name is **refused.** A
clinician may accept clinical risk for their own patient. None may authorise
what the law forbids."

---

## 4:25 – 4:50 · Architecture, and where the model is not

> **[Point at the rail: SRC · C · PP · M · P · D · SINK.]**

"The architecture is ITU-T Y point three one seven two, node for node.
Identifiers are dropped at PP, the model drafts the explanation at M, and **P —
the policy node — decides.**

That block took twenty-nine milliseconds; the explanation took forty seconds,
because that part is the model. They are separate on purpose: remove the model
entirely and Samaam still blocks correctly."

---

## 4:50 – 5:15 · Readiness, gaps, and close

> **[Click: Readiness — the three marked dimensions. Then Gap matrix.]**

"We claim three of the thirteen readiness dimensions, with evidence rather than
ambition: AI and policies, data governance and privacy, human oversight.

And six regulatory gaps — each a provision we searched for and did not find,
each with a recommendation to the regulator.

The repository is public and Apache-licensed; all data is synthetic.

That is Samaam. The AI is not trusted — it is constrained. Thank you."

---

## Delivery notes

You are a physician; the clinical terms are yours to say naturally. Three
things still help:

| Term | Note |
| :--- | :--- |
| صِمَام / Samaam | *sa-MAAM* — say it once slowly at 0:00, the name has to land |
| 19.1 | say **"nineteen"** — the decimal adds nothing aloud |
| Y.3172 | "why · three-one-seven-two" |
| Royal Decree 60057 | "six-zero-zero-five-seven" — read as digits, not "sixty thousand" |

Pause after every number that appears on screen. The subtitle and the pixel
should agree in the viewer's eye.

## If it needs to be shorter

Cut **1:05 – 1:40, the knowledge base** (76 words, ~35 s with the link click).
It is the only self-contained block; everything else builds on what came before.
That lands you near **4:40**.

If you cut it, add four words at 2:30 — *"from the Ministry protocol"* — so the
citations still have a stated origin on screen.

## If something goes wrong

| Problem | Do this |
| :--- | :--- |
| Explanation card still spinning | Ignore it and keep talking. At 4:25 its lateness becomes the argument |
| Sidebar dot turns red | Backend stopped. Restart it, re-record from the current section only |
| SC-01 returns 403 | The device is still LOCKED from a previous take. Reload the page and re-send |
| Override dialog will not open | The finding was `CONFIRM`, not `AUTHORISE`. Reload SC-02 and re-send |

## Subtitles — required

Burn in or attach captions. Record clean audio, generate in CapCut, then check
these five by eye: **403**, **19.1**, **Royal Decree 60057**, **Y.3172**,
**PDPL Article 29**. Auto-captioning mangles all five.
