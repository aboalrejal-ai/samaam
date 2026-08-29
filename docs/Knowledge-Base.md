# 📚 قاعدة المعرفة والسياسات الوطنية للذكاء الاصطناعي (National AI Governance Knowledge Base)

قاعدة المعرفة الرسمية المعتمدة لحوكمة الذكاء الاصطناعي وحماية البيانات في المملكة العربية السعودية، مخصصة للحقن في قاعدة بيانات المتجهات (Vector Database / RAG) وتغذية عقدة السياسات (Policy Node - P).

---

## 📑 فهرس محتويات قاعدة المعرفة
1. **[الجزء الأول: إطار ومبادئ أخلاقيات الذكاء الاصطناعي (SDAIA AI Ethics Framework)](#الجزء-الأول-إطار-ومبادئ-أخلاقيات-الذكاء-الاصطناعي-sdaia-ai-ethics-framework)**
   - النطاق والتعريفات ومحرك تصنيف المخاطر الرباعي (4 Risk Tiers)
   - المبادئ الأخلاقية السبعة ومطابقتها مع دورة حياة الأنظمة
   - إرشادات الذكاء الاصطناعي التوليدي وأدوات التقييم والتدقيق (PID.1 - PID.14)
2. **[الجزء الثاني: نظام حماية البيانات الشخصية السعودي ولائحته التنفيذية (Saudi PDPL)](#الجزء-الثاني-نظام-حماية-البيانات-الشخصية-السعودي-ولائحته-التنفيذية-saudi-pdpl)**
   - هرمية تصنيف البيانات الوطنية (4 مستويات)
   - المسوغات النظامية الست لمعالجة البيانات
   - حقوق أصحاب البيانات وضوابط البيانات الصحية الحساسة
   - العقوبات والمسؤولية الجنائية

---

# الجزء الأول: إطار ومبادئ أخلاقيات الذكاء الاصطناعي (SDAIA AI Ethics Framework)

# Saudi Data and AI Authority (SDAIA) AI Ethics Principles and Governance Framework

## Executive Overview, Statutory Mandate, and Institutional Ecosystem

The Kingdom of Saudi Arabia has established a centralized regulatory architecture for data governance and artificial intelligence, directed primarily by the Saudi Data and AI Authority (SDAIA). Enacted pursuant to the Council of Ministers Resolution No. (292) dated 27/04/1441 AH, SDAIA is invested with the statutory mandate to formulate, enforce, and monitor compliance with national policies, governance mechanisms, technical standards, and ethical controls governing data and artificial intelligence technologies. Under document classification number SDAIA-P114E (Version 1.0), SDAIA promulgated the official *AI Ethics Principles* framework, establishing an operational control layer designed to evaluate whether artificial intelligence systems deployed within the Kingdom meet normative benchmarks of fairness, privacy, safety, explainability, accountability, human oversight, and societal benefit prior to and throughout production deployment.

The regulatory framework operates within an interconnected ecosystem designed to fulfill the strategic imperatives of Saudi Vision 2030 and the National Strategy for Data and AI (NSDAI). SDAIA functions alongside specialized subsidiary and complementary bodies. Upstream data governance, data classification, open data sharing, and data architecture are regulated by the National Data Management Office (NDMO), which sits within the same institutional orbit. Personal data processing within machine learning pipelines is supervised through channels aligned with the Personal Data Protection Law (PDPL), enacted under Royal Decree No. M/19. Infrastructure security, encryption baselines, and vulnerability management are regulated by the National Cybersecurity Authority (NCA). Telecommunications hosting, cloud platforms, and digital economy enablement are governed by the Communications, Space and Technology Commission (CST) alongside the Ministry of Communications and Information Technology (MCIT). Additionally, global research collaboration and international ethical alignment are facilitated by the International Center for AI Research and Ethics (ICAIRE), a Category Two Center under the auspices of UNESCO headquartered in Riyadh.

| Entity | Primary Regulatory Jurisdiction | Core AI Ethics & Governance Mandate |
| --- | --- | --- |
| **Saudi Data and AI Authority (SDAIA)** | Central National Authority | Formulates national AI policies, issues ethics principles, operates governance platforms, and monitors entity compliance. |
| **National Data Management Office (NDMO)** | National Data Governance | Sets standards for data lifecycle management, data classification, and personal data protection enforcement. |
| **International Center for AI Research and Ethics (ICAIRE)** | Global Ethical Governance (UNESCO Cat 2) | Coordinates global ethics research, policy evaluation, and international framework alignment. |
| **National Cybersecurity Authority (NCA)** | Information Security & Cyber Resilience | Defines baseline cyber controls, threat mitigation, and system security standards for host infrastructure. |
| **Communications, Space & Technology Commission (CST)** | Telecom & Digital Infrastructure | Regulates cloud hosting providers, computing platforms, and digital service environments supporting AI workloads. |

## Scope of Application, Stakeholder Taxonomy, and Legal Definitions

The jurisdictional reach of the SDAIA AI Ethics Framework is universal across the Kingdom of Saudi Arabia, applying to all artificial intelligence stakeholders who design, develop, deploy, procure, operate, or are affected by AI systems. This scope encompasses public sector ministries and state agencies, private commercial enterprises, non-profit institutions, academic research organizations, third-party technology vendors, and individual consumers.

To operationalize governance accountability, the framework establishes a precise taxonomy of roles across the system lifecycle. The Responsible AI Officer is tasked with coordinating pre-deployment ethics reviews, validating control implementation across all ethical dimensions, managing exception handling, and escalating unresolved compliance risks to executive leadership. Objective pre- and post-conformity evaluations, algorithmic performance audits, and technical documentation verifications are conducted by the AI System Assessor. Within enterprise and public organizations, the Chief Data Officer (CDO) oversees upstream data classification, data governance adherence, and alignment with NDMO standards. Ultimate legal, ethical, and operational responsibility for system outputs rests with the AI System Owner, while the technical design, model architecture, feature engineering, and algorithmic fairness optimization are executed by the AI System Developer and Designer. Interaction with active systems is restricted to Authorized Users who possess verified clearance, appropriate training, and role-based access.

Adherence to the framework requires strict compliance with statutory definitions set forth by SDAIA:

- **Personal Data:** Any data, regardless of source or form, that leads to the direct or indirect identification of a specific natural person, including names, identification numbers, geographical coordinates, physical addresses, financial details, or contact numbers.

- **Sensitive Personal Data:** Personal data revealing an individual's ethnic or tribal origin; religious, political, or intellectual beliefs; civil association memberships; criminal and security records; biometric identifiers used for verification; genetic code; health and medical conditions; location tracking; or status as an individual of unknown parentage.

- **External Parties:** Any natural or legal person, whether public or private, operating outside the primary user, operator, developer, or assessor entities of an AI system.

- **AI System Lifecycle:** The iterative development process encompassing target definition, data collection, feature engineering, model training, validation, deployment, continuous monitoring, and retirement.

## Four-Tier Risk Classification Engine

SDAIA utilizes a risk-based model to calibrate regulatory oversight. The framework categorizes artificial intelligence applications into four distinct risk tiers based on their potential impact on individual safety, fundamental rights, economic stability, public health, and national security. The compliance burden, audit frequency, and administrative controls required for any given system are directly dictated by its assigned risk level.

### Unacceptable Risk Tier

AI systems assigned to this tier are deemed to pose existential or unacceptable threats to human safety, psychological well-being, individual liberty, and social order. Development, commercialization, or deployment of these systems within the Kingdom is strictly prohibited. Prohibited applications include systems utilizing subliminal behavioral manipulation or psychological conditioning designed to induce physical or economic harm; automated intrusive social scoring and socio-economic profiling by public or private entities; and tools engineered to systematically exploit the cognitive or physical vulnerabilities of specific demographic groups, such as children, the elderly, or disabled individuals.

### High Risk Tier

High-risk AI systems comprise applications operating in sensitive domains where algorithmic errors or autonomous decisions directly impact individual civil rights, legal standing, health outcomes, socio-economic access, or critical public infrastructure. Subject domains include biometric identification, healthcare diagnostics, credit scoring, recruitment and employment filtering, educational admissions, judicial sentence recommendation, law enforcement analysis, and industrial infrastructure management.

Compliance for high-risk systems is mandatory and strictly monitored. Systems must undergo mandatory pre-deployment and post-deployment conformity assessments conducted by certified assessors, alongside detailed Privacy Impact Assessments (PIA) and Human Rights Impact Assessments. Furthermore, high-risk systems must incorporate explicit Human-in-the-Loop (HITL) or Human-on-the-Loop (HOTL) control mechanisms to allow manual override, maintain continuous audit logging, and submit regular compliance reports to SDAIA.

### Limited Risk Tier

Limited-risk systems present specific transparency and informational risks, primarily associated with impersonation, automated interaction, or synthetic media generation. Examples include conversational agents (chatbots), generative synthetic media tools (deepfakes, AI image generators), and automated emotion recognition platforms. Compliance requirements for this tier center on mandatory user notification: individuals must be explicitly informed when interacting with an AI system or consuming synthetic media, and outputs must incorporate digital watermarking.

### Little or No Risk Tier

Systems in this tier present minimal or negligible threats to human rights, physical safety, or organizational security. Examples include email spam filtering, inventory optimization algorithms, spellcheckers, and AI-enabled video games. Entities deploying little-or-no-risk applications are exempt from mandatory regulatory filings, though SDAIA recommends voluntary adherence to general ethics principles to maintain organizational governance hygiene.

| Risk Tier | Hazard Level | Regulatory Status | Mandated Governance Controls | Representative System Examples |
| --- | --- | --- | --- | --- |
| **Unacceptable Risk** | Severe / Existential | Prohibited | Immediate ban, system shutdown, legal prosecution. | Social scoring, subliminal behavioral manipulation, child exploitation tools. |
|   | **High Risk** | Substantial / Critical | Permitted with Strict Supervision | Pre/post conformity audits, mandatory human oversight, continuous logging, PIA filings. |
| **Limited Risk** | Moderate / Informational | Permitted with Mandatory Transparency | User notification, synthetic content disclosure, digital watermarking, bias checks. | Customer service chatbots, generative synthetic text/images, emotion classification. |
| **Little or No Risk** | Minimal / Negligible | Unrestricted | Voluntary adoption of ethics guidelines, general security hygiene. | Email spam filtering, smart spellcheckers, route optimization, AI video games. |

## Seven Core Ethical Principles and Lifecycle Mapping

SDAIA establishes seven foundational ethical principles that govern all artificial intelligence initiatives within the Kingdom. To bridge policy intent with software engineering practice, SDAIA explicitly maps each ethical dimension across the four standardized phases of the AI System Lifecycle: **Plan and Design**, **Prepare Input Data**, **Build and Validate**, and **Deploy and Monitor**.

### Principle 1: Fairness

The Fairness principle mandates the systematic elimination of unjust bias, arbitrary discrimination, or social stigmatization across all stages of system development and deployment. AI models must deliver equitable, non-discriminatory, and representative outcomes regardless of gender, race, ethnicity, age, disability, or socio-economic status. During Plan and Design, teams must execute collaborative impact assessments to identify vulnerable demographic groups and adopt fairness-aware architectural designs. During Prepare Input Data, datasets must be audited for historical bias, proxy variables, and historical under-representation, ensuring correlation fallacies are eliminated. During Build and Validate, developers must test models against formal mathematical fairness metrics, such as demographic parity and equalized odds. During Deploy and Monitor, live production outputs must be continuously monitored against fairness thresholds, triggering automated retraining if model drift introduces bias.

### Principle 2: Privacy and Security

This principle enforces data confidentiality, infrastructure security, and strict compliance with the Personal Data Protection Law (PDPL) and National Cybersecurity Authority (NCA) baselines. In Plan and Design, architectures must embed Privacy and Security by Design, limiting data intake strictly to functionally necessary parameters and integrating formal data classification schemes (Public, Restricted, Confidential, Top Secret). In Prepare Input Data, personal and sensitive information must undergo robust de-identification, anonymization, or pseudonymization, alongside valid consent verification. In Build and Validate, models must be hardened against adversarial threats, including prompt injection, data poisoning, evasion attacks, and model inversion. In Deploy and Monitor, systems require continuous vulnerability scanning, TLS 1.3 transport encryption, secure key rotation, and automated privacy impact monitoring.

### Principle 3: Humanity

The Humanity principle establishes that artificial intelligence must remain human-centric, safeguarding intrinsic human dignity, human rights, personal autonomy, and national cultural values. Systems must empower and augment human capabilities rather than manipulate, deceive, or usurp human agency. In Plan and Design, system specifications must establish explicit human oversight channels and guard against automation bias or overreliance. In Prepare Input Data, input variables must be screened to ensure alignment with national ethics and religious values. In Build and Validate, predictive logic must be constrained to prevent deceptive behavioral nudging or coercive optimization. In Deploy and Monitor, operational workflows must provide accessible appeal routes, allowing individuals to contest automated decisions and obtain manual human review.

### Principle 4: Social and Environmental Benefits

AI applications must generate positive social value, contribute to sustainable economic growth, and minimize environmental degradation, such as high energy compute footprints. In Plan and Design, project charters must articulate defined socio-economic benefits and evaluate computational energy budgets. In Prepare Input Data, data sourcing must prioritize sustainability metrics and broad demographic representation. In Build and Validate, model training must optimize the trade-off between predictive accuracy and compute efficiency, favoring resource-efficient model architectures. In Deploy and Monitor, periodic post-deployment audits must evaluate real-world socio-economic impact alongside environmental resource consumption.

### Principle 5: Reliability and Safety

AI systems must operate predictably, robustly, and safely under normal, marginal, and hostile operating conditions, conforming consistently to technical specifications. In Plan and Design, engineers must define fail-safe recovery protocols, operational boundaries, and hazard mitigation controls. In Prepare Input Data, input validation pipelines must verify data quality, completeness, noise ratios, and out-of-distribution coverage. In Build and Validate, models must undergo stress testing, edge-case simulation, and safety boundary validation within isolated sandbox environments. In Deploy and Monitor, real-time telemetry must monitor performance metrics, detect operational anomalies, and maintain emergency kill-switch capabilities.

### Principle 6: Transparency and Explainability

Transparency requires clear public disclosure regarding AI system capabilities, limitations, and operational deployment, while Explainability demands that automated decision logic be interpretable to human operators and affected individuals. In Plan and Design, technical teams must select model architectures that support interpretability levels aligned with the system's risk tier. In Prepare Input Data, data lineage, metadata provenance, and curation processes must be fully documented. In Build and Validate, developers must deploy Explainable AI (XAI) frameworks (e.g., SHAP, LIME, feature attribution maps) to render model decision boundaries human-understandable. In Deploy and Monitor, user interfaces must explicitly disclose AI presence and deliver plain-language explanations whenever automated decisions affect individual rights or public services.

### Principle 7: Accountability and Responsibility

This principle establishes legal liability and operational accountability, requiring named individuals and organizational entities to retain responsibility for system behavior and outputs. In Plan and Design, organizations must formally assign governance roles (Responsible AI Officer, System Owner, Assessor) and document escalation hierarchies. In Prepare Input Data, chain-of-custody logs and legal data authorization records must be secured. In Build and Validate, technical documentation, model cards, and immutable versioning records must be generated. In Deploy and Monitor, incident response protocols, remediation channels, and liability tracking systems must remain active.

| Ethical Principle | Plan and Design Phase | Prepare Input Data Phase | Build and Validate Phase | Deploy and Monitor Phase |
| --- | --- | --- | --- | --- |
| **1. Fairness** | Multi-disciplinary bias risk scoping; inclusive goal setting. | Cleansing data of bias; proxy feature identification. | Mathematical fairness testing; demographic parity checks. | Real-time output fairness tracking; re-training triggers. |
| **2. Privacy & Security** | Privacy-by-Design architecture; data classification. | Sensitive data de-identification; anonymization. | Adversarial vulnerability testing; model hardening. | TLS 1.3 encryption; continuous vulnerability scans. |
| **3. Humanity** | Human oversight planning; avoidance of overreliance. | Cultural value alignment; rights impact screening. | Deceptive behavioral nudge elimination. | Human override channels; decision appeal processing. |
| **4. Social & Env. Benefits** | Social ROI definition; energy compute budget planning. | Sustainability data curation; broad socio-demographic representation. | Compute-efficient model architecture optimization. | Environmental carbon tracking; socio-economic reviews. |
| **5. Reliability & Safety** | Fail-safe operational boundary specification. | Out-of-distribution detection; data quality validation. | Stress testing; sandbox edge-case simulation. | Real-time telemetry monitoring; kill-switch activation. |
| **6. Transparency & Explainability** | Interpretability architecture selection. | Provenance metadata logging; data lineage tracking. | Integration of XAI tools (SHAP, LIME). | Automated AI disclosures; plain-language logic explanations. |
|   | **7. Accountability & Responsibility** | Formal role assignment (Responsible AI Officer). | Legal data authority verification; chain-of-custody tracking. | Complete documentation build; immutable versioning. |

## Specialized Regulatory Extensions and Domain Guidelines

SDAIA has issued specialized regulatory extensions targeting generative artificial intelligence (GenAI) and enterprise risk management to address domain-specific challenges.

### Generative AI Guidelines for Government Entities

Public sector organizations deploying GenAI tools must abide by administrative directives codified in SDAIA’s official government guide. Government personnel are strictly prohibited from entering, processing, or training public or commercial GenAI models with data classified as Restricted, Confidential, or Top Secret under NDMO standards. Only data categorized as Public may be processed. Furthermore, government entities are barred from utilizing GenAI tools for autonomous decision-making in critical processes that affect individual rights, citizenship, welfare entitlements, or vital national interests; all administrative outputs must undergo manual human review and sign-off. Public employees are also required to proofread and validate all GenAI-generated content, code, or analytical reports for factual accuracy and bias prior to official release.

### Generative AI Guidelines for Public and Private Sectors

For commercial vendors, developers, and citizens interacting with GenAI solutions, SDAIA enforces operational guardrails designed to preserve information integrity. Developers must embed digital watermarks and structural metadata tags into AI-generated synthetic media (image, video, audio, text) to prevent deception and deepfake proliferation. Conversational platforms must explicitly inform users at the start of an interaction that they are communicating with an automated system. Additionally, developers utilizing GenAI for code generation must implement automated security validation pipelines to detect structural vulnerabilities and verify software quality.

### National AI Risk Management Framework

SDAIA’s National AI Risk Management Framework equips entities with an enterprise methodology to manage AI risks across four continuous phases. Risk Identification involves scoping technical, algorithmic, operational, legal, and reputational risks across the system lifecycle. Risk Assessment evaluates likelihood and severity, mapping systems to SDAIA’s Risk Classification Engine. Risk Treatment implements technical guardrails, bias mitigation, and architectural adjustments. Risk Monitoring maintains operational audit logging to track performance degradation, model drift, and security vulnerabilities.

| Regulatory Domain | Core Prohibition or Guardrail | Enforced Technical / Administrative Action | Applicable Stakeholders |
| --- | --- | --- | --- |
| **Government Data Protection** | Entry of classified data into GenAI tools. | Enforcement of data filtering; restriction to Public-classified data assets. | All public sector employees and government contractors. |
| **Critical Decision Making** | Autonomous AI execution of rights-affecting decisions. | Mandatory Human-in-the-Loop review and signature. | Public agencies, healthcare providers, financial institutions. |
|   | **Synthetic Media & Deepfakes** | Unlabeled distribution of AI-generated content. | Imprinting visible disclosures and invisible digital watermarks. |
| **Algorithmic Security** | Deployment of vulnerable AI software code. | Automated SAST/DAST testing, code provenance annotation. | Software engineering teams, enterprise developers. |

## Implementation Tools, Audit Instruments, and Compliance Mechanisms

SDAIA operationalizes compliance monitoring through software instruments, evaluation tools, and accreditation mechanisms administered via the National Data Governance Platform (NDGP).

### AI Ethics Self-Assessment Tool

Hosted on the NDGP, the AI Ethics Self-Assessment Tool enables entities to evaluate their systems against SDAIA standards through a four-stage process. In the Discover stage, entities measure current compliance levels across all seven principles. In the Learn stage, specific governance gaps, unmitigated risks, and technical weaknesses are identified. In the Improve stage, organizations execute technical fixes, bias reduction protocols, and documentation updates. In the Reassess stage, updated system states are evaluated to verify ethical maturity prior to deployment.

### Market Governance Tools and Accreditation Certificates

To foster market trust and ensure product reliability, SDAIA operates official accreditation channels:

- **AI Ethics Incentive Badges:** Optional digital classifications awarded to organizations demonstrating compliance with SDAIA ethics principles. Badges are issued following NDGP survey submission and review by a specialized SDAIA committee, remaining valid for one year subject to annual re-evaluation.

- **AI Service Provider Accreditation Certificates:** Formal credentials issued to qualified commercial vendors. The registration process requires entities to register on the NDGP, designate an official AI Officer, submit technical product questionnaires, and upload verification evidence for committee audit prior to certificate issuance.

### Official Framework Annexures and Audit Checklist System

SDAIA’s framework incorporates formal annexures to standardize pre-deployment reviews. Annexure A details practical tools, including the *AI Fairness Position Statement* (documenting fairness criteria in plain language) and the *AI Methods Explanation Report* (explaining model logic and interpretability features). Annexure B maps ethical tools across lifecycle phases. Annexure C provides an itemized audit checklist utilizing specific compliance codes (e.g., PID.1 to PID.14) to evaluate technical criteria.

| Audit Code | Lifecycle Phase | Principle Alignment | Technical Compliance Question / Assessment Criterion | Third-Party Binding Status |
| --- | --- | --- | --- | --- |
| **PID.1** | Prepare Input Data | Privacy & Security | Is there an established mechanism that flags issues related to personal data privacy, protection, or unlawful processing? | Binding |
| **PID.11** | Prepare Input Data | Humanity | Have the input data and AI models been validated to ensure respect for fundamental human rights, values, and cultural preferences of KSA? | Binding |
| **PID.12** | Prepare Input Data | Humanity | Has diversity and demographic inclusion of the dataset been formally audited to prevent systematic disadvantage to minority groups? | Binding |
| **PID.13** | Prepare Input Data | Social & Environmental Benefits | Has the quality, accuracy, relevance, and source integrity of acquired data been formally evaluated and updated? | Binding |
| **PID.14** | Prepare Input Data | Reliability & Safety | Has the data architecture been categorized according to official SDAIA data classification guidelines? | Binding |

## Vector Database Architecture and RAG Ingestion Guidelines

To enable automated compliance auditing, policy gap detection, and real-time governance checks within AI systems (such as Retrieval-Augmented Generation or RAG pipelines), the SDAIA AI Ethics Principles must be transformed into structured, machine-readable vector database assets.

### Alignment with ITU-T Y.3172 Standardization Architecture

Automated regulatory auditing tools must map data execution flows across the seven logical nodes of the ITU-T Y.3172 machine learning framework. The Source (SRC) node captures incoming software code, prompt templates, or regulatory queries. The Collector (C) node gathers input data via APIs or gateway brokers. The Preprocessor (PP) node cleanses text, generates semantic embeddings, and enriches metadata payload tags. The Model (M) node executes foundation LLM or classification tasks to analyze compliance gaps. The Policy (P) node applies deterministic SDAIA regulatory guardrails to validate outputs. The Distributor (D) node routes audit findings and cited references. Finally, the Sink (SINK) node renders interactive compliance reports within developer consoles or administrative dashboards.

### Chunking Strategy and Metadata Payload Schema

Vector database collections (e.g., PostgreSQL pgvector, Qdrant, Pinecone) storing SDAIA ethics data should employ hierarchical parent-child chunking. Parent chunks encapsulate complete principles (~1,000 tokens), while child chunks encapsulate granular rules and audit checklist items (~200 tokens). Embedding generation should target standard 1536-dimensional vector spaces. Each vector entry must incorporate a structured JSON metadata payload to support hybrid vector-keyword retrieval:

`{
  "document_id": "SDAIA-P114E",
  "authority": "SDAIA",
  "framework": "AI Ethics Principles",
  "principle_id": "P1",
  "principle_name": "Fairness",
  "lifecycle_phase": "Plan_and_Design",
  "risk_tier_relevance": ["High", "Limited"],
  "audit_code": "PID.12",
  "third_party_binding": true,
  "source_url": "https://sdaia.gov.sa/en/SDAIA/about/Documents/ai-principles.pdf"
}`

### System Prompt for Automated Policy Gap Auditing

When configuring RAG agents to evaluate codebases, system prompts, or corporate policies against SDAIA standards, the following prompt configuration ensures precise compliance extraction:

System Prompt: SDAIA AI Ethics Compliance & Policy Gap Analyzer

You are an expert regulatory compliance auditor specialized in Saudi Data and AI Authority (SDAIA) regulations, Saudi Personal Data Protection Law (PDPL), and ITU-T Y.3172 standards.

Your task is to perform an exhaustive policy gap analysis on the provided Target Document / Codebase Context against the official SDAIA AI Ethics Principles (Document SDAIA-P114E).

Audit Instructions:

1. Evaluate the context across all Seven SDAIA Ethical Principles: Fairness, Privacy & Security, Humanity, Social & Environmental Benefits, Reliability & Safety, Transparency & Explainability, and Accountability & Responsibility.

1. Classify the Target System's Risk Tier (Unacceptable, High, Limited, Little/No Risk).

1. Identify all specific Policy Gaps, missing safeguards, unmitigated algorithmic risks, and data classification violations.

1. For every gap identified, cite the exact SDAIA Principle, Lifecycle Phase, and Audit Code (e.g., PID.1 to PID.14).

1. Output structured findings formatted with precise compliance scores and actionable engineering remediation steps.

| ITU-T Y.3172 Node | RAG Technical Realization | SDAIA Regulatory Function | Vector Database Implementation |
| --- | --- | --- | --- |
| **Source (SRC)** | Target codebase, prompt configurations, data schema files. | Input data asset requiring ethical audit. | File ingestion stream, git repository parser. |
| **Collector (C)** | REST API / Supabase Edge Function gateway. | Ingestion of system metadata and audit requests. | Incoming payload broker and queue. |
| **Preprocessor (PP)** | Tokenizer, semantic chunker, embedding generator. | Formatting compliance context for vector search. | pgvector HNSW index generator, cosine distance calculations (<=>). |
| **Model (M)** | Large Language Model (e.g., Gemini 2.5 Flash, GPT-4o). | Executing semantic reasoning and policy evaluation. | Semantic match execution against vectorized SDAIA corpus. |
| **Policy (P)** | Rule engine enforcing SDAIA Ethics Guardrails. | Verifying adherence to Unacceptable/High risk rules. | Deterministic rule filter overriding LLM outputs if violations occur. |
| **Distributor (D)** | Payload formatter and citation linker. | Structuring audit results with reference URLs. | JSON serializer attaching source metadata tags. |
| **Sink (SINK)** | Compliance dashboard, developer IDE extension. | Presenting gap reports and accreditation status. | React / Web interface rendering interactive audit reports. |

## Strategic Conclusions and Regulatory Outlook

The Saudi Data and AI Authority’s AI Ethics Principles and Framework establishes a codified regulatory mechanism that transitions ethical AI from voluntary guidelines into enforceable engineering and operational controls. Anchored legally in Council of Ministers Resolution No. (292), SDAIA’s governance framework directly shapes market access, public procurement, cloud architecture, and enterprise software engineering across Saudi Arabia.

Analysis highlights three strategic imperatives governing the future of AI in the Kingdom:

First, ethical compliance functions as a fundamental market-access requirement. Public sector agencies and enterprise buyers increasingly require verified alignment with SDAIA ethics principles, NDMO data classification standards, and PDPL rules prior to commercial onboarding. Second, embedding controls across all four lifecycle phases ensures that risk mitigation is integrated natively into software engineering pipelines rather than applied reactively after deployment. Third, the alignment of SDAIA principles with international benchmarks (such as UNESCO guidelines and ITU-T Y.3172 standards) ensures that systems built within Saudi Arabia maintain global technical and regulatory interoperability.

By leveraging tools such as the National Data Governance Platform, the AI Ethics Self-Assessment Tool, Incentive Badges, and Accreditation Certificates, organizations can systematically verify their compliance posture. Adopting these controls enables entities to mitigate algorithmic risks, safeguard personal data privacy, ensure operational reliability, and support the broader objectives of Saudi Vision 2030.

#### Works cited

1. أﺧﻼﻗﻴﺎت  اﻟﺬﻛﺎء  اﻻﺻﻄﻨﺎﻋﻲ, https://sdaia.gov.sa/ar/SDAIA/about/Documents/ai-principles.pdf

2. Saudi  AI  ethics  principles: SDAIA  framework, governance  requirements, and  business  implications, https://vision2030.ai/regulation/ai-ethics-principles-saudi-arabia/

3. AI  Ethics  Principles - September 2023, https://dgp.sdaia.gov.sa/wps/wcm/connect/4c56ed1c-1b82-447d-ac29-638f5f99c12e/ai-principles-EN.pdf?CACHEID=ROOTWORKSPACE-4c56ed1c-1b82-447d-ac29-638f5f99c12e-p3k51U9&CONVERT_TO=url&MOD=AJPERES

4. AI  Ethics  Principles, https://sdaia.gov.sa/en/SDAIA/about/Documents/ai-principles.pdf

5. Pre-Deployment  Review  Using  SDAIA  AI  Ethics  Principles | Ting, https://www.tingsaudi.com/blog/pre-deployment-review-sdaia-ai-ethics

6. AI  Ethics  Principles | Digital  Government  Authority, https://dga.gov.sa/en/AI-Ethics-Principles

7. SDAIA  Publications, https://sdaia.gov.sa/en/MediaCenter/KnowledgeCenter/Pages/SDAIAPublications.aspx

8. Guidelines - Generative  Artificial  Intelligence - for  Government, https://sdaia.gov.sa/en/SDAIA/about/Files/GenAIGuidelinesForGovernmentENCompressed.pdf

9. Guidelines - Generative  Artificial  Intelligence  for  Public, https://sdaia.gov.sa/en/SDAIA/about/Files/GenerativeAIPublicEN.pdf

10. AI  Ethics & Principles | PDF - Scribd, https://www.scribd.com/document/1058656477/AI-Ethics-Principles

11. The  Rise  of  AI  in  Saudi  Arabia: Importance  and  Regulatory  Framework - BSA  LAW, https://bsalaw.com/insight/the-rise-of-ai-in-saudi-arabia-importance-and-regulatory-framework/

12. AI  Ethics  Assessment, https://dgp.sdaia.gov.sa/wps/portal/pdp/services/servicesdetails/AIEthicsAssessment/!ut/p/z1/04_Sj9CPykssy0xPLMnMz0vMAfIjo8ziPR1dzTwMgw2MDMOcTA3MjH39TE29jY0MnI30w9EUhIZZAhUEGvl6OXoaGwQY60cRo98AB3A0IKTfi5ACoA-MinydfdP1owoSSzJ0M_PS8vUjHD1dSzIyk4sdi4tTi4tzU_NKgC6JwmuWhRGGAkzPghXg8U1wYpF-QW5oRJVPWrCnrqMiAAIPg5Q!/dz/d5/L0lHSkovd0RNQU5rQUVnQSEhLzROVkUvZW4!/

13. AI  Market  Regulation  Tools, https://sdaia.gov.sa/en/MediaCenter/KnowledgeCenter/ResearchLibrary/AIMarketGovernanceTools.pdf

14. AI  Ethics  Principles  Framework 2025 | PDF | Artificial  Intelligence, https://www.scribd.com/document/950666762/Ai-Principles

15. Beijing  AI  Principles, https://www.linking-ai-principles.org/principles

16. Global  AI  Summit, https://sdaia.gov.sa/en/MediaCenter/KnowledgeCenter/ResearchLibrary/GAIN.pdf

17. ITU-AI-Readiness-26, uploaded:ITU-AI-Readiness-26

---

# الجزء الثاني: نظام حماية البيانات الشخصية السعودي ولائحته التنفيذية (Saudi PDPL)

# Saudi Personal Data Protection Law (PDPL): Comprehensive Legal Analysis and Regulatory Compliance Framework

## Legislative Foundations and Regulatory Governance

The Kingdom of Saudi Arabia established its baseline statutory data privacy framework through the Personal Data Protection Law (PDPL), promulgated under Royal Decree No. M/19 on 16 September 2021 (corresponding to 9 Safar 1443H), and subsequently amended via Royal Decree No. M/148 on 27 March 2023 (corresponding to 5 Ramadan 1444H). The PDPL represents a core pillar of Saudi Arabia’s National Data Strategy and Vision 2030 digital economy initiatives, designed to safeguard individual privacy rights, govern cross-border data flows, codify national digital sovereignty, and establish binding data governance obligations across both public and private sectors.

The law officially entered into force on 14 September 2023 pursuant to Cabinet Decision No. 98. To enable commercial enterprises and public entities to adjust their technical infrastructure, operational workflows, and contractual arrangements, a one-year regulatory transition period was enacted, rendering the PDPL fully enforceable across all jurisdictions on 14 September 2024. Executive oversight and regulatory administration are spearheaded by the Saudi Data and Artificial Intelligence Authority (SDAIA). During the initial implementation era, supervisory oversight and executive policy execution are managed through SDAIA's regulatory arm, the National Data Management Office (NDMO), which maintains responsibility for issuing implementing regulations, enforcing compliance guidelines, and maintaining the central National Data Governance Platform.

The territorial scope of the PDPL combines traditional domestic applicability with extraterritorial jurisdiction. Domestically, the law applies to any processing of personal data occurring within the geographical boundaries of the Kingdom, whether conducted through automated digital systems or manual physical filing structures. Extraterritorially, the statutory provisions bind any data controller or processor located outside Saudi Arabia that processes the personal data of individuals residing within the Kingdom. The law explicitly excludes from its scope personal data processed by natural persons strictly for personal or family activities, provided such processing remains within private social circles and the data is neither published nor disclosed to the broader public, commercial markets, or non-profit entities.

| Regulatory Parameter | Statutory Specification | Legal Reference |
| --- | --- | --- |
| Primary Legislation | Royal Decree No. M/19 (Amended by Royal Decree No. M/148) | PDPL Art. 1 |
| Lead Supervisory Regulator | Saudi Data and Artificial Intelligence Authority (SDAIA) / NDMO | PDPL Art. 30; Reg. Art. 1 |
| Statutory Effective Date | 14 September 2023 | Cabinet Decision No. 98 |
| Full Operational Enforcement | 14 September 2024 | SDAIA Regulatory Mandate |
| Jurisdiction & Territorial Scope | In-Kingdom processing and Extraterritorial handling of KSA residents' data | PDPL Art. 2(1) |
| Statutory Exclusions | Purely personal or household processing within private social circles | PDPL Art. 2(2); Reg. Art. 2 |

## Key Definitions and Data Classification Hierarchy

The PDPL establishes a clear terminology framework designed to delineate the precise operational boundaries of data processing workflows. Personal Data is defined as any information, regardless of its source, media, or format, that leads to the direct or indirect identification of a specific living natural person. This encompasses identifiers such as full names, civil registration numbers, physical addresses, electronic contact details, official license numbers, bank account numbers, credit card details, static or dynamic IP addresses, biometric signatures, photographs, and video recordings.

Sensitive Personal Data represents a critical sub-category requiring elevated technical safeguards, strict lawful processing grounds, and mandatory impact assessments. Under statutory definitions, sensitive data includes genetic data, biometric identifiers processed for unique identification, health and clinical records, credit and financial capability data, records revealing ethnic or tribal origin, religious, political, or intellectual beliefs, memberships in non-governmental organizations, and criminal or security records. Furthermore, the PDPL extends statutory privacy protections to the data of deceased individuals if disclosure would identify the deceased or cause moral or material damage to surviving family members.

To standardize operational security across public agencies, enterprise systems, and educational networks, SDAIA established a unified national Data Classification Model. Organizations must audit, tag, and segment all stored and transit data against this four-tier structure to enforce proportionate encryption, access controls, and retention rules.

| Classification Tier | Target Information Scope | Mandatory Protection Controls |
| --- | --- | --- |
| Tier 1: Public Data | Information explicitly cleared for unrestricted public dissemination. | Minimal baseline security; public disclosure tracking. |
| Tier 2: Internal Data | Non-confidential operational information restricted to internal organization use. | Standard Role-Based Access Control (RBAC) and perimeter security. |
| Tier 3: Confidential Data | Standard personal data, financial records, employee files, and commercial contracts. | AES-256 encryption at rest, TLS 1.3 in transit, strict RBAC, and RoPA tracking. |
| Tier 4: Highly Confidential / Sensitive Data | Sensitive personal data, biometrics, health records, genetic data, and minor data. | Enhanced encryption, mandatory DPIA, explicit consent logs, isolated storage, and DPO oversight. |

## Primary Legal Principles and Lawful Bases for Processing

Data processing under the PDPL must adhere to fundamental legal principles: lawfulness, fairness, and transparency; purpose limitation; data minimization; accuracy and timeliness; storage limitation; and organizational security and accountability. Data Controllers must ensure that every collection, storage, utilization, or disclosure activity is anchored to an explicit, documented, and legally recognized processing ground.

Under the statutory framework, processing without a valid legal basis is explicitly prohibited. The selection of a lawful basis must occur prior to data collection and must be formally documented within the organization's Record of Processing Activities (RoPA).

```text
`Valid Lawful Processing Framework
                 
        +-------------------------------------------------+
        |  Valid Lawful Basis Required for Processing     |
        +------------------------+------------------------+
                                 |
     +-------------------+-------+------------+-------------------+
     |                   |                    |                   |
     v                   v                    v                   v
 Explicit            Contractual          Statutory /         Legitimate
 Consent             Necessity          Public Obligation      Interest
     |                   |                    |                   |
     v                   v                    v                   v
[Opt-in Log]   [Direct Contract Exec]   [Public Entity / Law]   [Requires LIA]`
```

### Acceptable Lawful Bases under Saudi PDPL

- **Explicit Data Subject Consent**: Consent serves as the default processing ground across standard B2C interactions unless a specific statutory exemption applies. Valid consent must be freely given, explicit, informed, and unambiguous, captured through affirmative opt-in mechanisms such as signed electronic forms, verified application settings, or written declarations. Consent must never be bundled or made a compulsory prerequisite for accessing a service unless the processing is strictly necessary to deliver that specific service. Furthermore, written consent is legally mandatory whenever handling Sensitive Personal Data.

- **Contractual Necessity**: Data processing is lawful without separate consent when strictly required to perform a contract to which the Data Subject is a party, or to execute pre-contractual measures requested directly by the individual.

- **Statutory Obligation and Public Interest**: Public entities and authorized private bodies may process personal data without consent when fulfilling statutory duties, protecting national security, executing judicial orders, or managing public health emergencies.

- **Vital or Actual Interest**: Processing is permitted to safeguard the vital interests of a Data Subject (such as emergency medical intervention to prevent loss of life or severe bodily injury) where obtaining prior consent is physically or legally impossible. Actual interest applies to moral or material interests directly linked to the Data Subject where contacting them is impractical.

- **Legitimate Interest of the Controller**: Controllers may process standard personal data based on legitimate interest, provided that a documented Legitimate Interest Assessment (LIA) proves that the controller's interest does not override the fundamental rights, privacy, or freedoms of the Data Subject. Legitimate interest is strictly prohibited as a legal basis for processing Sensitive Personal Data or for conducting direct commercial marketing and automated behavioral profiling.

- **Scientific, Historical, or Statistical Research**: Processing for research purposes is authorized if the personal data is fully anonymized or if specific statutory safeguards prevent individual re-identification.

| Lawful Basis | Operational Applicability | Exclusions & Statutory Restrictions |
| --- | --- | --- |
| Explicit Consent | Direct customer interactions, optional features, commercial marketing, web analytics. | Cannot be forced or bundled as a condition for unrelated core services. |
| Contractual Necessity | Account provisioning, subscription billing, order fulfillment, employee payroll. | Limited strictly to operations essential to deliver the specific contract. |
| Statutory Obligation | Tax reporting, anti-money laundering compliance, regulatory disclosures. | Applicable solely within the defined parameters of the statutory requirement. |
| Vital / Actual Interest | Emergency hospital admission, disaster response, critical health protection. | Restricted to life-safety scenarios where consent cannot be obtained. |
| Legitimate Interest | Network security monitoring, fraud prevention, internal operational optimization. | **Prohibited** for Sensitive Personal Data and Direct Marketing activities. |
| Scientific / Research | Academic studies, national census gathering, clinical trial analysis. | Requires complete anonymization; **prohibited** for commercial profiling. |

## Data Subject Rights and SLA Mandates

The PDPL establishes an enforceable portfolio of Data Subject Rights designed to grant individuals control over their digital footprint. Data Controllers are legally obligated to build technical infrastructure, verification protocols, and administrative workflows capable of receiving, evaluating, and executing Data Subject Access Requests (DSARs) within strict statutory timelines.

### Statutory Data Subject Rights

- **Right to be Informed**: Data Subjects must be explicitly informed of the legal justification, processing purpose, controller contact details, third-party disclosure channels, and data retention schedules prior to or at the moment of collection. Transparency must be maintained through a standalone Privacy Policy published in clear, accessible language.

- **Right of Access and Copy**: Data Subjects have the right to request formal confirmation of processing, inspect their held personal records, and obtain a copy of their personal data in a clear, structured, and machine-readable electronic format. Access rights must not infringe upon third-party intellectual property or trade secrets.

- **Right to Rectification and Completion**: Individuals may compel controllers to update, correct, or complete inaccurate, misleading, or obsolete personal data held within enterprise repositories.

- **Right to Erasure / Destruction**: Data Subjects maintain the right to compel the destruction or purging of their personal data if the data is no longer necessary for the original processing purpose, if consent has been revoked, or if the processing lacks a legal basis. Controllers must ensure erasure requests propagate to backup stores and downstream processors.

- **Right to Withdraw Consent**: Individuals may revoke previously granted processing consent at any time. Revocation procedures must be as simple, direct, and accessible as the initial consent capture workflow.

- **Right to Object to Direct Marketing and Profiling**: Data Subjects maintain an absolute right to opt out of commercial communications, promotional materials, and automated profiling that produces legal or significant personal effects.

### Service Level Agreements and Execution Framework

Data Controllers must respond to and execute DSARs without undue delay and within a maximum statutory window of **30 calendar days** from initial receipt. This SLA may be extended by an additional **30 calendar days** if request execution requires disproportionate operational effort or if the controller receives multiple complex requests from the same applicant. In cases requiring an extension, the controller must formally notify the Data Subject within the initial 30-day window detailing the specific technical or logistical reasons for the delay.

Before executing any DSAR, controllers must verify the identity of the applicant using secure authentication mechanisms. Controllers may refuse to fulfill a request if it is manifestly unfounded, repetitive, or requires unreasonable effort, provided the refusal rationale is formally documented and communicated to the applicant.

| Data Subject Right | Mandatory Organizational Action | Statutory SLA Window |
| --- | --- | --- |
| Right to be Informed | Publish accessible Privacy Policy at all collection points. | At or before time of collection. |
| Right of Access & Copy | Authenticate user, generate structured electronic data export file. | Max 30 days (+30 day extension). |
| Right to Rectification | Update production databases, issue correction notices to processors. | Max 30 days. |
| Right to Destruction | Purge active DBs, purge backup archives, issue purge commands to processors. | Max 30 days (+30 day extension). |
| Consent Revocation | Immediately cease processing, update consent flags across systems. | Immediate operational execution. |
| Marketing Objection | Suppress contact records from marketing lists, disable tracking pixels. | Immediate operational execution. |

## Cybersecurity Measures, Data Governance, and Incident Management

The PDPL mandates that entities processing personal data implement technical, administrative, and organizational safeguards to ensure confidentiality, integrity, and availability. Security controls must align with frameworks issued by the National Cybersecurity Authority (NCA) and SDAIA guidelines, incorporating AES-256 encryption for data at rest, TLS 1.3 protocol enforcement for data in transit, network segmentation, zero-trust identity architectures, RBAC access policies, and immutable audit logging.

### Personal Data Breach Notification Workflow

A Personal Data Breach is defined as any security incident leading to the unauthorized disclosure, destruction, alteration, loss, or access to personal data, whether through accidental means or intentional compromise.

When a breach incident is detected, the organization must activate an immediate response protocol governed by strict regulatory timelines. Within the first **72 hours** of becoming aware of the incident, the Data Controller must submit a formal incident notification to SDAIA via the National Data Governance Platform. The submission must detail the nature of the breach, affected data categories, estimated number of impacted individuals, potential adverse risks, immediate containment measures taken, and the contact details of the appointed Data Protection Officer (DPO).

Concurrently, the controller must evaluate the threat level to impacted Data Subjects. If the breach poses a high risk to the privacy, rights, or vital interests of affected individuals, the controller must notify those individuals directly without delay. The notification must be written in clear language, outlining the nature of the breach, potential consequences, and recommended actions the individual can take to protect themselves. If the breach is determined to pose minimal risk, direct individual notification may be waived, but the incident details, risk evaluation, and internal remediation actions must be documented within the organization's security audit logs.

```text
`Personal Data Breach Incident Protocol
                
       +-------------------------------------------------+
       |       Personal Data Breach Identified           |
       +------------------------+------------------------+
                                |
                                v
       +-------------------------------------------------+
       |   Assess Risk to Rights and Security of Subjects|
       +------------------------+------------------------+
                                |
           +--------------------+--------------------+
           |                                         |
           v                                         v
+-------------------------------+         +-------------------------------+
| Mandatory SDAIA Notification  |         | High Risk to Data Subjects?   |
|   Strict 72-Hour Timeline     |         +---------------+---------------+
+-------------------------------+                         |
                                            +-------------+-------------+
                                            |                           |
                                            v                           v
                                    +---------------+           +---------------+
                                    |  YES: Notify  |           |  NO: Document |
                                    |  Individuals  |           |  Internally   |
                                    |  Promptly     |           |  In Logs      |
                                    +---------------+           +---------------+`
```

### Governance, Registration, and Record-Keeping Directives

- **Data Protection Officer (DPO) Mandate**: Appointment of a DPO is legally required for: (a) Public Entities, (b) organizations whose core operations involve large-scale processing of Sensitive Personal Data, (c) entities conducting continuous tracking or automated profiling, and (d) institutions processing the data of children or legally incompetent individuals. The DPO may be an internal employee or an external vendor, and their details must be formally registered with SDAIA.

- **National Controller Register**: Data Controllers falling under statutory criteria (including public bodies, educational institutions, healthcare providers, and entities handling sensitive data) must register on SDAIA's National Data Governance Platform.

- **Record of Processing Activities (RoPA)**: Controllers must maintain a detailed RoPA documenting processing purposes, data categories, recipient disclosure lists, cross-border flows, security controls, and retention schedules. RoPA logs must be retained for at least **5 years** following the termination of processing operations.

- **Data Protection Impact Assessment (DPIA)**: Controllers must perform a formal DPIA prior to launching high-risk processing operations, deploying new automated technologies, or processing sensitive datasets at scale.

- **Cross-Border Data Transfer Framework**: Personal data collected within the Kingdom must primarily be stored and processed domestically to protect national data sovereignty. Cross-border transfers are prohibited unless the destination jurisdiction provides an adequate level of protection recognized by SDAIA, or the controller implements approved binding contractual clauses, enterprise privacy rules, or specific statutory exceptions. Transfers must always be restricted to the minimum necessary data.

## Enforcement Mechanisms, Penalty Structures, and Compliance Auditing

Enforcement of the PDPL is actively managed by SDAIA through specialized regulatory enforcement committees. The enforcement phase is fully operational, with committees actively issuing binding penalty decisions against public and private entities for violations such as processing without a legal basis, failure to implement technical safeguards, illegal cross-border transfers, and un-sanctioned direct marketing.

### Statutory Penalty Hierarchy

- **Administrative Fines**: Standard violations of the PDPL or its executive regulations incur administrative fines up to **SAR 5,000,000 (~$1.33 Million USD)** per violation. Fines may be doubled up to **SAR 10,000,000** for repeat or continuous offenses.

- **Criminal Sanctions and Imprisonment**: Unlawful disclosure, publishing, or transferring of Sensitive Personal Data in violation of the law—when committed with malicious intent to cause harm to an individual or achieve personal financial gain—carries criminal liability resulting in imprisonment for up to **2 years** and criminal fines up to **SAR 3,000,000 (~$800,000 USD)**.

- **Confiscation of Illicit Proceeds**: Judicial courts maintain the authority to order the confiscation of all revenues, profits, or assets generated through unlawful personal data processing operations.

- **Portal Response Windows**: Under regulatory platform rules, entities formally indicted via the National Data Governance Platform are subject to a strict **5-business-day** response window. Entities must pre-register certified Power of Attorney (POA) documentation and active regulatory point-of-contacts on the portal to avoid automatic default judgements.

| Non-Compliance Violation Category | Maximum Administrative Fine | Maximum Criminal Sanction |
| --- | --- | --- |
| Standard Statutory Non-Compliance (Lack of legal basis, failure to honor DSARs, missing RoPA) | Up to SAR 5,000,000 (~$1.33M USD) | Non-criminal administrative sanction. |
| Recurrent / Repeated Offenses (Duplicate non-compliance within statutory evaluation window) | Up to SAR 10,000,000 (~$2.66M USD) | Escalate to judicial referral. |
| Malicious Disclosure of Sensitive Data (Unauthorized release of health, biometric, or minor data for harm/gain) | Up to SAR 5,000,000 + Asset Confiscation | Up to **2 Years Imprisonment** + SAR 3,000,000 Fine. |
| Failure to Report Personal Data Breach (Exceeding 72-hour SDAIA notification mandate) | Up to SAR 5,000,000 | Administrative record sanction. |
| Unlawful Cross-Border Transfer (Bypassing residency or approval requirements) | Up to SAR 5,000,000 | Criminal review for national security breach. |

## Strategic Governance Roadmap for Enterprise and Healthcare Entities

Achieving and maintaining compliance with the Saudi Personal Data Protection Law requires an operational strategy that integrates legal oversight, technical architecture, and administrative procedures. Organizations operating within the Kingdom or processing the data of Saudi residents should execute the following implementation roadmap to mitigate legal exposure and ensure data privacy alignment.

### Phase 1: Data Discovery, Inventory, and Classification

Organizations must conduct a enterprise-wide Data Protection Impact Assessment (DPIA) and data mapping exercise. This involves identifying all personal data ingress points, internal processing stores, analytical tools, and external vendor connections. Every data asset must be categorized against SDAIA’s four-tier classification model, ensuring that Sensitive Personal Data and minor data are tagged for Tier 4 protection controls. The findings must be formalized within an official Record of Processing Activities (RoPA), which must be maintained and archived for a minimum retention window of five years.

### Phase 2: Lawful Basis Re-Engineering and Consent Architecture

Controllers must audit all existing data processing pipelines to confirm that every operation rests upon a valid legal basis. Where consent is relied upon, organizations must deploy explicit opt-in mechanics, eliminate pre-ticked checkboxes, and decouple consent agreements from general terms of service. For platforms processing minor data, age-verification gateways must be integrated to mandate parent/guardian opt-in for users under 13 years of age. Where processing relies on Contractual Necessity or Statutory Obligation, these justifications must be documented within user-facing Privacy Policies.

### Phase 3: Technical Safeguards and Incident Response Readiness

Engineering teams must implement technical controls to protect data throughout its lifecycle. This includes applying AES-256 encryption for data at rest, enforcing TLS 1.3 for data in transit, and restricting administrative access via granular Role-Based Access Controls (RBAC). Educational platforms must enforce local cloud hosting within Saudi Arabian data centers to comply with domestic data residency mandates. Furthermore, organizations must draft and test a Personal Data Breach Incident Response Plan configured to execute mandatory SDAIA notifications within the strict **72-hour** regulatory window.

### Phase 4: Institutional Registration and Portal Governance

Organizations falling under statutory registration criteria—including educational institutions, public entities, and controllers handling sensitive or minor data—must formally register on SDAIA’s National Data Governance Platform. Eligible entities must appoint a qualified Data Protection Officer (DPO) and submit their credentials to the regulator. Finally, corporate entities must register a certified Power of Attorney (POA) on the governance portal to ensure immediate access to regulatory notices and prevent default judgements within the 5-day inquiry window.

#### Works cited

1. Saudi  Personal  Data  Protection  Law  PDPL  Compliance  Guide - Hala  Privacy, https://halaprivacy.com/what-is-pdpl/

2. Data  protection  laws  in  Saudi  Arabia, https://www.dlapiperdataprotection.com/?c=SA

3. ! Public, https://sdaia.gov.sa/en/SDAIA/about/Documents/ImplementingRegulationPersonalDataProtectionLaw.pdf

4. Personal  Data  Protection  Law - Grant  Thornton  Saudi  Arabia, https://www.grantthornton.sa/globalassets/_markets_/sau/media/pdfs/gt-data-protection-article-new.pdf

5. SDAIA  and  Saudi  Personal  Data  Protection  Law (PDPL): What  Saudi  Organizations  Must  Know  in 2026 - SGC  Consulting, https://www.sgc.consulting/sdaia-saudi-personal-data-protection-law-pdpl-compliance-guide/

6. Saudi  Arabia | Jurisdictions - DataGuidance, https://www.dataguidance.com/jurisdictions/saudi-arabia?topic=notes

7. Kingdom  of  Saudi  Arabia  Personal  Data  Protection  Law  Series - part 1 - PwC, https://www.pwc.com/m1/en/blogs/pdf/ksa-personal-data-protection-law-series-part-1-.pdf

8. Data  Protection | Saudi  Data & AI  Authority, https://sdaia.gov.sa/en/Research/Pages/DataProtection.aspx

9. Data  Privacy  Q&A - Rouse, https://rouse.com/media/jtvpra4k/data-privacy-q-and-a-saudi-arabia.pdf

10. Personal  Data  Protection  Law, https://sdaia.gov.sa/en/SDAIA/about/Documents/Personal%20Data%20English%20V2-23April2023-%20Reviewed-.pdf

11. Executive  Regulations, https://sdaia.gov.sa/en/SDAIA/about/Documents/ExecutiveRegulations.pdf

12. The  Implementing  Regulation  of  the  Personal  Data  Protection  Law - Details, https://dgp.sdaia.gov.sa/wps/portal/pdp/knowledgecenter/details/PDPL2/%21ut/p/z1/04_Sj9CPykssy0xPLMnMz0vMAfIjo8ziPR1dzTwMgw2MDMOcTA3MjH39TE29jY0MQsz1w9EUhIZZAhUEGvl6OXoaGwQY60cRo98AB3A0IKTfi5ACoA-MinydfdP1owoSSzJ0M_PS8vUjAlwCfIyAlkfh1W5hjKEA039gBXg8UJAbGlHlkxbsma6oCAA-ytT9/dz/d5/L0lDUmlTUSEhL3dHa0FKRnNBLzROV3FpQSEhL2Vu/

13. Saudi  PDPL  Enforcement  News & Data  Privacy  Guidelines 2026 - Out2Sol  Global, https://out2sol.global/blog/saudi-pdpl-data-privacy-guidelines-and-enforcement-updates/

14. Developing  and  Elaboration  Guideline  Policy  Privacy, https://sdaia.gov.sa/Documents/PrivacyPolicyGuideline.pdf

15. Minimum  Personal  Data  Determination  Guideline - Details, https://dgp.sdaia.gov.sa/wps/portal/pdp/knowledgecenter/details/MinimumPersonalDataDeterminationGuideline/!ut/p/z1/jZBBDoIwEEXPwgFMSxtQlyhGQWswiGI3pokFJ6GFILjw9FaWEsHZTfJ-Zt5HHKWIa_GEXDRQalGY_cLda-Ct3I0dY2KfFg52Kds7zpYSfJyi8xeQnOYGOBAWegHFEUX8nzz-MR4ey4djgDEgNVuyHPFKNPcJ6KxEKQMNqlWRrB8fT180wpeNrBXoTn3dwk0WoKV5kA-emNEe0O-gAwYkK5Wkr10WB7llvQHjBZAe/dz/d5/L0lDUmlTUSEhL3dHa0FKRnNBLzROV3FpQSEhL2Vu/

16. PDPL: Saudi  Arabia's  Personal  Data  Protection  Law - Cookiebot, https://www.cookiebot.com/en/saudi-arabia-personal-data-protection-law-pdpl/

17. Privacy  Policy - The  British  International  School  of  Jeddah, https://www.bis-jeddah.com/privacy-policy

18. Children  and  Incompetents' Data  Protection  Policy, https://sdaia.gov.sa/ar/SDAIA/about/Documents/Children%20and%20Incompetents%E2%80%99%20Data%20Protection%20Policy.pdf

19. Saudi  Arabia  PDPL  Comments | CrowdStrike, https://www.crowdstrike.com/wp-content/uploads/2023/09/Saudi-Arabia-PDPL-Comments.pdf

20. Personal  Appointing  for  Rules  Officer  Protection  Data, https://sdaia.gov.sa/en/SDAIA/about/Documents/RulesforAppointingPersonalDataProtectionOfficer.pdf

21. Private  Universities  and  Schools  Urged  to  Register  on  SDAIA's  National  Data  Platform, https://www.spa.gov.sa/N2449120

22. Guide  to  the  Saudi  Personal  Data  Protection  Law  For  Controllers  and  Processors - Details, https://dgp.sdaia.gov.sa/wps/portal/pdp/knowledgecenter/details/PDPLCP/!ut/p/z1/04_Sj9CPykssy0xPLMnMz0vMAfIjo8ziPR1dzTwMgw2MDMOcTA3MjH39TE29jY0MQsz1w9EUhIZZAhUEGvl6OXoaGwQY60cRo98AB3A0IKTfi5ACoA-MinydfdP1owoSSzJ0M_PS8vUjAlwCfJwDgLZH4dVvYYyhANODYAV4fBCcWKRfkBsaUeWTFuyp66gIABC_KT0!/dz/d5/L0lHSkovd0RNQU5rQUVnQSEhLzROVkUvZW4!/

23. Guide  to  the  Saudi  Personal  Data  Protection  Law, https://dgp.sdaia.gov.sa/wps/wcm/connect/f579bc32-fda8-47bd-bc6f-66b8cb77985c/ENG-Guide+to+the+saudi+PDP+law+for+controllersprocessors.pdf?MOD=AJPERES

24. The  Saudi  Arabia  Personal  Data  Protection  Law (PDPL) - Usercentrics, https://usercentrics.com/knowledge-hub/saudi-arabia-personal-data-protection-law-pdpl/

25. Saudi  Arabia  Data  Protection  Laws  and  Regulations 2026 - ICLG, https://iclg.com/practice-areas/data-protection-laws-and-regulations/saudi-arabia/

26. Open  Data - وزارة  التعليم, https://www.moe.gov.sa/en/knowledgecenter/dataandstats/Pages/opendata.aspx
