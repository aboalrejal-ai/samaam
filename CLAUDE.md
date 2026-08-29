# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

**صِمَام (Samaam)** — a hackathon submission for the **ITU AI Readiness Hackathon — Kingdom of Saudi Arabia**, Health/Radiology track.

As of now the repo contains **specification documents only — no code, no commits**. The first implementation work in this repo is greenfield.

```
docs/            Samaam.md (concept) · Hackathon-Guide.md (the contract) · Knowledge-Base.md (RAG corpus)
kb/sources/      Primary source PDFs — Y.3172 standard, WHO health-AI ethics, NSDAI, ITU AI4G KSA
kb/framework/    dimensions.json — official ITU 13 dimensions / 6 factors / 111 metrics
reference/organizers/   Organizers' reference code (read-only, do not import)
app/             Samaam implementation
scenarios/       The three mandatory demo scenarios
```

`docs/Hackathon-Guide.md` is the spec of record. Where it and any other file disagree, the guide wins.

## Hard constraints (non-negotiable — these are graded)

- **Deadline: 31 August 2026, 23:59 Riyadh.** Judging day 14 Sept 2026, Riyadh.
- Technical report **≤ 5 pages** PDF. Demo video **≤ 7 minutes**, with subtitles. Exceeding either loses points.
- GitHub repo must be **public, MIT/Apache-2.0, and contain zero API keys**. All secrets via env vars only.
- **100% synthetic data.** Never commit or generate real/realistic patient records. Every UI screen and the report must carry the notice: *"بيانات محاكاة لأغراض الهاكاثون فقط"*.
- **Zero hallucination rule.** The Policy Node must never invent a law name, article number, or URL. If the retrieved context does not support a claim, it must return `INSUFFICIENT_EVIDENCE`.
- Knowledge Base must hold **15–40 sources with direct, working links to the actual documents** — never ministry homepages.
- The MVP must be **functionally operational** (live RAG retrieval + real policy enforcement), not a static UI mockup.

## Architecture: ITU-T Y.3172 seven-node pipeline

Every module must map to a named node, and code/docs should use these symbols verbatim (`SRC`, `C`, `PP`, `M`, `P`, `D`, `SINK`) — the mapping itself is a judging criterion.

```
SRC → C → PP → M → P → D → SINK
                    ↑
              Knowledge Base (pgvector)
```

- **SRC** — Saudi regulation texts, synthetic patient record, technician-entered scanner settings.
- **C** — API ingest; simulates HL7 FHIR (patient data) and DICOM Modality Worklist (device commands).
- **PP** — PDPL anonymization, chunking, embedding generation.
- **M** — LLM + RAG retrieval; drafts the clinical/regulatory reasoning.
- **P** — **Policy Node. The heart of the project.** Deterministic guardrail that inspects M's output against retrieved policy chunks and either approves, warns, or blocks.
- **D** — attaches citations (authority, document title, section, direct URL) and writes the audit log.
- **SINK** — operator UI, and the mock device API that receives (or is denied) the execute command.

### The Policy Node's six verdicts

`P` must classify every scenario into exactly one of: `COMPLIANT`, `VIOLATION`, `AMBIGUITY`, `CONFLICT`, `POTENTIAL_GAP`, `INSUFFICIENT_EVIDENCE`.

`VIOLATION` → block execution and name the violated article + issuing authority. `POTENTIAL_GAP` and `INSUFFICIENT_EVIDENCE` → mandatory human-in-the-loop; never auto-approve.

**`P` must be deterministic code, not a second LLM call.** An LLM may draft the reasoning inside `M`, but the block/allow decision has to be enforceable, reproducible rule logic — otherwise the safety claim collapses under judging, and the whole pitch is that the AI is *constrained* by policy rather than trusted.

### The domain mechanic

The mock device API (representing the CT scanner and the Bayer-Medrad-style contrast injector) must return **`403 Forbidden — Policy Violation`** when `P` rejects the settings. That HTTP rejection *is* the demo's money shot: an unsafe contrast dose for a low-GFR oncology patient never reaches the hardware.

## The three mandatory demo scenarios

The video and the report must both walk through all three, in this order:

1. **Baseline / compliant** — normal patient, settings pass, answer is approved *with visible citations*.
2. **Operational drift** — low `GFR` + high iodinated contrast request → `P` issues a conditional block, cites the protocol, and proposes a safe alternative (low-dose CT / adjusted contrast).
3. **Controversial breach** — attempt to export or commercially exploit patient data → hard security override citing PDPL + SDAIA ethics, session halted, incident written to the audit trail.

## Stack

LLM inference goes through any OpenAI-compatible provider (GLM/Z.ai by default, OpenRouter or Alibaba DashScope by swapping two env vars) via `app/llm.py`. Embeddings are computed locally by ChromaDB — no key, no network — so retrieval keeps working if the venue's wifi dies during the demo.

The guide's Gemini + Supabase code in §9 is illustrative only; do not wire it up.

## Reference implementation in `Hackathon-Guide.md`

Section 9 contains ready-to-use `pgvector` schema (`policies_kb`, `match_policies` RPC, HNSW index) and a Supabase Edge Function (`supabase/functions/policy-guardian/index.ts`). Use it as the starting point rather than designing from scratch.

Read it for the Policy Node system prompt and the six-verdict contract, not for the stack. The dimension mismatch it contains (768 vs. the KB's 1536) is moot now that ChromaDB owns the embedding.

## Knowledge Base gaps to close before submission

`Knowledge-Base.md` is built for the **Education** track, not Health. It has full SDAIA AI Ethics and PDPL coverage (including minors/student data, which this project does not use), and **no health-sector regulation at all**. Missing and required:

- SFDA medical-device and Software-as-a-Medical-Device (SaMD) regulations.
- MoH clinical practice guidelines: radiology protocols, contrast administration limits, GFR thresholds.
- PDPL provisions specific to health data and automated diagnostic liability.
- ~~WHO / ITU guidance on ethics and governance of AI in health~~ — covered by `kb/sources/WHO_Ethics_Governance_AI_Health.pdf`.

The education/minors section (student data, Noor/MADARES, parental consent) has been removed — Samaam has no minor or student subjects, and leaving it in signalled a corpus copied from another project.

Still to fix: several citations are law-firm and vendor commentary (`iclg.com`, `cookiebot.com`, `scribd.com`, consultancy blogs) rather than primary government documents. Judging rewards official primary sources — replace them as verified sources arrive.

