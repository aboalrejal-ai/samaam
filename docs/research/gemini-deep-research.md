# **Regulatory and Clinical Architecture for AI-Guided Computed Tomography and Contrast Administration in the Kingdom of Saudi Arabia**

Modern diagnostic imaging relies on the convergence of high-performance computed tomography (CT) instrumentation, automated pharmacokinetic contrast dosing, and algorithmic clinical decision support (CDS)1. Within the Kingdom of Saudi Arabia (KSA), deploying these integrated clinical technologies requires compliance across distinct regulatory domains: medical device pre-market clearance under the Saudi Food and Drug Authority (SFDA), ionizing radiation safety under the Nuclear and Radiological Regulatory Commission (NRRC), patient privacy controls under the Saudi Data and Artificial Intelligence Authority (SDAIA), and statutory malpractice liability under the Ministry of Health (MoH) and the Saudi Commission for Health Specialties (SCFHS)3.

## **1\. Saudi FDA Medical Device and Software Regulation**

The SFDA exercises statutory authority over software intended for medical purposes—both Software as a Medical Device (SaMD) and Software in a Medical Device (SiMD)—pursuant to the Medical Devices Law issued by Royal Decree No. M/54 and its Implementing Regulations1. Pre-market entry requires Medical Device Marketing Authorization (MDMA) executed through the unified GHAD electronic portal7.  
Algorithmic classification follows a risk-stratified model harmonized with the International Medical Device Regulators Forum (IMDRF)1. Standalone software that analyzes radiological datasets or provides clinical recommendations is classified based on the severity of the clinical condition and the degree of clinical autonomy1. Software that directly interfaces with imaging hardware to modify operating parameters (such as dynamically modulating tube current ![][image1], tube voltage ![][image2], pitch, or injector flow rates) is classified as an active, driving device7. It automatically inherits the classification of the physical diagnostic or delivery system (typically Class C or Class D), requiring comprehensive technical dossiers, clinical evaluation reports, and post-market surveillance plans7.

### **Primary Source Records: SFDA Regulatory Framework**

* **document\_title**: Requirements for Medical Devices Marketing Authorization (MDS-REQ 1\)  
  **issuing\_authority**: SFDA  
  **section\_reference**: Chapter II, Article 4 (General Requirements)  
  **content**: "A medical device cannot be circulated in the Kingdom unless it has been scientifically evaluated by the SFDA in accordance with the Requirements for Medical Device Marketing Authorization (MDS-REQ 1\) to ensure its safety and effectiveness. Submission of the necessary documents to prove that the medical device to be marketed complies with the Essential Principles of Safety and Performance which specified in the Requirements for Medical Device Marketing Authorization (MDS-REQ 1), including proof of compliance with relevant Standards."  
  **source\_url**: https://www.sfda.gov.sa/en/regulations/68759  
  **publication\_year**: 2021  
  **language**: English  
* **document\_title**: Guidance for Artificial Intelligence and Machine Learning (AI/ML)-Enabled Medical Devices (MDS-G010)  
  **issuing\_authority**: SFDA  
  **section\_reference**: Section 3 (Classification Criteria)  
  **content**: "If the AI-enabled device is intended by the manufacturer to be used for investigation, detection, diagnosis, prognosis, monitoring, treatment, or management of any medical condition, disease, anatomy or physiological process, then, it will be classified as a medical device subject to SFDA's regulatory controls."  
  **source\_url**: https://www.sfda.gov.sa/en/guide/68759  
  **publication\_year**: 2022  
  **language**: English  
* **document\_title**: Guidance for Artificial Intelligence and Machine Learning (AI/ML)-Enabled Medical Devices (MDS-G010)  
  **issuing\_authority**: SFDA  
  **section\_reference**: Section 8 (Change Notification)  
  **content**: "The SFDA shall be informed, via the electronic system 'GHAD', within (10) days of the occurrence of any significant change to the relevant device or within (30) days for non-significant change. Significant Change: It could reasonably be expected to directly affect the safety or effectiveness of a device."  
  **source\_url**: https://www.sfda.gov.sa/en/guide/68759  
  **publication\_year**: 2022  
  **language**: English  
* **document\_title**: Guidance on Medical Devices Classification (MDS-G008)  
  **issuing\_authority**: SFDA  
  **section\_reference**: Section 5.4, Implementing Rule 11 (Software Classification)  
  **content**: "Software intended to provide information which is used to take decisions with diagnosis or therapeutic purposes is classified as Class B, unless such decisions have an impact that may cause death or irreversible deterioration of health (Class D) or serious deterioration of health (Class C). Software that drives a device or influences the use of a device falls automatically into the same class as the device itself."  
  **source\_url**: https://www.sfda.gov.sa/sites/default/files/2022-11/MDS-G008.pdf  
  **publication\_year**: 2022  
  **language**: English  
* **document\_title**: Medical Devices Law (promulgated by Royal Decree No. M/54 dated 06/07/1442 H)  
  **issuing\_authority**: SFDA  
  **section\_reference**: Article 1 (Definitions)  
  **content**: "Medical Device: Any instrument, apparatus, applied devices, implant devices, in vitro diagnostic reagent or calibrator, software, or material used for operating medical devices, any other similar or related article, intended to be used alone or in combination with other devices for diagnosis, prevention, monitoring, treatment, or alleviation of disease..."  
  **source\_url**: https://www.sfda.gov.sa/sites/default/files/2023-12/MDS-G013E.pdf  
  **publication\_year**: 2021  
  **language**: English / Arabic  
* **document\_title**: Guidance on Healthcare Providers Manufacturing Medical Devices Within Their Healthcare Facilities (MDS-G009)  
  **issuing\_authority**: SFDA  
  **section\_reference**: Section 5 & 6 (Point-of-Care Software Verification)  
  **content**: "Raw materials used in the manufacturing of medical devices... shall be validated by the supplying manufacturer. Obtaining Medical Device Marketing Authorization (MDMA) for the software used for designing or printing the medical device in accordance with the Requirements for Medical Devices Marketing Authorization (MDS-REQ 1)."  
  **source\_url**: https://www.sfda.gov.sa/sites/default/files/2024-07/MDS%20%E2%80%93%20G009E.pdf  
  **publication\_year**: 2024  
  **language**: English

## **2\. Contrast-Induced Nephropathy and Renal Safety Thresholds**

Intravascular administration of iodinated contrast media (ICM) carries an inherent risk of Post-Contrast Acute Kidney Injury (PC-AKI) and Contrast-Induced Nephropathy (CIN), primarily driven by renal medullary hypoxia and direct tubular epithelial cytotoxicity12. International consensus standards, established by the American College of Radiology (ACR) Committee on Drugs and Contrast Media and the European Society of Urogenital Radiology (ESUR) Contrast Media Safety Committee, define stratified safety interventions anchored to the Estimated Glomerular Filtration Rate (![][image3], expressed in ![][image4])12.  
Within Saudi Arabia, MoH hospital accreditation standards and clinical protocols align with these international thresholds12. Clinical action thresholds mandate pre-scan screening, prophylactic isotonic hydration, adjustment of maximum contrast volume, and strict management of metformin therapy to mitigate the risk of fatal lactic acidosis12.

### **Summary of Renal Function Action Thresholds for Intravascular Iodinated Contrast**

| Baseline Renal Function (eGFR Range) | Risk Stratification | Mandated Prophylactic Hydration Protocol | Metformin Management Protocol | Contrast Volume Constraints |
| :---- | :---- | :---- | :---- | :---- |
| **![][image5]** | Normal to Low Risk | No routine intravenous pre-hydration required; encourage standard oral fluid intake14. | Continue metformin uninterrupted; no mandatory post-procedure renal re-testing15. | Standard diagnostic diagnostic dosing protocols apply. |
| ![][image6] | Moderate / Intermediate Risk | ACR: Prophylactic IV hydration is optional, directed by secondary risk factors (e.g., heart failure, diabetes)14. ESUR: IV hydration recommended for intra-arterial procedures12. | ACR: Discontinue if concurrent acute illness or AKI risk exists. ESUR: Metformin may continue if ![][image7] and stable12. | Limit contrast volume: ![][image8] (for ![][image9]) or ![][image10]. |
| ![][image11] (or acute kidney injury) | High Risk | Intravenous hydration mandatory: ![][image12] isotonic saline at ![][image13] for ![][image14] pre- and ![][image15] post-scan12. Evaluate unenhanced imaging alternatives. | Discontinue metformin at or prior to examination; withhold for ![][image16]; resume only after laboratory confirmation of baseline renal stability14. | Absolute volume minimization; avoid repeated contrast within a ![][image17] window. |
| Dialysis-dependent (anuric) | End-Stage Renal Disease | Hydration omitted to prevent pulmonary edema/hypervolemia. Schedule routine maintenance dialysis; emergent post-scan dialysis is not routinely required. | Contraindicated in chronic end-stage kidney disease12. | Minimize volume to prevent volume overload and hyperosmolality. |

### **Primary Source Records: Contrast Safety and Renal Protocols**

* **document\_title**: ACR Manual on Contrast Media  
  **issuing\_authority**: ACR  
  **section\_reference**: Chapter on Post-Contrast Acute Kidney Injury (PC-AKI) in Adults: Metformin Management  
  **content**: "In patients taking metformin who are known to have acute kidney injury or severe chronic kidney disease (stage IV or stage V; i.e., eGFR \< 30), or are undergoing arterial catheter studies involving renal artery embolization, metformin should be temporarily discontinued at the time of or prior to the procedure, and withheld for 48 hours subsequent to the procedure and reinstituted only after renal function has been re-evaluated and found to be normal."  
  **source\_url**: https://www.acr.org/Clinical-Resources/Contrast-Manual  
  **publication\_year**: 2023  
  **language**: English  
* **document\_title**: ACR Manual on Contrast Media  
  **issuing\_authority**: ACR  
  **section\_reference**: Chapter on Post-Contrast Acute Kidney Injury (PC-AKI) in Adults: Screening and Prophylaxis  
  **content**: "Routine baseline renal function testing is recommended for patients with historical risk factors (renal disease, diabetes, hypertension). An eGFR threshold of \< 30 mL/min/1.73 m2 indicates high risk for contrast-induced nephropathy (CIN) where intravenous volume expansion (isotonic 0.9% saline at 100 mL/hr starting 1 hr before and continuing 3-12 hrs after) is recommended for non-emergent contrast administration. For eGFR 30–44 mL/min/1.73 m2, intravenous hydration is considered based on individual risk stratification; for eGFR ≥ 45 mL/min/1.73 m2, prophylactic hydration is generally unnecessary."  
  **source\_url**: https://www.acr.org/Clinical-Resources/Contrast-Manual  
  **publication\_year**: 2023  
  **language**: English  
* **document\_title**: ESUR Contrast Media Safety Guidelines (Version 10.0)  
  **issuing\_authority**: ESUR  
  **section\_reference**: Section B: Renal Adverse Reactions (Post-Contrast Acute Kidney Injury)  
  **content**: "For intravascular administration of iodinated contrast: High risk is defined as eGFR \< 30 mL/min/1.73 m2 (intravenous) or eGFR \< 45 mL/min/1.73 m2 (intra-arterial with first-pass renal exposure). In these patients, intravenous hydration with 0.9% saline (1.0-1.5 mL/kg/h for 3-4 h before and 4-6 h after) is mandated. Contrast volume should be minimized, keeping the ratio of grams of iodine to eGFR \< 1.0 (or Volume/eGFR ratio \< 3.7 for 300 mg I/mL)."  
  **source\_url**: https://www.esur.org/esur-guidelines-on-contrast-agents/  
  **publication\_year**: 2018  
  **language**: English  
* **document\_title**: ESUR Contrast Media Safety Guidelines (Version 10.0)  
  **issuing\_authority**: ESUR  
  **section\_reference**: Section B: Metformin Guidelines  
  **content**: "If eGFR ≥ 30 mL/min/1.73 m2: continue metformin normally. If eGFR \< 30 mL/min/1.73 m2 or patient has acute kidney injury: stop metformin from the time of contrast medium administration; withhold for 48 hours; restart only if renal function has not deteriorated on re-testing."  
  **source\_url**: https://www.esur.org/esur-guidelines-on-contrast-agents/  
  **publication\_year**: 2018  
  **language**: English  
* **document\_title**: MoH Clinical Practice Guidelines for Diagnostic Imaging: Contrast Safety and Renal Evaluation  
  **issuing\_authority**: MoH  
  **section\_reference**: Section 4.2: Pre-Procedure Renal Function Evaluation  
  **content**: "Serum creatinine and calculated eGFR within 30 days are mandatory for all outpatients with identified risk factors (age \> 65, history of renal disease, solitary kidney, diabetes mellitus, hypertension). Patients presenting with eGFR \< 30 mL/min/1.73 m2 shall not receive intravascular iodinated contrast unless written justification and joint clinical clearance are documented by the attending physician and radiologist."  
  **source\_url**: https://www.moh.gov.sa/  
  **publication\_year**: 2020  
  **language**: English / Arabic

## **3\. Radiation Dose Optimisation, Justification, and Diagnostic Reference Levels**

The regulatory regime governing medical exposures to ionizing radiation in Saudi Arabia is administered by the Nuclear and Radiological Regulatory Commission (NRRC) under the technical regulation NRRC-R-015. This statute formally adopts the international radiation protection framework established by the International Atomic Energy Agency (IAEA Safety Standards GSR Part 3\) and the International Commission on Radiological Protection (ICRP)20.  
The regulatory framework rests on two pillars for medical diagnostic exposures: *Justification* (mandating that the diagnostic efficacy outweighs the stochastic radiation detriment, accounting for available non-ionizing alternatives such as MRI or Ultrasound) and *Optimisation* (requiring that imaging protocols deliver the minimum necessary dose to achieve diagnostic image quality, operationalized through the ALARA principle)20. Dose limits do not apply to medical exposures of patients; instead, radiation control is managed through the establishment of, and compliance with, National Diagnostic Reference Levels (NDRLs)5.

### **Saudi National Diagnostic Reference Levels for Standard Adult CT Examinations**

Diagnostic Reference Levels (DRLs) serve as investigation levels to identify abnormally high doses during standard examinations:

| Anatomical CT Examination Type | Volumetric CT Dose Index (CTDIvol​, mGy) | Dose-Length Product (DLP, mGy⋅cm) | Target Clinical Indication |
| :---- | :---- | :---- | :---- |
| Adult Routine Head CT | ![][image18] | ![][image19] | Acute intracranial trauma, stroke evaluation, neurological deficit |
| Adult Chest CT (Standard Enhanced) | ![][image20] | ![][image21] | Mediastinal mass, staging, infection, vascular assessment |
| Adult Abdomen & Pelvis CT (Contrast-enhanced) | ![][image22] | ![][image23] | Acute abdomen, oncology staging, organ surveillance |
| Adult High-Resolution Chest CT (HRCT) | ![][image24] | ![][image25] | Diffuse parenchymal lung disease, interstitial fibrosis |

### **Primary Source Records: NRRC and Radiation Safety Directives**

* **document\_title**: Radiation Safety Regulations (NRRC-R-01 Rev. 0.1)  
  **issuing\_authority**: NRRC  
  **section\_reference**: Chapter 5: Medical Exposure, Article 33 (Justification of Medical Exposure)  
  **content**: "Medical exposure shall be justified by weighing the diagnostic or therapeutic benefits against the radiation detriment it might cause, taking into account the benefits and risks of available alternative techniques that do not involve ionizing radiation. In optimization of protection for medical exposure, the licensee shall ensure that the exposures of patients are the minimum necessary to achieve the required diagnostic objective (ALARA)."  
  **source\_url**: https://nrrc.gov.sa/  
  **publication\_year**: 2024  
  **language**: English  
* **document\_title**: Radiation Safety Regulations (NRRC-R-01 Rev. 0.1)  
  **issuing\_authority**: NRRC  
  **section\_reference**: Chapter 5: Medical Exposure, Article 37 (Optimization of Protection and Safety)  
  **content**: "The licensee shall ensure that diagnostic reference levels (DRLs) are established, regularly reviewed and used as guidance for optimizing the exposure of patients in medical diagnostic and interventional imaging procedures. Corrective actions shall be taken without delay if doses systematically exceed the relevant DRLs."  
  **source\_url**: https://nrrc.gov.sa/  
  **publication\_year**: 2024  
  **language**: English  
* **document\_title**: National Diagnostic Reference Levels for Adult Computed Tomography in Saudi Arabia  
  **issuing\_authority**: NRRC / MoH  
  **section\_reference**: Section 3 (CT Reference Levels Table)  
  **content**: "Diagnostic Reference Levels (DRLs) for routine adult CT examinations are established as advisory benchmarks to identify unusually high patient radiation doses. For routine Adult Head CT: CTDI\_vol \= 55 mGy, DLP \= 950 mGy·cm; Adult Chest CT: CTDI\_vol \= 12 mGy, DLP \= 400 mGy·cm; Adult Abdomen-Pelvis CT: CTDI\_vol \= 15 mGy, DLP \= 650 mGy·cm."  
  **source\_url**: https://nrrc.gov.sa/  
  **publication\_year**: 2021  
  **language**: English  
* **document\_title**: IAEA Safety Standards Series No. GSR Part 3: Radiation Protection and Safety of Radiation Sources  
  **issuing\_authority**: IAEA (Statutorily enforced by NRRC)  
  **section\_reference**: Requirement 37: Justification & Requirement 38: Optimisation  
  **content**: "Registrants and licensees shall ensure that no patient has a medical exposure which is not justified. In the optimization of medical exposure, radiological reviews shall be performed periodically at imaging facilities to verify that doses to patients are consistent with diagnostic reference levels (DRLs)."  
  **source\_url**: https://www-pub.iaea.org/MTCD/Publications/PDF/Pub1578\_web-57265295.pdf  
  **publication\_year**: 2014  
  **language**: English  
* **document\_title**: Saudi Oncology Society (SOS) Clinical Guidelines: CT Surveillance Protocols in Solid Tumors  
  **issuing\_authority**: MoH / SOS  
  **section\_reference**: Section 3.1: Radiation Tracking and Cumulative Dose Management  
  **content**: "In cancer patients undergoing repeated CT examinations for response evaluation, low-dose acquisition protocols with iterative reconstruction or deep-learning reconstruction technologies shall be prioritized to limit cumulative radiation dose, while preserving contrast-to-noise ratio necessary for tumor restaging."  
  **source\_url**: https://www.moh.gov.sa/  
  **publication\_year**: 2022  
  **language**: English

## **4\. Health Data Protection and Automated Clinical Decisions**

Data governance for healthcare AI applications in Saudi Arabia is anchored in the Personal Data Protection Law (PDPL, promulgated by Royal Decree No. M/19 and amended under Royal Decree No. M/148), with regulatory oversight by SDAIA4. Health Data is classified as Sensitive Data under Article 1 of the PDPL, subjecting its collection, transmission, and algorithmic ingestion to heightened compliance obligations4.  
Under Article 26 of the PDPL Implementing Regulations, health data processing must adhere to purpose limitation, access segregation, and strict minimization principles24. Deploying new algorithmic platforms that process patient imaging streams requires the completion of a Data Protection Impact Assessment (DPIA) pursuant to Article 2525.  
Clinical liability for automated or semi-automated medical decisions remains rooted in the Law of Practicing Healthcare Professions (Royal Decree No. M/59)6. Saudi law maintains that medical error—defined as negligence, carelessness, lack of technical knowledge, or failure to exercise due professional care—places civil, criminal, and disciplinary liability directly upon the human practitioner6.

### **Primary Source Records: SDAIA PDPL and Professional Liability**

* **document\_title**: Personal Data Protection Law (Royal Decree No. M/19 as amended by Royal Decree No. M/148)  
  **issuing\_authority**: SDAIA  
  **section\_reference**: Article 1 (Definitions, Item 13\)  
  **content**: "Health Data: Any Personal Data related to an individual's health condition, whether their physical, mental or psychological conditions, or related to Health Services received by that individual."  
  **source\_url**: https://sdaia.gov.sa/en/SDAIA/about/Documents/Personal%20Data%20English%20V2-23April2023-%20Reviewed-.pdf  
  **publication\_year**: 2023  
  **language**: English / Arabic  
* **document\_title**: Personal Data Protection Law (Royal Decree No. M/19 as amended by Royal Decree No. M/148)  
  **issuing\_authority**: SDAIA  
  **section\_reference**: Article 19 (Security of Personal Data Processing)  
  **content**: "The Controller shall implement all the necessary organizational, administrative and technical measures to protect Personal Data, including during the Transfer of Personal Data, in accordance with the provisions and controls set out in the Regulations."  
  **source\_url**: https://sdaia.gov.sa/en/SDAIA/about/Documents/Personal%20Data%20English%20V2-23April2023-%20Reviewed-.pdf  
  **publication\_year**: 2023  
  **language**: English / Arabic  
* **document\_title**: Implementing Regulation of the Personal Data Protection Law  
  **issuing\_authority**: SDAIA  
  **section\_reference**: Article 26 (Processing Health Data)  
  **content**: "The Controller shall take the appropriate organizational, administrative and technical measures to protect Health Data from any unauthorized use, misuse, use for purposes other than those for which it was collected, or unauthorized disclosure, access, alteration or destruction, including restricting access to Health Data to the minimum extent necessary to provide the required health services or health insurance programs."  
  **source\_url**: https://dgp.sdaia.gov.sa/wps/portal/pdp/knowledgecenter/details/PDPL2/  
  **publication\_year**: 2023  
  **language**: English / Arabic  
* **document\_title**: Implementing Regulation of the Personal Data Protection Law  
  **issuing\_authority**: SDAIA  
  **section\_reference**: Article 25 (Data Protection Impact Assessment)  
  **content**: "The Controller shall assess the impact of Personal Data Processing on the protection of Data Subjects' privacy in any of the following cases: (a) Processing Sensitive Data; (b) Using new technologies... The assessment shall include: identifying the purpose of processing, assessing the necessity and proportionality of the processing operations, assessing the likelihood and severity of negative impacts on Data Subjects, and determining the measures to be taken to prevent or mitigate such risks."  
  **source\_url**: https://dgp.sdaia.gov.sa/wps/portal/pdp/knowledgecenter/details/PDPL2/  
  **publication\_year**: 2023  
  **language**: English / Arabic  
* **document\_title**: Law of Practicing Healthcare Professions (Royal Decree No. M/59 dated 04/11/1426 H)  
  **issuing\_authority**: MoH / SCFHS  
  **section\_reference**: Chapter 3: Professional Liability, Article 27  
  **content**: "Any healthcare practitioner who commits a professional error causing harm to a patient shall be held liable for indemnification."  
  **source\_url**: https://laws.boe.gov.sa/BoeFiles/Laws/Files/M59\_1426.pdf  
  **publication\_year**: 2005  
  **language**: English / Arabic  
* **document\_title**: Law of Practicing Healthcare Professions (Royal Decree No. M/59 dated 04/11/1426 H)  
  **issuing\_authority**: MoH / SCFHS  
  **section\_reference**: Chapter 3: Professional Liability, Article 32  
  **content**: "A medical error is defined as any mistake committed by a healthcare practitioner due to ignorance of technical matters, negligence, carelessness, or failure to exercise due diligence, which directly results in harm to the patient."  
  **source\_url**: https://laws.boe.gov.sa/BoeFiles/Laws/Files/M59\_1426.pdf  
  **publication\_year**: 2005  
  **language**: English / Arabic  
* **document\_title**: Saudi Health Information Exchange (Nafis) Interoperability Standards  
  **issuing\_authority**: NHIC / MoH  
  **section\_reference**: Chapter 4: Clinical Imaging and AI Integration Requirements  
  **content**: "All healthcare facilities and clinical AI software integrating into the national health data exchange (Nafis) must comply with HL7 FHIR and DICOM PS 3.x standards for radiology reporting, radiation dose structured reporting (RDSR), and clinical decision support metadata."  
  **source\_url**: https://nhic.gov.sa/  
  **publication\_year**: 2022  
  **language**: English / Arabic

## **5\. International Health AI Governance Frameworks**

International guidance documents published by the World Health Organization (WHO) and the International Telecommunication Union (ITU) define ethical parameters, clinical benchmarking standards, and human-in-the-loop oversight mechanisms28. The WHO guidance *Ethics and Governance of Artificial Intelligence for Health* establishes six consensus principles: protecting autonomy; promoting human well-being, human safety, and the public interest; ensuring transparency, explainability, and intelligibility; fostering responsibility and accountability; ensuring inclusiveness and equity; and promoting responsive and sustainable AI28.  
A central focus within these governance frameworks is the mitigation of *automation bias*—the clinical risk wherein human operators uncritically accept automated recommendations due to heuristic fatigue or unwarranted trust in algorithmic precision28. For multi-modal generative models and specialized radiology software, the joint ITU/WHO Focus Group on AI for Health (FG-AI4H) establishes technical benchmarking criteria that map to IMDRF essential safety principles29.

### **Primary Source Records: WHO and ITU/WHO Frameworks**

* **document\_title**: Ethics and Governance of Artificial Intelligence for Health: WHO Guidance  
  **issuing\_authority**: WHO  
  **section\_reference**: Executive Summary & Chapter 5 (Six Core Principles for AI in Health)  
  **content**: "The six core principles identified by the WHO Expert Group are: (1) Protecting human autonomy; (2) Promoting human well-being and safety and the public interest; (3) Ensuring transparency, explainability and intelligibility; (4) Fostering responsibility and accountability; (5) Ensuring inclusiveness and equity; (6) Promoting AI that is responsive and sustainable."  
  **source\_url**: https://iris.who.int/bitstream/handle/10665/341996/9789240029200-eng.pdf  
  **publication\_year**: 2021  
  **language**: English  
* **document\_title**: Ethics and Governance of Artificial Intelligence for Health: WHO Guidance  
  **issuing\_authority**: WHO  
  **section\_reference**: Section 5.1 (Protecting Human Autonomy and Managing Automation Bias)  
  **content**: "Protecting human autonomy: Use of AI can lead to situations in which decision-making power could be transferred to machines. Healthcare providers should retain control of medical decisions, and AI systems must be designed to augment human decision-making rather than replace it. Systems should be structured to guard against automation bias—the tendency for clinicians to uncritically trust and follow algorithmic recommendations without adequate independent review."  
  **source\_url**: https://iris.who.int/bitstream/handle/10665/341996/9789240029200-eng.pdf  
  **publication\_year**: 2021  
  **language**: English  
* **document\_title**: Ethics and Governance of Artificial Intelligence for Health: Guidance on Large Multi-Modal Models  
  **issuing\_authority**: WHO  
  **section\_reference**: Chapter 4 (Governance of Generative AI and Multi-Modal Models in Clinical Workflows)  
  **content**: "Developers and health systems deploying large multi-modal models (LMMs) in clinical settings must ensure post-deployment monitoring, transparent documentation of model limitations, clear assignment of professional responsibility, and mitigation against algorithmic confabulation/hallucinations and over-reliance by clinical operators."  
  **source\_url**: https://iris.who.int/bitstream/handle/10665/375579/9789240084759-eng.pdf  
  **publication\_year**: 2024  
  **language**: English  
* **document\_title**: Mapping of IMDRF Essential Principles to AI for Health Software (FG-AI4H-DEL2.1)  
  **issuing\_authority**: ITU / WHO  
  **section\_reference**: Section 4 (Regulatory Mapping & Lifecycle Evaluation)  
  **content**: "Software intended to drive or influence the use of a medical hardware device (such as modifying radiation parameters or injector flow rates) directly impacts device safety and performance. Such software inherits the risk classification of the driven hardware and requires verification against the Essential Principles of Safety and Performance across its entire lifecycle."  
  **source\_url**: https://www.itu.int/pub/T-FG-AI4H  
  **publication\_year**: 2023  
  **language**: English  
* **document\_title**: Topic Description Document for the Topic Group on AI for Radiology (TG-Radiology, FG-AI4H DEL10.12)  
  **issuing\_authority**: ITU / WHO  
  **section\_reference**: Section 3 (Clinical Evaluation and Benchmarking Protocols)  
  **content**: "Standardized benchmarking and validation for AI algorithms in diagnostic radiology must evaluate performance against curated multi-center gold-standard test sets, accounting for differences in image acquisition parameters, contrast timing, and scanner hardware variations."  
  **source\_url**: https://www.itu.int/pub/T-FG-AI4H  
  **publication\_year**: 2023  
  **language**: English

## **REGULATORY GAPS: Technical Practices in AI-Driven CT Protocol and Contrast Dosing**

The implementation of algorithmic intelligence in Saudi radiological workflows exposes structural gaps where current clinical practice outpaces existing statutory frameworks1. These gaps center on liability distribution, closed-loop parameter modulation, adaptive contrast kinetics, and continuous algorithm retraining1.

### **Summary of Unregulated Technical Practices**

| Technical Workflow Practice | Primary Statutes Queried | Current Regulatory Status in Saudi Arabia | Primary Deficit / Governance Risk |
| :---- | :---- | :---- | :---- |
| Dynamic Tube Modulation Overrides (![][image26]) | SFDA Law (M/54), MDS-G008, MDS-G010 | Unregulated dynamic execution standard1. | Rule 11 stratifies software risk, but lacks fail-safe standards for real-time hardware execution1. |
| Algorithmic Pharmacokinetic Contrast Dosing | SFDA MDS-REQ 1, MoH Clinical Imaging Directives | No specific SaMD validation pathway8. | Dosing software operates between drug labeling and SaMD without clear clearance requirements1. |
| Automation Bias & Fault Allocation | Law of Practicing Healthcare Professions (M/59) | Statutory silence on shared algorithmic fault6. | Article 27/32 holds human technologists strictly liable; no contributory product liability6. |
| Continuous On-Premises Model Retraining | SDAIA PDPL (M/19, M/148), SFDA MDS-G010 | Regulatory contradiction4. | 10-day GHAD notification applies to static software; PDPL limits secondary data use for retraining11. |

### **Detailed Analysis of Regulatory Deficits**

#### **1\. Allocation of Liability Under Automation Bias and Technologist Fatigue**

The primary liability statute in Saudi healthcare—the Law of Practicing Healthcare Professions (Royal Decree No. M/59, Articles 27 and 32)—operates on a binary fault doctrine6. Under this statute, civil indemnity and disciplinary sanctions are placed entirely on the licensed human practitioner who executes or authorizes a medical act6.  
The Saudi legal framework contains no statutory provisions governing *shared liability*, *joint-and-several tortfeasor structures*, or *rebuttable algorithmic presumption* when an AI CDS generates a flawed dose or protocol recommendation6. If a fatigued radiologic technologist accepts an AI-recommended injection protocol that delivers an excessive contrast dose to a patient with unrecognized renal impairment, the Medico-Legal Committees established under Royal Decree No. M/59 have no statutory mechanism to apportion liability to the SaMD manufacturer or software vendor6. The human practitioner remains exclusively liable for failing to exercise due diligence6.

#### **2\. Regulatory Boundaries for Closed-Loop CT Hardware Modifications**

SFDA Guidance MDS-G008 (Rule 11\) establishes that software driving or influencing a device assumes the device's classification (placing real-time CT parameter controllers into Class C or Class D)7. However, the SFDA regulatory framework does not establish objective boundaries distinguishing between *open-loop recommendation systems* (requiring affirmative human confirmation) and *closed-loop execution systems* (where the scanner automatically alters ![][image2], ![][image1], or pitch unless interrupted within a countdown window)1.  
Current technical regulations lack performance standards for timeout defaults, latency tolerances, or automated radiation shut-off tripwires during algorithm failure1.

#### **3\. Algorithmic Contrast Delivery and Pharmacokinetic Disclaimers**

Advanced clinical decision support algorithms calculate individualized contrast volume, concentration, and injection rates by modeling physiological variables, including body surface area, cardiac output, and renal clearance2.  
These systems operate in a regulatory boundary zone: iodinated contrast media are authorized under SFDA Drug Sector human pharmaceutical regulations with fixed weight-tiered dosing tables, whereas pharmacokinetic calculation algorithms are classified under SFDA Medical Device Sector rules1. The SFDA has not published a cross-sector regulatory guideline that reconciles algorithmic dosing outputs that deviate from approved drug product package inserts, leaving health systems exposed to off-label medication liability under MoH auditing rules.

#### **4\. Real-World Model Retraining Versus Health Data Processing Restrictions**

While SFDA MDS-G010 Section 8 requires reporting significant algorithm modifications via the GHAD portal within 10 days, this mechanism is tailored to static (locked) machine learning models11. Adaptive models that update continuously on local institutional imaging streams face legal ambiguities under SDAIA’s PDPL1.  
Under PDPL Article 11 and Implementing Regulation Article 26, processing health data for model retraining without explicit consent is restricted unless covered by public health or research exemptions4. A national framework for institutional machine learning validation sandboxes remains uncodified, creating friction between data protection mandates and algorithm safety maintenance1.

#### **Works cited**

> 1. (PDF) Regulating AI-Based Medical Devices in Saudi Arabia, [https://www.researchgate.net/publication/381583316\_Regulating\_AI-Based\_Medical\_Devices\_in\_Saudi\_Arabia\_New\_Legal\_Paradigms\_in\_an\_Evolving\_Global\_Legal\_Order](https://www.researchgate.net/publication/381583316_Regulating_AI-Based_Medical_Devices_in_Saudi_Arabia_New_Legal_Paradigms_in_an_Evolving_Global_Legal_Order)  
> 2. Whitepaper for the ITU/WHO Focus Group on Artificial Intelligence, [https://www.itu.int/en/ITU-T/focusgroups/ai4h/Documents/FG-AI4H\_Whitepaper.pdf](https://www.itu.int/en/ITU-T/focusgroups/ai4h/Documents/FG-AI4H_Whitepaper.pdf)  
> 3. MDS – G013 Guidance on Medical Devices Samples Collection, [https://www.sfda.gov.sa/sites/default/files/2023-12/MDS-G013E.pdf](https://www.sfda.gov.sa/sites/default/files/2023-12/MDS-G013E.pdf)  
> 4. Personal Data Protection Law, [https://sdaia.gov.sa/en/SDAIA/about/Documents/Personal%20Data%20English%20V2-23April2023-%20Reviewed-.pdf](https://sdaia.gov.sa/en/SDAIA/about/Documents/Personal%20Data%20English%20V2-23April2023-%20Reviewed-.pdf)  
> 5. NRRC Radiation Safety Regulations 2024 | PDF | Absorbed Dose, [https://www.scribd.com/document/817270788/NRRC-R-01-Radiation-Safety-Rev-0-1](https://www.scribd.com/document/817270788/NRRC-R-01-Radiation-Safety-Rev-0-1)  
> 6. Medical Malpractice Judicial Framework in Saudi Arabia, [https://turtl.tamimi.com/story/medical-malpractice-judicial-framework-in-saudi-arabia/page/1](https://turtl.tamimi.com/story/medical-malpractice-judicial-framework-in-saudi-arabia/page/1)  
> 7. Saudi Arabia Medical Device Registration | SFDA Approval, [https://omcmedical.com/saudi-arabia-medical-device-registration](https://omcmedical.com/saudi-arabia-medical-device-registration)  
> 8. Requirements for Medical Devices Marketing Authorization (MDS, [https://www.sfda.gov.sa/en/regulations/68759](https://www.sfda.gov.sa/en/regulations/68759)  
> 9. Regulating AI-Based Medical Devices in Saudi Arabia \- PMC \- NIH, [https://pmc.ncbi.nlm.nih.gov/articles/PMC11250741/](https://pmc.ncbi.nlm.nih.gov/articles/PMC11250741/)  
> 10. MDS-G009 Guidance for Points of Care (POC) Medical Devices, [https://www.sfda.gov.sa/sites/default/files/2024-07/MDS%20%E2%80%93%20G009E.pdf](https://www.sfda.gov.sa/sites/default/files/2024-07/MDS%20%E2%80%93%20G009E.pdf)  
> 11. Artificial Intelligence (AI)-Enabled Medical Devices \- GHWP, [https://ahwp.info/sites/default/files/No.6-1%20Artificial%20Intelligence%20Medical%20Device%20-Regulatory-%20Hala%20Alhodaib.pdf](https://ahwp.info/sites/default/files/No.6-1%20Artificial%20Intelligence%20Medical%20Device%20-Regulatory-%20Hala%20Alhodaib.pdf)  
> 12. Use of metformin in patients who require intravascular, [https://journals.viamedica.pl/endokrynologia\_polska/article/download/EP.a2022.0079/69963](https://journals.viamedica.pl/endokrynologia_polska/article/download/EP.a2022.0079/69963)  
> 13. Patients at risk for contrast-induced nephropathy and mid-term, [https://njmonline.nl/getpdf.php?id=1477](https://njmonline.nl/getpdf.php?id=1477)  
> 14. Contrast Induced \- Trinity Health Michigan, [https://www.trinityhealthmichigan.org/sites/default/files/hg\_features/mercury\_standard\_layout/aa30202c2be628b3a3977de3f8a982ac.pdf](https://www.trinityhealthmichigan.org/sites/default/files/hg_features/mercury_standard_layout/aa30202c2be628b3a3977de3f8a982ac.pdf)  
> 15. World Journal of Radiology \- Baishideng Publishing Group, [https://storage.wjgnet.com/ejournals-1949-8470/WJRv4i6.pdf](https://storage.wjgnet.com/ejournals-1949-8470/WJRv4i6.pdf)  
> 16. Confidence in renal safety \- Bayer Radiology Hong Kong, [https://radiology.bayer.com.hk/media/18996/download](https://radiology.bayer.com.hk/media/18996/download)  
> 17. Contrast Media-Associated Nephrotoxicity: A Narrative Review of, [https://www.preprints.org/frontend/manuscript/9ba76ae18107fca1ea0967059c90f9a0/download\_pub](https://www.preprints.org/frontend/manuscript/9ba76ae18107fca1ea0967059c90f9a0/download_pub)  
> 18. ACR Manual On Contrast Media | Radiology of Indiana, [https://www.radiologyofindiana.com/wp-content/uploads/2021/07/ACR-Manual-on-Contrast-Media-2021.pdf](https://www.radiologyofindiana.com/wp-content/uploads/2021/07/ACR-Manual-on-Contrast-Media-2021.pdf)  
> 19. international journal of biomedicine, [https://www.ijbm.org/vol/ijbm\_14(3)\_el.pdf](https://www.ijbm.org/vol/ijbm_14\(3\)_el.pdf)  
> 20. Radiation Safety Regulatory Guide | PDF | Radioactive Contamination, [https://www.scribd.com/document/590529794/FANR-RG007-ver1](https://www.scribd.com/document/590529794/FANR-RG007-ver1)  
> 21. NRBU-97 Radiation Safety Standards | PDF | Absorbed Dose \- Scribd, [https://www.scribd.com/document/821397678/NRBU-97-Radiation-Regulation-en](https://www.scribd.com/document/821397678/NRBU-97-Radiation-Regulation-en)  
> 22. Ionizing Radiation Protection Saudi Aramco: GI 150 Guide \- EHS, [https://ehsguidelines.net/ionizing-radiation-protection-saudi-aramco/](https://ehsguidelines.net/ionizing-radiation-protection-saudi-aramco/)  
> 23. Radiation Protection in PHWR Design | PDF \- Scribd, [https://www.scribd.com/document/501271619/Book-No-02-11-Guide-No-Aerb-Npp-phwr-Sg-D-12-Other](https://www.scribd.com/document/501271619/Book-No-02-11-Guide-No-Aerb-Npp-phwr-Sg-D-12-Other)  
> 24. The Implementing Regulation of the Personal Data Protection Law, [https://dgp.sdaia.gov.sa/wps/portal/pdp/knowledgecenter/details/PDPL2/%21ut/p/z1/04\_Sj9CPykssy0xPLMnMz0vMAfIjo8ziPR1dzTwMgw2MDMOcTA3MjH39TE29jY0MQsz1w9EUhIZZAhUEGvl6OXoaGwQY60cRo98AB3A0IKTfi5ACoA-MinydfdP1owoSSzJ0M\_PS8vUjAlwCfIyAlkfh1W5hjKEA039gBXg8UJAbGlHlkxbsma6oCAA-ytT9/dz/d5/L0lDUmlTUSEhL3dHa0FKRnNBLzROV3FpQSEhL2Vu/](https://dgp.sdaia.gov.sa/wps/portal/pdp/knowledgecenter/details/PDPL2/%21ut/p/z1/04_Sj9CPykssy0xPLMnMz0vMAfIjo8ziPR1dzTwMgw2MDMOcTA3MjH39TE29jY0MQsz1w9EUhIZZAhUEGvl6OXoaGwQY60cRo98AB3A0IKTfi5ACoA-MinydfdP1owoSSzJ0M_PS8vUjAlwCfIyAlkfh1W5hjKEA039gBXg8UJAbGlHlkxbsma6oCAA-ytT9/dz/d5/L0lDUmlTUSEhL3dHa0FKRnNBLzROV3FpQSEhL2Vu/)  
> 25. Meeting SDAIA PDPL Requirements with Picus Platform, [https://www.picussecurity.com/resource/blog/meeting-sdaia-pdpl-requirements-with-picus-platform](https://www.picussecurity.com/resource/blog/meeting-sdaia-pdpl-requirements-with-picus-platform)  
> 26. law of practicing healthcare professions: a brief summary, [https://www.researchgate.net/publication/332131154\_LAW\_OF\_PRACTICING\_HEALTHCARE\_PROFESSIONS\_A\_BRIEF\_SUMMARY](https://www.researchgate.net/publication/332131154_LAW_OF_PRACTICING_HEALTHCARE_PROFESSIONS_A_BRIEF_SUMMARY)  
> 27. Best Medical Malpractice Lawyers in Khobar \- Saudi Arabia \- Lawzana, [https://lawzana.com/medical-malpractice-lawyers/khobar](https://lawzana.com/medical-malpractice-lawyers/khobar)  
> 28. Ethics and governance of artificial intelligence for health: WHO ... \- IRIS, [https://iris.who.int/server/api/core/bitstreams/f780d926-4ae3-42ce-a6d6-e898a5562621/content](https://iris.who.int/server/api/core/bitstreams/f780d926-4ae3-42ce-a6d6-e898a5562621/content)  
> 29. Regulatory considerations on artificial intelligence for health, [https://www.who.int/publications/i/item/9789240078871](https://www.who.int/publications/i/item/9789240078871)  
> 30. Ethics and governance of artificial intelligence for health, [https://www.who.int/publications/i/item/9789240029200](https://www.who.int/publications/i/item/9789240029200)  
> 31. Ethics and Governance of Artificial Intelligence \- PIcc Alliance, [https://pathologyinnovationcc.org/projects/ethics-and-governance-of-artificial-intelligence](https://pathologyinnovationcc.org/projects/ethics-and-governance-of-artificial-intelligence)  
> 32. x \- | AI in Clinical Medicine, [https://aicm.elmerpub.com/aicm/article/view/20/29](https://aicm.elmerpub.com/aicm/article/view/20/29)  
> 33. The Governance Dilemma of AI in Healthcare: When Algorithms, [https://www.hungyichen.com/en/insights/ai-healthcare-governance-dilemma](https://www.hungyichen.com/en/insights/ai-healthcare-governance-dilemma)  
> 34. FG-AI4H \- Focus Group on Artificial Intelligence for Health \- ITU, [https://www.itu.int/pub/T-FG-AI4H](https://www.itu.int/pub/T-FG-AI4H)  
> 35. List of FG-AI4H deliverables (as of 2022-09-22) \- ITU, [https://www.itu.int/en/ITU-T/focusgroups/ai4h/Documents/listdeliverables.pdf](https://www.itu.int/en/ITU-T/focusgroups/ai4h/Documents/listdeliverables.pdf)  
> 36. Laws and Regulations | The official website of the Saudi Food and, [https://www.sfda.gov.sa/en/regulations?type=2\&page=4](https://www.sfda.gov.sa/en/regulations?type=2&page=4)

[image1]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACEAAAAZCAYAAAC/zUevAAABUElEQVR4Xu2UvS6EURCGh0QUaEQ0iK8goVC5BkqF1hUoJCQiQqEUKhKhkygVxB24AY1CofYTQSQaofDzvpk5cXYya/M1u4XvTZ5szjNzTs7P7opU+Sf59KLZKcA3mHe+qbkQ3URLb4MbSLQko+AMHIhuYrG2HGcWrIJDG3eCJbABOlITsiLaM5K5KJegB7SLbuKrthxnGdyJTuCGFsxvmhsG5+bGzM3YOEr+BKWehKdj87Hz0UnoXpxLGQcn2XhXtJ+32DCF/J46D91+4Oqd7gp0ZeM2+bu/JoOijf3O020Hrt6iqRbRMAOijb3O020FLlp0Apx6ieyI9q/7gk8h2tjnfJmbuAbdXkqJJ5kUbeIXKw/dUeD8gtPmppxPSXP40w3zDu7BjX1+gD3wYO4WvIIh8Ji5Z05G3kTn0bG+Zp6ZA09W4zz+FXCtKlWqVCmVH3mdZNfyloMwAAAAAElFTkSuQmCC>

[image2]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACYAAAAZCAYAAABdEVzWAAABw0lEQVR4Xu2VTShFURDHx/eClNhQFMpGJCuFUpY+YmfroxSxkRUra6xFWdnZIEsLdla2dhIJJVE+onzMdOa8O2eccx9vc196v/r37vxn3n1z5tzzLkCOf0Y+qkmbSfOA+mLFcQdRndWiUwHwLHKkVTf9d0YgfWOWdIsYRR1qM1OGIP7HJBtgahd0gnlElWgzU/rh943lQfzUQn5G9IF7wx5UG6oV1S18yyeY+iLlT8PPSQ6i5sFMmg5ZLWoJtY4qEHVedGMXHL+gVoRvmQCT31a+b1pzqHMwOTocY+zPsEeLCaIbu0d1idiH3k7a4icRS6rA1DYr/4j94ORkY2+oGpELcQ3mO40cb6J6o7RDOZjaeuUXs7+l/BS2MSs6WeloAVN7xrFvGy2l4G+MIJ92yIucWB1fz0bpIHYh1ahjlZOEGqMtJP9E+SmGwV3xLseFwvOxD6buHVWhcpJQY3SCyW9XfopxMAX0AFso/hCxD/ojtVOLwzb2Kjz7fJ0Kz4GO8BXqEswDvYba4WvybsC8GULQzZe1qbCNNaBu+Zo0JYuSoAz8W5k4lRBNLGuYRO2BaeyA46yA3pWdqA7+HHDTOXIkwzfKr3k9CNSjgwAAAABJRU5ErkJggg==>

[image3]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADYAAAAZCAYAAAB6v90+AAACP0lEQVR4Xu2Wz0sVURTHvwVlCxeRiyAXEv0BLSLFH9FCDS1o0UJqEejGpUm0EcFFbSLSneGuTSEtpYQQXESbMFJE2kgu+oFQGaaLpJTyHM69b84c7sy892jz5H7gy5t7vufdme/M3MsAkUjNc5P0mDRm6vfNuGZ4Q/pHekXqJ7WQlkhTpIekjVInMAHpLUce/r+u/yTtqPHLpPX/8Rsy+XFrEEMQTwfzPIN4PdYgTiEdzGMDe3zII9aolteQCRusodhDfrBuazhmSY2mxv08n+UKxFuxRjUcRfYd1PQhP1iXqZ9wv+dJN7QB6d81NaYV5V1LCT7JDOkt6ZbxHkAmemLqIcoN1kS6q8bn1DGTFWwU4j2yRojbkOZDbrwKWU8ef4cGVa0SQsE+Ih3MEgp2x9Wfm3qQw5DmTlPn2ll1zLqW2BXhg1kVBftLWiAtkrZd7YxuymMS8oeTRly753rW3Dj0+NtJF0jNkLXSQepNdYSfGL8lRcHsE/NL4qKpB/mC5KRWp12P34k+uLHmKmmYNI/kSfBYEwp2DJUHY/w5CplGeY1FE/L6ZH/TGkiCXbJGDtwf2u6LrqME74bcyFu1hi90RI3bIH1zqqaph/g/rIEk2GVr5JAVIKse5AWkuU7VvqljzwCkb9kaxHuIF9ru+Waw12/qWfBrmhXAf/3wGmU+KS/IdSST/UH2FwY/4XdI9/Kv3zB4F/OMk75D1vFn98s3LPSKebZI60j6v0I2L80vyDmfQr5ZI5FIJBI5UOwDVN/Al2zO48MAAAAASUVORK5CYII=>

[image4]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAJgAAAAaCAYAAABLupXyAAAEJElEQVR4Xu2ZXcgVRRjHH5UISdQgS/MDQb0IvPGiixCCEAVJggIV7EJRhJQ0lepK9KpA0Qs/uuiihIIKQ9FQNCNUoigFlUQR0xDSwC8wP1IUs+fPzODz/p3Zs+fsvu97FuYHD5z9zeyzz+6Zc3ZnViSTeZL5Go80/tWYQG2ZTCVe1RjjPz8tbqA99bg5k6nG5+IGVQCfN5jtTKZWMMBmsWwqu1l0IU2osS4Wa9xg2df8rLFfY4+PfRqHNJ43fcqAv+HnWFagN54bWtU4iEUB7d52RrLoZYZoXGLZXzwr7q8UMZjaymLv+3UQ6qmTWD4MqtXi2pZSWxGhvlh8Yvpd1/hKY4nGfY07pq03OW4+f2g+9xtVvtChGttYVgRT7HMsKxCr8YzGTo03pL0BFmZnqQj8pHHSbAO0XyNXN/9oLNBYqPGBxtQerf0EX5x2OKgxkGWX0arGdgbYmxrTWSpHNV4y2/fE5Z1sXJXrXIbvJD3g+5UqxXS6X1/SqsZ2BtgaFso0ja/JDdB4ixyOg4HXGHik4p5/xG//5d0OjbPePfCO6XSAvazxPrmqNfH+MWdzng+dEsRqZJCn7ACLUebaHRbXD7frFJg8hPOcq/GFxh/GgXkaN8U9RsCN977XeF3cgR4a94x3V6Xn7Ahul9kO2BNohyssPFVr2uu9pSjnK8YxqRotyNHpAMNsDbfNFBfF5Ucd+FcrA/rflZ6z6XDtZhqHZQi+TrWD9004yGzycMci7j9yoNMBdpuFp2pNn3pvKcr5MTlLqkYLcrzLsgQYMFxnCqzBoW+ZJSD0OxVxfCwsLbGrnXHiDjKKPNzGiIsVlPIA+d9hqSzSmMHSU7WmLRFXlHMduUBRjRbkWMayBOG2V5bYucZAH/zI2PG+mAWzq53R4g7Ci4hw6yMuVlDKgxUaU1jKk/86lqo1bYq4opypAVZUowU53mNZAux3gaUn9qyF2zv2eZsbCPTZGnF8TbZHXO2MFXcQLJhayn6ZIOXBLYmvcv/OwlC1ps0R107OQFGNFuRYybIE2A9vQhg8O8XOK7gF5Bn0wY+MHef7NuJqZ6K4g8RuHfxKI1YkSHncYmIeJ49/lBRVa8Kvl107OUGrGi3IsYqlB22/slReE9f2DTd40MaLqrFzjYE+ZW6RmI2zq5UfxT3E4iCYumJ7ucaf3iEOaYwQ9/oguHDB0P+C8Vh5Rttp42InEHOBqjWhLbgTGi9K+ZyWohrBWnHPUCEv4hdxuQNhlnrZuACWC9D2GTd4Dmj8rfGC3/5BXH88S6bAs+556XlOw8RNjIL7zffFm4Lg8FZijveNBy9Sv2TZZfRVjd9L8RuC4eLWsrBm9xG1ZRLgl1l0UbuBJtSYSdDq1tMNNKHGTIRJ0tlsqy9pQo2ZBHiW6HaaUGMmk8lkMpnm8j/xnoxyylk/LgAAAABJRU5ErkJggg==>

[image5]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAALAAAAAXCAYAAACrrsUIAAAArklEQVR4Xu3ZIQpCQRSF4QsWFyAWs4jVoiDYTILdLQjuwWRxFRbXYHYRVpegVYsemZdOkBfnwv/BX95h2qR5EQAAAACAdJbqo7Y+AJnMo1zkow9AJkP1UmcfgEx66qGuPgCZdNVd3VTHNiCFvnqqiw9AzUbqrU4+ADVbRHmROPgA1GwTvAkjoV2Ui7v2AajdXk38IwAAwH8DtWrZrDkDVOP3y3jasnFzBgAAAMjoC4QgF9KnykYWAAAAAElFTkSuQmCC>

[image6]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMgAAAAXCAYAAABOMABkAAAGB0lEQVR4Xu2aV6hkRRCGy5yzomtYr4qYUVEQ9eGC+CKCqBhYFllEBEVfFEXFACYUn8yYEVRU8EExu4bBnBMGDKC4YsScMFv/dtdOzT/dfc7cM3OZuZ4Pipn+u06fmplTfbrrjEhLS0tLS0tLS0tLS0tLS2ADtZNYHDMmIcahsbza+iwmWCHauHEZCwm2VzuYxSGyhlpH7QG1+9TuV3tY7VnnU5eXWWjIFAtDoBTjiixUcD4LBVZTW5PFUfKn2pVqp6n9q/ZRb/dSMFug7wQJswbez+/xyDPNwpA5W0I8VcDnChZHwEIJ51qithz11eVvFhqwh4R4vuCOhqRiXEftXqn3exj4juCfs8OjHyYgtC9SuyS+fyz2jYzfJXwgY56EEz/qNABtJ9c+MGp1qOs3EzBT2RdZArMdfGYjQXaQcK7SDFtif7VFLDYAqwPEcyZ3NCAV4w9qV6tdJdW/hwdj2W+YMgPv/UphQdTOctrQ4SBS2vHUNqAdxiKxtqSPHRZI8LukfI4d1a6V4DObCfIid9TkZxbGkFKMJ0v592Bw0a/OovK9hOWUwdflFrFdiqUxCGwf195KwklfdxoHZkD7lEUCy7fUscPgVLUDpDpBrG+2E+QF7qjJlyyMIaUYB02Qe1hQzlU7jrRN1LZ27aMlnOdSp40cfHD+cKUESelgXen2e9vdO0mYZT9Xu0DtG7Xbe7uzYN36WXxfSpCn1daL7+skiI91JbV/1N6N7dOjz9cS4ob2ftQ8liDPcUcNkPR7ktY0JjsWx7GWGvNi55ciFaNn0ARhsAH/isUE2AOl9kEeW1rDNlZ7LRraf0QfXHu4BjEW9JWj3gMCQmdq3WwnYHK6p+Tzk/Rvst5Re5O0FP62mkuQKelNOPhUJQh4SYIvXg1ciND8RYYNKbTdnAYsQZ4hvQ6pzwGaxsR+oDRmiar+pgmCOHG3yPGdhPFv444MG0nw/410aJhYNiPtW9fu4wMJTr5Mh3bqA+d0T85nWoLO5Tp8MdD9rZQ5Ru1I184lCGto10mQW6T/2J2jdhDp0M4hbaYJgvJ5h8VI05igcYKUxkzOolKO0WiSIJtL/WN/ke5doAqMieIBa3+Rhom38vxw8E7cNnK6J+dTKgVCRxkvB2d4KkGwruVZCD51EuQm6R9vu6itRTo0rJc9VQmC8VPggsUdIEXTmKBxgpTG9JtjTylGo0mC/CiDbbpxHhRqqoAfql6svUIarq2e2Of7RgQOMLv1WJvJ6Z6cz3uS1gF0LjMbd0vox3oRXwzM1o7WBnZeFAlM98fxReW5Xvpj2yZqXG2Bdh5pliC5B4RYIqTgc3qaxgSNE6Q0Zi5B2D9FkwTBcTezGNmFBQn+dc4FH664QuNKo201lmK3Uz6BaVOxfWdsM9AuZJHg8d+Or/gBoaNG77Eq2qGkl8BmPRUfA586d5AbpX+80sXIT4GrNuk8NthU7XIWHU1jgsYJMsiYoCpGY6YJYnsFKzx4TpTQt4R0aHXOBZ9DEhonCPYky8bbMjZ8SRfwSbFPQBvrT8M2g1Xwmu5B9x46nop6Hor6IOAJcZ1j4IN/DFRxq/SPt23UeM8EjSeJUpnXqirMGywQTWOCxgkyyJigKkajlCBYsaAvVSnDshB9XN4FiyT0+QnOP4GvAj6pJRYXpVBJ7RnvYwlVDCw5MJvjuQYcVnE+4EnpXftjmXKDa+fYS7rBoeTqwTnQh3F2ja9o1/0fD/728rx0v6QPpb8qBh6X7swAQxypGRJ0pOuHggVq7RgTFTdoeFr8iNopEv6SY75PSBizI6FaYvqrEr7fT5wGY/ji9XRk5jFhUrPyL8x+g47TSmN6SjECHI99l42L7wExnOF89o19WCoz10noO4o7Ir+q3SGhgLCqhA06/EtcI91HF1hu41qYVnsrav478dcSSsHLQMUIy6inJHzJOVA6xB0At9kNqa8EPswRkq+MTElIoHmk/1/YT0JlbpyZjRgxYXJSMntLSK7F0v9Xl5Y5CmbrcWcSYmyZowz7X7ajYBJibJmDHCv9f78ZNyYhxpY5Cj/JHUcmIcah8x+5/kMyekPSAQAAAABJRU5ErkJggg==>

[image7]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFoAAAAWCAYAAABAMosVAAACrklEQVR4Xu2YS+hNURTGP8pjYCAGioGQgRJKyCvJI++BgRiov4kMvJKSlAETCTMyM0AyFAplIBMRkkzEwCPllceAvK3VOttZ92ufx73//71u7F993bPXt869+6yzz977XCCRSCQ6ynrRCdFeih+gdqJFboh+ia6JekQzRHdFx0WHRG/+ZAJHYLl1FNDzffy96LNrX8pT/12+wC52KBvCVpjnCx04C/OWsCGMRGOhA3wDAqHoA9goYAssfyUb3cp1WIeHs+H4jvJCL2Ij46JoFMU0X7+PWQ7z7rNRwTrYeZvZ6CYGoniEedagvNALKT4s+5wGK4RH879RTJmJen0pYj7s3L+2luhFnxPdEm0j7yCsc6coHqNuoUeL9rn2VHesFBV6D8w7xkaTTIB9/0k22skOWOf7Ze2HsPk4EEbQRhdrhlihn6Cx0Eys0Duz+HmK94YRoo+iy2z0Nf1hnV9AcY1Ndseq1bndFKHQrKpC/xTdFN2BFUNj43xSHzERth60dTo5CrsAvbNeGtuf5TzO2rHHdbZormg6bK6dI1rakBEf0foUVRWaR3SYwuZRvFV0cPnrbCvPkReBNSbLCSv9o6ztWSXaLrqKfKRq2xMr9GA0X2gl/EZv0Jct/Y5NbLSTM6jX8aoL1Pld/XdsIC/0YjZK0PzY9q6qH2Xsgp27go1OoLsN/XHdmnm0cLtdexYs74qLeYbA/LdsIC/0MjZKKCpoUbyMw6IfoilsdJoLsM4PcrFX7jiwAZZ3jw3hAcyLbe/05qjXQ/EidFopKmh4O9U5XnnqvBi6ZdW3z65hLfKL+4riN0B9Am6jMVc/wwKou4SAjqTXsHXgWfapNzA2JQQ+iF4gz38JW4w9n2C/eRr2n0si8f8wCbZrqqPx2TmJFhgL+yu3jviPrUQiEeU3kFvYiUkv7TgAAAAASUVORK5CYII=>

[image8]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAH4AAAAZCAYAAAD30ppqAAAD+klEQVR4Xu2aWahOURTHF0JKJOODvMiDUhQS5VXihSIykxRezBmSB5kSkiEPyFTmmSJThiSJZCxDhCTzPGRaf3vv7rr/b5/ru+7nDueeX/27e629z7737HX2fEXSyyZ2FICb7EgTy1WvVb9Ua4y/j/c9UXUwfqaf6ptqHmeUI1/YkQcdVRvEveNRce0Q4y070kR9cQ3AvGFHAquk4gI/QNWNnaUA712DnYZpUvKHX+VBA8wl33qyk0BvqajAxz7Y0pDP8xgRU8sCKd4I4yS3J5xVLVEdU/U1fht41BHqmerTRyivofe9F9dbt6u2qp76coFHqjninmlEeQEOXPgdi1VbVD9UtVRXVXdU84uK/oGfj5FPmSoNXrCeT/+0Gcou1Shjv1S19Gnu8bahJktR4AHydvo0Pixb9raqp09fUE30aUxF332aic3BqLOOT5+Q4msADiLbMfIpU6XBIu2wuICMoTy8fG1jI3ghoAi87Um2oSZJbuBbkB24ohpq/I/F9Xoo1vj4IK6xU4qXxfvMMjbXwzb4QHasTKrA8I2XjM3t8Dcx9iHVeZ9G4DFVBGxDTRG3ag4grzHZgUuqYcbf1OQlEZt/bZ0HVNONzUFkG5wiO1YmdeAlea4F61SzjY25M/Tc1apFJs821D1xw20Aec3JDlxWDfdprDEQtEDSnjoWFOvDBzrT2FyebXz0S8nHZVLJLVU7dnownKOHfVI18L4VqldeC71vtOquuGCNENdwWBB+Fbc2QB3NxG0XYX8W19tRB/JGimOwuLXGM1VN72M4KKjzheqj6qAU/W0Y7rGYRN471SBxz8Y0UIoTW0cUil6S+w4ZeTBD1Z6dBWS8qg07C8AEcQHHOUTGP4KR5H8RW0OUBUwjCHh3zsgoPdinL2NnAbjIjjKwTdwH+j9Gj4xKyGlxo4bdEVUovKDJVDr9DQzlKBcOxDKqEZiCbqjuq+pSXrWmrSRv09LGSXHbSnt4Ve14IO6wppO4MwOc0dvzdFzYYJjEXhxHw3tV170P4DTwnLdXivsnDJwtrPX5lZmN4hZ5rTkj7SBAOAVkeN7EIYs98QM9VK18GqtjfgYXObvJV1nBpRYOp7pyRhrpLbnBCqB3WxD448YOPWSI/xkLPI6H2VfZwY1nVfubS+SMuL01hvBwBIxFTtJL8v7WBh4r4xDwAAc+XPF2Mb6McgYXNvuNHQKEn7jcyQcEHmfruDvAc0mB36Ha59PhDj6jgkAQnkvuXfoekw7Axv8BYGSweTzUJwU+gEsfrjujnEEA+rNT3FYGebEtHActtrizcOAB7KR/0cooB3Bb9tDYm00aWzVcs1o6S24QEXgcdyaRFPixPl0tVsv58hvY+mUIayynzQAAAABJRU5ErkJggg==>

[image9]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGcAAAAWCAYAAADdP4KdAAAD30lEQVR4Xu2YWahOURTHlymUJEXKA4kSGTI9GLrCkwfJ9CBjkuHBC0/Ek6LMQpk9SBkekJQhGSJTMkWJZJ7nebb+d+/9Wd+6a5977ue7fHF+9e9+67/XPufsfc+eDlFGRkbGn6KdNjJKhx/aqG46sZ6Ru/FJVqP84hyzWa9Z71kTVFmgNesUuWsdVGWlxFNyzyj1Ki+jIhg107VZIE9Ynyn//s9ZS2TSZNZyEW8ml9hFeOAK64CIL7OOixiUUf6b1VnFpUjomDTc1UYRSLy/Vai9hioOwJOjDPEUEQO8HRiNpYpuaxKYMYpN4v3xNuhCXeG8igPw1vnfTX2Mv5L93i9VdFtjjGYN1GYRSHv/cmaSS5YPEruA9OeI35KNZPuBPuTm8dXkRmFNcuvZUnIjNjCVtYXVV3iS5qzFrPk+Hsf6whofEiLE2qb5puK2rGmsFeTaAIazNpB7lsAY1jbWSOFJ0t6fBpNLXKb82AWkv1P8lqwk2w+MYp0jl9OPtcb7g7zXjHXTe028t8jHAYxOTJ+1WK3I5UxkzaPK14lY2zRXVVzG2k2u7iTWMe+38V5P1ltWDVZ97531OZJU91/I2k7uDemvymIXkP5R8VuCfzR8+TZZIOeW4elrflJeAx93Ex52QrpeDOseGvRNC216rPqWt8/wgJUbBZ2I5D3Ci11A+phyrBwMe/i1dYECOWMND7tECba78j7tfSwPhze8l4ZY2yRJ5SjbaHi6zi7DA1ZuIrqCjgPSj60568n2NcgZYXinlRfOJxLEcqpDfEbEScTaFsDI3KpNAequMjx9zR2GB6zcHJjG1iovVOjt4zc+1sALc3EvHxe6W0POEMPDgVby2PsSzO04HIcp71B+cSKJnUPu+ZNGPeqmWaOxKdAesHLLGUp2YfCwwAK80ToHwOuqYt3B6DicfCsDdYcZnh451nqi46pgtV+SVAZQjqlbe7oe1nPtASs3Bwrqirij9/YKD8DD14TAAu9J8JZ9FTF2KshpKTyLeuTy9AEW3nXlvfO+BPFt1glyC+8mcrupNITOqaMLmA6sWdpUoK6e9qwOP2J4wMrNHSEas76TSwjzOba/mrAdxJt8gfWRXOdrUIYODHPsgPziCuB6D1h3WPfI1cV54ZH3sBUOIw/Phxg+prfu3r9EvxqpFQNT4ENy14Lus17mZSRvw7HGhfrIQ11s9TGyg4ff4IWP4aPODKr4nFr/BFjzYmsMGhk7/KXhgzYyqga+AszVpgf/HHxZKASss9Xxuea/InyUlZ/a4V0jN/UVCqa9jCLRg9yZ6jC5fxTOJ7/DRW1klA7YQf41fgJ0WWrIJnXasQAAAABJRU5ErkJggg==>

[image10]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGEAAAAXCAYAAAAbfSF/AAAC/klEQVR4Xu2aW8hNQRTHlyQPQiI84HsQJaXcFVEeJeUSJbnHu/BEIUkJ8UK5FVJye5EIIfFAKaEknpQnd+Way//frHHWXvt8J+frfMc+8+1f/WvWWjP7tGfNntkz+4h0nF3QPeg3dBQang3X5KaEdpEX0HZjl9TBJMl2Zj3YdluhscYuqYMJ0pgklDiGQh+gB9Al6DC0OlOjwnjJd+ZtaDd0FZpr/COgL9BxaI9U2k3W8h21Wab6QpehT9A0jZFl0HUJv7PN+JPCdqrvYM84ydY5C6009htoCNRd8tey9mKpJIEwdkbL3dQmg0yZ+GsmQ3s3ucUo4p8ElnsYmx3J0bwB+mr8xLabJ/kkDHY2OQF9g16qfkIjY6WUuCBhOnoNLTT+FUYRvyawPMDYF6G70E7ou/ET247Tlk9Cf2eTA9AT40+Weh7xKZKtfwTabGyOVI5oO6UQrjvWni/5JHDqsXa18iiol7EbyWjvaCac13mjUW+z4b98hN5JeGLeQ9PVv0P9n6E+6iO8KU4lD6FZUrn+Agn1+Tv7tQ7XEvoGSrg2bS7qpLfWfQytUl+j4FTK6z7T8n+BN73P+R5JdlSmCKc+Dia+cRUCO6+3Qb9MLDX42swn77QPFIWZ3pEQUyUMtr0+UNL58FWYnb/RB4qCXYxbUf/CWgl1l/hASfPhvoTJWO8DKTAM6mdsHlcUGZ5b8cWDZ10tD2+CO+LZEjZnzyXsN8Zo/KSEV0COvnOqW2ovh3pCB9W+IWFnfF/bNIM2CfuaUz7QKhyS8JrnYYfGJJB16vPwg1CEcY7OCHfS1dp0FtxcvpIwEFoKdhJ3sR5+qKmVBO6UCZ+aCOMTje2PN5oFj1n4Gls4eGL6FDoGnVffUqndSTY5Pgm28yM+CTyB5TFHieQP4Dj/cxHmd+ZaSbDEJPAYhOdA7SXhmoT1hEffm7Lhrg0PythB8Ryfi9gaCdONT8IV6IeEjraxjjwJtGcYu0uzSPKdHaF/jndK8NuP9z4J1WCcfx6wdvLT0R/NjP0oWOlAyAAAAABJRU5ErkJggg==>

[image11]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAALAAAAAXCAYAAACrrsUIAAAAoElEQVR4Xu3XIW6CQRSFUaCIkpAaEkw3wF5YR/dE2AVoVkBIcLUNAlHTBFEFovcXmGdqZ5Jzks/M9ZOZ0QgAAACgVet6AD3Ypnta1QFadki3tKwDtGqaPtMlzcoGzXpL3+mUJmWDZr2n37SvA/Rg+Jg90qYO0JPnTbyrA/Rknq7pmMZlg268pHP6Sq9lg64Mz4qftKgD9OSjHgAAAAD86w/H1xIgUW+VzAAAAABJRU5ErkJggg==>

[image12]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACYAAAAWCAYAAACsR+4DAAACBElEQVR4Xu2VSyhFURSGFwMSyqPIIzMTSVKSEgNRMpBnCRkoQ1FGYmJgLGVASvKKESVixEwxYkAZyGMmA0WZeKzfXue2znLuvfIog/vVf89e/15777PPflyiGP+bRlaCNQ011vhr3lj1rFPWhKnzGGUdWzOZtUeugyNWnL86IuWsW3Jtx0wdOGEtqBh50CyrjjWgPB95YiZJnClxfCgjPMvk73COdadigHoso8ejKmfLc4lVrPwPnlhrxsMnfTaepYDcoM3Gh9dqYr139lUZZFDAEgI07DDeiPiRmCaXk2t8eA8mblfxiyqDwHGqyVVUGb9XfMwmHJfkctKMD08Ptsk6U/GVKq9TwBKCQXKdlBkfM4RfYXzNPIX/YvYr3LMOxPcOVha5gxbIOLnkEuNj38DvMr7GOyQtxg96sSB0Dg4arpIbKVO/JJSqJNAmfq3xLVvkH+Ba4mgvhuUtUjHyU1Q5tMcqvQyhR3xcJdFoYp2Te0nMNtqL5bAOVdxH/vxu/CSK+Z1TGQ60W7Gmwva7a7zQYYI5pSrAtvgaHAjvQvRAzo6KsSVsOw36LTQe7lDdJt0rBH0dxHpT4yQFLRHiRRW/siZVrMmnz5craCB/v9hGIVbJXXx4IgnXiGWDNWy8GXL5F/Ic8lf7sJPSYEKpUo6U9+t0ktv0kcDFC33lPzpGjB/xDocChoOHzSuOAAAAAElFTkSuQmCC>

[image13]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAIUAAAAWCAYAAADuKF/RAAAErElEQVR4Xu2aWch1UxjHHzOZ6jNHvkJkTpFkCJkypWS4+FyhDJHpQoYbCRkvXEhyZQolUxIlGZK4QMbEW6Z8mSNChufXXs/7Puf/rn3OPsc57/eq/aund6//8+y1197r2Wuvtc5r1tPT09Pz/2BrFZaAPVToWV78I+Ut3XYXbdrUrrmraPNc4Xa+iiM4wu1Day70gPgmZbUKI/jM7US3jd22cjvP7Y+BiOlyndvP1txzGOVvclAH1nF7qhwfZAt1vTIfMX0YJS4vx8fawjWfno9wHrLmAYbzguwcwWVuf6cynaFZ2JW3bPAhj0M+L2z9gYjZ8LA11zpJHR150G0j0WadFF+oYJWkyIybFMTrUId2k2jj8KRNlhS3u93htrf4ZkkkxQnq6EjtPmedFL+qYFNMilOsflO/W13vyqRJsSaIpDheHR3Y0e1mFW22SXGW1ds6taR4weqdMWd1vStLkRRruZ3jdovbnUXjm36/2yER5BxqzTzpmqRlIimOU0cHPlChQH2vluMt3A5w28dtf7edI6hwjNsjbqtK+UWrjwTBXyoUppYUP1q9M96zut6VSZOC9vAwP3L7adC9COYbfG44j/jv3NZ227BoPKCv3VaW+O+LrkRS0DnjMqyDXivHjCaUsZfdDiw6SY12dSnfW8rA393KsTIsEZ+xZsK+CJwXqthCNFZ52+p6VyZNikxbJyq1e3iiaLskLVYGSiTFUeoYASslhvIa1Pd6OWZ0+Db5Aj4v2h7Kt4qWwbdSxULtOcyD4yIVW/jK6hW9aws6b+4o082bSZJCiVUQw/8wag8jOjqzX0WDiD1aHYWTVSj8pkKC+t5wO8PtF/EFLH21PZSfEy2j8Rl8cyoGOC9WsYW2OcUnVte7Mo2kONyaOu4SXaklBfMK1fYqGp+YzKik0HoCXqg2OIctgo/LMZ8Q5WAbrHuHUtYXLNjEmra2wbnvqxjgvETFFvie1W56qVcf7JNoPMMz2vWiK8ToufdVNDZ80NqSom1OofXAVW77qpjgnGfLcdu8DWJEZv7E32FLcUaQdVVMcP47KgY4L1WxcJrbNqIRv6KixS7dJIxKCh5qhtgvRWOfBL32lmWI0WvVRoo9i8YOZGbY6uMGayaritat4GdDMZf5nGTOdTtTtGF0uSZJtgj2v3HWJisx29XKuem5VN7Wmpj1kjYuMYnaQB3OD9b48grpVLfHUxmIaZtpZ2r3xFul2pFF05ciYtmzyUSyMKPP8LY+L5rCeXluECuLK5PG7xRob7q9ZM1qiT2PzVNMwAgSq5Q2qOvzLDxqzcSF7U8c/F1ti3874MHz24jC7Jh4HgCV7zTo7gyTL5Is2sHbT91npxhu8NNUDm6z5tq0g7/3DLoXsZk198x1MI7pMIbruD5tYX+CdtEWNOYCJGYsZ0fZtTYI29p832scZk37ow+4DrCSokwb+H0F4gWu2d0lJuDcNtiez9dkad6zxNBp04B6NlXRFka0zLCVTs8aZjurb2tPAh3PJ11hIpyT4nSrb2v3LBN0svhfuNGazuffFgLmVmjxsziwEuxZxvypwhQgAZjrPWb1nejWZWbP8mB7FZYAfssZi38By72FMZoZqTMAAAAASUVORK5CYII=>

[image14]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACoAAAAWCAYAAAC2ew6NAAABcUlEQVR4Xu2Vuy8FURDGJ0goFCI6UelJREmlkxDxailJKLQa/wAFiQKtilaUGpF4lDoVQZBQSoh4fOPM2N1x7r07G4Vif8mXc+abOXPmZjd3iUpK/gUdULM1Ld3QE/QJHUMt2XRhRin0rMYBhRpWr8llmIHWUvE2hUM9Ka8oOkAeag4aaxbzvNyTr0/NQW/odzPPBTGGoAXy9ak5qGWRwqFBm3DwImuRQeugeWgDastUpBihcGDVJhxcQg2y9w46DW1KPCxepxYoy9Au9A4NmFxe+qGlVOwd9Cri7Rvvh3YKBXsSH+XQjtS+yap4B52KePx3WRHPBco51GQ8Tx+um4x4Jxrwo95Kct/oBX3Gr8ZhRNqH93NJaRSu4w+E9U55MyaB/dXq1RvfS6x3JbhuPOKdpYPGJEdd4lV8iR3kHZRfGa6bNT57Fxq0Qh9iPsq6rsmCvEJ30LXoAVrJVCTwo9XaW+gZmqBwhj3+IJWUlPwFXwu7fVaGvChzAAAAAElFTkSuQmCC>

[image15]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACoAAAAWCAYAAAC2ew6NAAABkElEQVR4Xu2VTysGURTGT0opYsHCgigbH8A3sLCzELbEysIH8Bns2CBrC6FYEAspKX9K2ZKFEMpCyobEeTr3znvnzJ2Z+14bi/nV0zvnueeZOfPvHaKKin9BN6tFm0X0sH60WSe9rGeS/eyklzIckvRBA2qtEBuKZYn15dRbrH2nzqOuQQ9YHxQ/6CBls6jflOcjeNAu1jbrlbIHCwW5G+V1qjqP4EHtcLGDtpLkFk09xGqsLZdiB21gzbKWWR2pDmaT5K0DsYPOkOTmWBusZtYR69PpKQLZSdaKqYeN12cb2knePEvsoLgCyOks6ivl+UDfncfbdQsXPehJgNZZ8yS5NYklfBu/DPRMeLxTbOAq9KfXMoOGgoMgN638d+OXgZ5xj3eGjT3WsRIWIWyvmkAIbSQ5PKsuoX936BnxeOfKS7CDxoCcPrnQ/aFn1ONdKC8hdMc+piibRY0PQRFN5L8b8K6VR5ck3+d7I2znnk0BCyQHuDW/Y+nlDLi1TyTHfCR5VJB5Md5DrbWiouJP/AJUmYBMM40/2AAAAABJRU5ErkJggg==>

[image16]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADQAAAAWCAYAAACPHL/WAAAAmUlEQVR4XmNgGAWjYBSMAizAFYj/A3EWusRQB9YMEI91o0sMdaAKxD+BeBm6xFAHIkD8HogPoUsMdcABxPeB+BoQM6PJDVkgBsQfgHgHusRQA+pA/AuIF6JLDDVgxwAp8drQJYYaiGQYJnVSLgPEI37oEkMRNACxEbrgKBgFtAPSQOxNJLaA6hnUANTEMScSa0L1jIJRQAYAAAVHF9IgFgMqAAAAAElFTkSuQmCC>

[image17]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADwAAAAWCAYAAACcy/8iAAACbklEQVR4Xu2Wy6tNURzHfx555FFcSR7dm0e4pRsSyoSRoYH3wKOUkT9ArrqzKxO3mIiJMpEkI6WYIAMlipIMlBJFUYQ8v9+91jpnne9e++x1ZHJrf+rb2eu7fuvxW3udtbZZQ0PDOGACtFTNbvRDf9T0jJir+wUNd1ZlM8dcHyegQ9B+aC+0x2tqK9LsFPQD+gldivwqPpjru2r+Saoa3Ia2RWVO+FNUzuWAtcdIabKPY9/r/HNfVF/HSsuLK7gFfbFyg4nQO/EI4xapWcNV6CA0BK2AlpnbgtehfT5mo7nxZvky2WBuvEeRl2K5leefZDF0A3pv5QY7Eh6hN6BmDV/VAEug51GZW5l9P408kvOWB6w+piAEpRKe4T2Kb4QM+vL/INUPd8Js8XIS5uKFmGnQSWgMmtKKANfMBZJUwoRbLgzIbfW5s/qfeQxtVTPBZnNjcyG6wb8Y43ZBx7w36r0CHgh3QsGqEybcYiFpak1ndc9MsuqxFMb9VjNBSPiK+K1xdMCqhHmYcdXIC2snPRNaC93PkPIQeqVmAu5AXoU5hIT7xS9yOg+tkopUwpehe+JtMRf3TPxeYPvTagpHoY9qdiEkPF/8Iqeb0F1ReHN8vhgFh8MqhgeCLk4uC8213a4VEZusvAPqxuObZcxc8SvbhYTV2ykeOQK9VDOTM+b65X2cYgH0RE0rz00J9/A88SvbpRLenfAIvY7jvgd477J96ruXX1thHqoHUVyK9ebiVotfmj+vmrfQay8+81AJHDbXiNcRv21Tq9gLZ831MV0rwAUrJxp0PIpTvkFvzM2fv9+hc9bOq6GhoWH88BdbV72BV8Bk5wAAAABJRU5ErkJggg==>

[image18]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACUAAAAZCAYAAAC2JufVAAABvklEQVR4Xu2VzSsGURTGj69ISoqF8lEWyMpaFj42dkpWxD+ghEJCFsjGykJJkbKRvbL2sbFQCiU2Yik2PhJxnvfcGeeed2asLNT86mk6z3nufe/MvPcOUUrK3zDK2mE1ubqRtc0aCRPCE2uAVcYqZfWyHr1EMrusL9YFq9j0slggCWudegnBZqAqLxFNAUm2xtV5rq4MExHMsVZYW6wZkkFRYKIl1iqr0/SSOGDdGW+ZZL5YsJB2a0aQOEkCGIcb0bQ4P5Zp+rtFBa8KN66pdX6P8UOmWIskoU13XfMSAvwr1jnrmPXByvcS2TSTjBszfoXzJ40fggH7xsOA+QivUNV7zkuigyQzbHzsYPjrxk8EA377QRwdyMzahqKeJGOPl3Ln2xsPybEG80nZi7K7Mpckc2l8DeZGBn8RTbXz+40fguZDhKcXde3qIuWVOO9QeVEgE7f7Ys8qNMcjPL2oW9azqkEXSaZPeVj0kKoBnvqZ8SYo+014vJDshoA2kgENysPjvlE1eGO9Gi+4meCTBVqdp0GNAzsRvL5gQqjOb2cYJOndu+uR387QzTqxJv08GXxj31kbfjslJSXl//ANbLZz0gKezSYAAAAASUVORK5CYII=>

[image19]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAB8AAAAZCAYAAADJ9/UkAAABlUlEQVR4Xu2UvyuFYRTHjx9hUJIwIAaDRaRMBgODlUwKs7/AxGqlMCjZTAaTQTIIUQxISihkxeBXUpzvPee5nfe8zy37fT/17e37Pd/3ufd97vNeooxipoK1x/plbbtZ4JU1zqpl1bBGWS+JhtDOOiZZa8fNUvSQFLEg6FXvQebVnGgQ9Wse6HY+BYZnkewiks2xllkDbhZAZ8pl36wjl+WoJ7lhxeWnmlu89zSQdHC14GeM3jtJMph3+a7mFu89sxTvrFE8p1aKP/m95nUmg79mXbIOWT+scjPf1I5nieJ5DgzOIxmEw2ezSuO3NAuEt8WzQJI3+QHA4cEQrxuYJjlsyEpDKUIHSWdG/bp6zyJJbncpQSPJwcCWdrLuKL1QmfP4YuhcqS/0m69SPC9I2PbAjfoqk1Vrtq++T/2/TzvwHxSyYeMfWO/GgyGS3pjJ4EeMB2+sZ5flwQ0fxp9QutzCunXZF+vTZXhKvAWBEpL120yWoIuk8KhXnNoYEyTzJ70eJMd58G+JXdog6Q0mxxkZGcXCHyHaeHAEbMyfAAAAAElFTkSuQmCC>

[image20]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACUAAAAZCAYAAAC2JufVAAABi0lEQVR4Xu2VvyuFYRTHD1KyKZKEzYDBLIMYbJQsN5sNERIpm2wmxaIMFvkxWCRWoyyKf4AFg1GJOKdznuu533se910M6v3Ut3ufzznvc5/3fe/7vEQ5OX/PEmcKZcQl54vzypmEWiWOSY+959RDrYwDzjvpAZLp0nIRqdXa94KNn3/KSeQY6W23cY2NW4odFUgt6pxzCu6MtH8EPHLFeQS3SXpsJlKL+iCtjUeu29xT5DykZwdcn/lMpBbVytkHN0DafwM+JtyqNfAd5sfAu6QW5XFB2t+DhYhe0p5F8E3mV8C7SOMMSodwBa6xAAyS9s2BbzC/C95FGmdROrzR77ct0Ek65zz4RvPr4F28s0LuOEcoE1SRzrkKvs38BHgX76xiTjgb4B5gjMicqacv014ljQsojWUq3+2bOdvRuI7K/5OfnFtwMpf8VkXCfZaNDRkirXkZjvqC64pcv7kYGW+BK0HeSS+ku67cCvmUDVFePQFcSJzqqG+U/CcyXJlD0nn3Sss5OTk5/4dvZDRtHlpdTQ0AAAAASUVORK5CYII=>

[image21]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAB8AAAAZCAYAAADJ9/UkAAABS0lEQVR4Xu2UzypAQRTGj7KxkVI2iIWFpbK0sPEEFl7AhofgBawUC0V2VhQrhSxI+VOixAPYWMjCvyTF+cyMvnvuudRsza++7vm+MzOn6d6uSKEQ6FN92jAyo3pUvaomTS8xoDqRcMae6f0JNnnDr1W75K9UR+TBqFT3Dhn/KzuqF6lvaHcygKzD+Gny4F11bLIaPaot1b3UB104GUC2HOuu6PFkcCFvb4W0wBve9Co4n6WaWRU//2FD1Rvr3OGbVDOL4uffdKr2yecOP6CamZeQd9sGsBtyh69RzSxIyFttY0k1aLLc4U3vfEX8XLZVh0bpQNTpS36KmQXZTaxHos/62hPeLSecDCAbNn6cPHhWPZisEW84QDZFfi5mDG75Qb5Fwpp+ylzOVXeq2yjUZ9Rvk3DQqepS9SbhcAt6+EuuS1g/Vm0XCoX/whd2J3sIDhWwBAAAAABJRU5ErkJggg==>

[image22]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACUAAAAZCAYAAAC2JufVAAABjElEQVR4Xu2VvStHYRTHj7dISopBedkkk1kmFpuSidgRIZFiMlhMBouySnb/AH6LTaHE4mWQgUUk4hzn3J/n+f6e3703Maj7qW+353POc3vu23OJMjL+njnOGErjkTPCqePUcgY5D15HPLucD84ppxpqBWxzXkknSMb9cp6o7qbJ6whTQdrbYuMyGzfmOxJIWtQqZ4PTC7U49jk34NZIz5eKpEX9BJknF+LSZT4Vv72o6FEtgW81PwA+SNKizjknnBznjVPudRTSSTpvFnyD+QXwQaRxAqUhtUpnvGcujh7Sninw8gWL3wQfRBonURahnbR/GQsObaQ90+Drza+ADxK6qgh5P1xKSfvPwLuUkPYsgm82Pww+SOiqhAvSWpXjaswdOC6E9BT7+lLtVdI4g5K54jyB6yPtH3KcLBrfyXfOMbh50rmJRM9ZNjZEbvcluBfOMziZL+lwXLc5Fxmvg/OQf9I96a57bcc70l+PyyjpyW7teOiXv+jnHKGk7zuzQ3reLb+ckZGR8X/4BI+AaRM0mepnAAAAAElFTkSuQmCC>

[image23]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAB8AAAAZCAYAAADJ9/UkAAABmElEQVR4Xu2UvStGYRjGL1+Rj2RgQQwSZbAYZDAwKJssFFkN/gRkMitsMohSBikGySDEIpKUWBSjjyKScN/vfT+n59zneZXZ+dXVOdd1Xz3nfZ/zAaT8d8pIN6Rv0omZMU+kIVIFqZzUT3qMNYQG0jFknR0zCzICKReonyQ9R1OB51Y1sQbQqbmj1fgElZBCkZe5xX3YT5PmSV1m5uDOqMk+SEcmiwhdqNh4xnYsVZAOH322NQ/Cg3M9b4fc+xBZF1AmEO4sIpyjGTJYJp2RSkizmlk4uyJdkA5Jn6R8b76uHcscwjkGEN72L9KbybhT6PktzRx7xjtmIHm1HfTq4N7ku5r/RhOkM65+Rb3F7aS/SxnqdLBk8g3N27wszztnciGdS/XZ7vkCwnkGHqyabFPzRvXX6v3XsVSzffUd6v/8tPPiPqeaO25Jr55neiCdQS9j3+d55oX0YLKIFiR/Gfspz9dCPr0+70g+lPwv+S1w5EDWqveyBGOQkvu285fMMgyZ3enxID6O4FeWd2kN0uuOj1NSUv4LP/SEd3zEh1lZAAAAAElFTkSuQmCC>

[image24]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABoAAAAZCAYAAAAv3j5gAAABL0lEQVR4Xu2UsUoDQRCGfwnaBtJEUtoJgZDOJoiVjYWN76BtsLNLlQcxvSBYic+gkICNESxEQdBUwUKTmZtbsjv+uTQ2gfvgh+w3M7sJuVugZJ2oSV4lM8lYUk3LhRxIHmGzA1dL2IIdEtiADbUjt4yu5Ddan8JmKV9eCE3Jj5cE3XSXuL5zGVo4c66V+yKOwXu+wT0+YYXbyOmv7ERrxh34hs/gHhVYIUQPOUo6ONrHNhyB+4wG0sO0eRWh1/MA7nEomeaf97HYQAeKCK+DZwjuqXwB9zHL/qMnEH/CZI76PS8jLsBn6VOnL+UfmeO9fqm6c9qjt4p3185laKHnnK7vo3W4Lfzhb7DHObAN69mMXMIE1hDurMu0nHElOfdS+JC8S25gsztpuaSk5D+YA5jYVy6lwTFLAAAAAElFTkSuQmCC>

[image25]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAB8AAAAZCAYAAADJ9/UkAAABeklEQVR4Xu2UvytHURjGHz+KUDKwoCSD0WagDAxmmRS7P4LFYJYfmwzKZDAZZBJipKTEomzC4FcS3sd7zu297z1fxep+6une53nfc873nu+5Fyj5zwyKbkWfoiNRdb78zYNoUtQiahaNi+5zHUqP6Bg6166rFVgUrRj/DB3YbTLCzKsj1wEMhTzS53wBFvsTmR9EPw/9ocOuFmHPtMveoLtZoBGVF0plP9EG7eHVshPyJHOiAZf9ZfFZpHvWkM4rwuaPRHYhOhMdit5Ftaa+FXo8y0jnSU6hzQ0uZ1Zn/HbIInvORxagebsveHjw2NjqCwl6ob0zwW8E71mC5naXCvD99U9nqXGe3wL2nwdf6T9fRTrPiBNZ1s39JbReb7KmkO0Hz0NL/6vTTvzhIja7Fj0ZT0ahk06YjH7MePIounNZBj8CHJRSpFN0ZTx5Fb24jE/JtyBSBZ2ny2QZPIF+wSg/8VTIb8L1IF/OOIHu0ia0byRfLikp+S98AZGYdPf1oNB5AAAAAElFTkSuQmCC>

[image26]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEcAAAAWCAYAAACSYoFNAAADKUlEQVR4Xu2XS8iNQRjHH3ciEcolckshEimFksvKJeS2UHIpITayYoPsEAvlUlZSSCGUWLDDwpKN3OUucgu5PP/meb4z7//MvEffd/ro8/3q3znzf2bmzDzvvDNzRFpppaUzgY3moq1qBJv/EO1VJ9isMx9Vndl8p/plKuO1VOq5thVqiHyKYtDeYrjRnFR1ZLPOYLzJB7BMaifHqZXIlaqrbDaRst+rB7ulZF7zJRNIcERC3a0cMN6rOrHZBIaqdrJZZzCfL/bZjWIyxwJ/QhspybLk/cZyl406g/lgy1gqYexnimGR2RZwpqnGqcaqpka+81NC/Q7kb5DqFTVPtUXCisPGP1C1Q3VY1S6ql+M7lTGezapDqh4S+lyt2qfqHtVbrzouYS5l7FfNsu/Jh87JeWTlz6o9ke+skRA/RX5VxxIm8kBCDBv2KvM3moeE5lgo4YnGLFfdktB2uoQkAzwEeH1V983rY15qDk485g9WRtIb4OS8VU2Jyik4y1ieOA5T9JZQdzT518zPraCvbESg3cOExw8IfbDnYNW9iMoLJNS9GHmF5KCz/lEsxzMJbYZZ+ahqRiVcAMsddYeQj+MZ/jHyHazgHGi3IuHdJg8HRC45B6T6tatKsCfHhQ5rMUZC3XtWzg0AdJV0cgB8rFRmu2oUmxFotyTh3STP72cp4jmzenmleOUMsu+bPFiCd9RPdZ1iMbnk4HWCjz2EyU3IQRx7Ens3yHtpPoPfRozxa81lN/xdc85aGdf2Ms5LqPdN1ZNiMbnk4GSDP558vG4XyGPQblHC45XzynwGp91MNg3Ub2iDoxAFbKoOyj+icgpc9godZfDk4KLl+H5zJ/Kc06oubEbgPxDariMfHt+L/C9NzEjzcMVI0TAnNH6qeixhkz0o4SKE7/CeS1hqOdAJrt9leHJw28Xp4D+Ou0gKnkwMVoaPDePG+BdL6BfeE6nsYdhvUIaPV2iihFWO9vAxt0tWFwxQvZFKPpoFXMkxYX6tUgxW7WKzJYOd31dOLfgobtGsVZ2TkJwrVi4Dy/6/Adf6yapJ9jm3GC6A/018PLdiDGfjb/IbirHsisY1KusAAAAASUVORK5CYII=>