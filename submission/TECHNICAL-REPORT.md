# صِمَام · SAMAAM
### An AI-Hardware Policy Gateway for Oncology Radiology
**ITU AI Readiness Hackathon — Kingdom of Saudi Arabia · Health & Radiology Track**

> ⚠️ بيانات محاكاة لأغراض الهاكاثون فقط — *Synthetic data, hackathon use only*

---

## Page 1 · Executive Summary

**The problem.** A radiology technologist on a night shift enters acquisition
parameters for a contrast-enhanced CT. The patient is an oncology case whose
kidney function is impaired by chemotherapy. The settings are routine, and for
this patient they are dangerous. Published evidence puts clinically important
CT interpretation errors at **3.0% at night against 2.0% by day, rising to 3.7%
in the last part of the shift**. Nothing between that console and the scanner
reads the patient's chart.

**The solution.** Samaam is a policy gateway that sits between the technologist's
console and the device. Every worklist passes through it. It reads the patient's
renal function, compares the requested settings against Saudi regulation, and
either releases the acquisition or returns **HTTP 403 — Policy Violation** with
the provision it is enforcing, its issuing authority, and a working link to the
source document.

**What makes it defensible.** The block is deterministic code, not a model. A
language model drafts the explanation *after* the decision is taken; it is never
in the path. The verdict lands in **29 milliseconds** and the prose follows.
Pull the model out entirely and the gateway still blocks correctly.

**Two authorities, never conflated.** Exceeding the national CT dose reference
level breaches a binding instrument — Royal Decree 60057 approving Saudi Health
Council Resolution 3/88. Missing renal prophylaxis departs from a Ministry of
Health protocol, which is national but is a practice instrument, not a penalty
provision. Samaam labels them differently, in shape as well as colour. Calling
the second a legal violation would be a false legal claim, and it is exactly the
kind of overreach this hackathon asks projects to avoid.

**Team.** [names, disciplines, institution]

---

## Page 2 · Problem, and Why Existing Tools Do Not Solve It

### The clinical case

Contrast-associated acute kidney injury rises sharply with declining renal
function. The Saudi MoH protocol states the risk directly: **approximately 5% at
eGFR ≥ 60, 10% at 45–59, 15% at 30–44, and 30% below 30 mL/min/1.73 m²**. Below
30, prophylaxis is indicated and metformin must be held. An oncology patient on
platinum chemotherapy sits in the highest band while receiving repeat imaging.

### What the market already has, and what it misses

Every commercial dose-management platform — Radimetrics, DoseWatch, teamplay,
DoseTrack, DoseWise — is **retrospective**. It discovers the overexposure after
the patient has received it, and reports it to the regulator later by email.

The one prospective control that exists, **NEMA XR 25 CT Dose Check**, has
required scanners since 2010 to warn before scanning when settings would exceed
preset dose values, and to make the operator confirm or correct. It is a real,
shipped, industry-wide interlock — which is why the mechanism Samaam uses is not
speculative.

But Dose Check compares the machine against a fixed number. It cannot see the
patient.

> **CT Dose Check compares the machine to itself. Samaam compares it to the patient.**

Samaam extends the same pre-execution interlock to renal function, active
chemotherapy, metformin, and the Saudi provisions that govern them.

### Why the block must be overridable

The MoH protocol is explicit that stage 4–5 chronic kidney disease is a
**relative, not absolute**, contraindication, and that contrast must not be
withheld from a life-threatening indication on renal grounds. A permanent hard
stop would violate the protocol it claims to enforce. The literature agrees:
hard stops draw override rates of **49–96%** and breed unsafe workarounds.

So Samaam blocks conditionally. A named consultant may release the acquisition,
and the release is written to the audit trail with their name against the risk
they accepted. This is the difference between an anonymous click and an owned
decision — and it is the operational answer to the liability gap in §4.

---

## Page 3 · Architecture — ITU-T Y.3172

```
   SRC ──→ C ──→ PP ──→ M ──→ P ──→ D ──→ SINK
                               ▲
                    Knowledge Base (ChromaDB)
                    43 records · 1,338 source chunks
```

| Node | Role in the standard | Implementation in Samaam |
| :--- | :--- | :--- |
| **SRC** | Raw sources | Saudi regulation PDFs, synthetic patient record, technologist-entered settings |
| **C** | Collection | REST ingest simulating a DICOM Modality Worklist |
| **PP** | Preprocessing | Direct identifiers dropped per PDPL Art. 23; **eGFR computed with CKD-EPI exactly as the MoH protocol prints it**; local multilingual embeddings |
| **M** | Model / RAG | Retrieval over the verified corpus; drafts the explanation |
| **P** | **Policy Node** | **Deterministic rule engine. No model. Four rules, each citing its record by explicit id** |
| **D** | Distribution | Attaches citations with authority, section and URL; writes the audit entry |
| **SINK** | Application | Operator console, and the mock CT + injector that returns 403 |

### The Policy Node

`P` returns exactly one of six verdicts: `COMPLIANT`, `VIOLATION`, `AMBIGUITY`,
`CONFLICT`, `POTENTIAL_GAP`, `INSUFFICIENT_EVIDENCE`.

Three design commitments make it auditable:

1. **No model in the decision path.** The block is `if` logic over cited
   thresholds. It returns the same verdict every time and can be read by a
   regulator who does not trust machine learning.
2. **Citation by identifier, not by search.** Each rule names its record
   (`MOH-CM-PROPHYLAXIS`), so the legal basis for a block cannot drift with the
   wording of a question.
3. **Refusal to guess.** Every record carries a verification status, and
   retrieval excludes unverified records by default. A missing eGFR yields
   `INSUFFICIENT_EVIDENCE` and a referral, never an assumption.

### Sandbox and data protection

The whole system is a sandbox: a simulated scanner, 100% synthetic patients, and
the notice *بيانات محاكاة لأغراض الهاكاثون فقط* on every screen. Embeddings are
computed locally, so retrieval and the block work with the network unplugged —
only the optional explanation needs the internet.

---

## Page 4 · Policy Gaps and ITU AI Readiness 2.0

### Regulatory gaps found — by absence, verified

Three independent deep-research passes plus direct retrieval of the primary
documents. Each gap below is a text that was searched for and not found.

| # | Gap | Recommendation to the regulator |
| :--- | :--- | :--- |
| **1** | The MoH contrast protocol sets eGFR thresholds but no instrument makes compliance enforceable, unlike the dose reference levels | Bind the radiology protocols by decision, as Royal Decree 60057 bound the DRLs |
| **2** | **No provision allocates liability when a fatigued technologist accepts an AI recommendation and harm follows.** SFDA requires study of interface influence and human oversight; none of it says who pays | Allocate liability across manufacturer, facility, technologist and consultant; require a signed override |
| **3** | DRL compliance is enforced retrospectively, by periodic email to SFDA | Require the check *before* acquisition — which is what Samaam does |
| **4** | No cumulative dose ceiling for repeatedly imaged oncology patients | Track cumulative dose across facilities in the national record |
| **5** | SFDA Rule 10 classifies scanner-influencing software clearly as Class C, but no rule governs mandatory confirmation, autonomous bounds, or override logging | Issue operational governance for AI-driven acquisition |
| **6** | The PDPL governs transparency of automated decisions, not medical negligence | Integrate the data law with the health professions law |

### Readiness dimensions — three claimed, with evidence

| Dimension | Why | Evidence in the system |
| :--- | :--- | :--- |
| **D10 · AI & Policies** | Samaam *is* a policy sandbox: it evaluates domain rules against live technical requests | Six verdicts, four deterministic rules, the gap matrix |
| **D11 · Data Governance & Privacy** | Health data is Sensitive Data under PDPL Art. 1(11) | Identifiers dropped at PP; export blocked with no override path |
| **D13 · Human Collaboration & Oversight** | High-risk decisions must not be automated away | Conditional block; named consultant override; full audit trail |

We claim three of thirteen. The framework asks for evidence, and padding the
list with dimensions we cannot demonstrate would weaken the three we can.

---

## Page 5 · Evaluation and References

### Scenario results — reproducible with `python run_demo.py`

| # | Scenario | Verdict | Device |
| :--- | :--- | :--- | :--- |
| **1** | Chest CT, eGFR 81.4, dose within national levels | `COMPLIANT` | **200** — released |
| **2** | Abdomen/pelvis, **eGFR 27.7**, DLP 900, metformin not held | `VIOLATION` | **403** — withheld |
| **3** | Bulk export of oncology records abroad for marketing | `VIOLATION` | **403** — session terminated |

**Scenario 2 in detail.** Female, 63, 68 kg, metastatic colorectal cancer on
FOLFOX. Creatinine 168 µmol/L → eGFR **27.7**, computed by CKD-EPI. Four findings:

- `national_drl` — **FAIL, statutory.** CTDIvol 18.0 > 14.0 mGy; DLP 900 > 706 mGy·cm
- `renal_prophylaxis` — **FAIL, national protocol.** eGFR < 30, no prophylaxis ordered
- `metformin` — **FAIL, national protocol.** Category II, not held
- `nephrotoxic_meds` — **WARN.** Oxaliplatin is a platinum compound; the protocol names the class

A consultant override releases it and is logged. On scenario 3 the same
consultant is **refused**: a clinician may accept clinical risk for their own
patient, but none holds authority to permit processing the PDPL forbids.

### Knowledge base

**43 verified records · 6 documented gaps · 1,338 chunks from 7 primary
documents.** Bilingual retrieval — an Arabic question returns the governing
Saudi record first.

### Primary sources

| Document | Authority | Link |
| :--- | :--- | :--- |
| Protocols on the Safe Use of Contrast Media in Radiology Departments (2021) | MoH | `moh.gov.sa/en/Ministry/MediaCenter/Publications/Documents/Protocols-of-CM.pdf` |
| National Diagnostic Reference Levels, MDS-G008 v2.0 | SFDA | `sfda.gov.sa/sites/default/files/2023-02/NDRL-En.pdf` |
| AI/ML Based Medical Devices, MDS-G010 | SFDA | `sfda.gov.sa/sites/default/files/2023-01/MDS-G010ML.pdf` |
| Personal Data Protection Law (Arabic, official) | Bureau of Experts | `laws.boe.gov.sa/BoeLaws/Laws/LawDetails/b7cfae89-828e-4994-b167-adaa00e37188/1` |
| Ethics and governance of AI for health | WHO | `who.int/publications/i/item/9789240029200` |
| Y.3172 — ML architecture for future networks | ITU-T | `itu.int/rec/T-REC-Y.3172/en` |

**Repository:** `github.com/[org]/samaam` · Apache 2.0 · no keys in source
