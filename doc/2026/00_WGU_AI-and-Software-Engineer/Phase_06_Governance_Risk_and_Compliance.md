# Phase 6: Governance, Risk & Compliance (GRC)
**Duration:** Week 14 (1 Week)  
**Target WGU Course:** Governance, Risk, and Compliance (2 CUs)

---

## 1. Official WGU Competencies Covered
- [ ] Evaluate compliance and regulatory requirements applicable to software products.
- [ ] Implement data classification and asset prioritization strategies.
- [ ] Select and map security and privacy controls to mitigate identified organizational risks.
- [ ] Conduct security audits and formulate structured remediation plans.
- [ ] Evaluate security strategies against organizational objectives and regulatory requirements.

---

## 2. Comprehensive Study Topics

### 6.1 IT Governance & Regulatory Frameworks
- **IT Governance:** Alignment of IT assets and strategy with enterprise operational goals.
- **Industry Frameworks:**
  - **NIST Cybersecurity Framework (CSF):** Identify, Protect, Detect, Respond, Recover.
  - **ISO/IEC 27001:** Information Security Management System (ISMS) standard.
  - **COBIT:** Enterprise IT governance framework.
  - **SOC 2 (Type I & Type II):** Trust Services Criteria (Security, Availability, Processing Integrity, Confidentiality, Privacy).
- **Regulatory Landscape:**
  - **GDPR / CCPA:** Data privacy, right to be forgotten, explicit consent.
  - **HIPAA:** Protected Health Information (PHI) safeguards.
  - **PCI-DSS:** Credit card data handling and storage standard.

### 6.2 Risk Management & Data Classification
- **Risk Taxonomy:**
  $$	ext{Risk} = 	ext{Threat} 	imes 	ext{Vulnerability} 	imes 	ext{Impact}$$
- **Risk Treatment Options:** Accept, Avoid, Mitigate (Apply controls), Transfer (Insurance/Third-party).
- **Data Classification Tiers:**
  1. *Public:* No harm if disclosed.
  2. *Internal:* Low sensitivity corporate data.
  3. *Confidential:* Sensitive business data, intellectual property.
  4. *Restricted / Sensitive:* PII, PHI, PCI, authentication credentials.

### 6.3 Security Controls & Audit Remediation
- **Control Categories:** Preventive, Detective, Corrective, Administrative, Technical, Physical.
- **Audit Workflow:** Evidence Gathering $ightarrow$ Control Testing $ightarrow$ Gap Analysis $ightarrow$ Finding Generation $ightarrow$ Remediation Action Plan (CAPA).

---

## 3. Remediation Matrix Format

| Audit Finding | Risk Severity | Impacted Regulation | Root Cause | Corrective Remediation Action | Owner | Target Date |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Database backups unencrypted at rest | High | SOC 2 / HIPAA | Default cloud setting not enforced | Enable KMS AWS-KMS AES-256 encryption on RDS | DevOps Lead | 7 Days |
| Customer PII logged in plain text | Critical | GDPR | Unfiltered logging in API layer | Implement log sanitization middleware | Backend Lead | 48 Hours |

---

## 4. Phase Deliverable
**Project:** Enterprise Risk Assessment & Remediation Strategy  
**Requirement:** Perform a full GRC audit for a target application:
1. Data Classification Schedule mapping all application data entities to privacy tiers.
2. Formal Threat & Risk Matrix identifying 5 critical technical/business risks.
3. Regulatory Compliance Mapping (GDPR/SOC2/HIPAA) against application capabilities.
4. Formal **Audit Remediation Plan** addressing simulated findings with clear owners and verification criteria.

---

## 5. Weekly Schedule & Action Plan

```
Week 14: IT Governance, Risk Management, Frameworks, & Compliance Audit
├── Mon: Governance principles, NIST CSF, ISO 27001, SOC 2, GDPR, HIPAA.
├── Tue: Risk assessment methodologies, quantitative vs. qualitative risk scoring.
├── Wed: Data classification tiers, preventive/detective/corrective controls mapping.
├── Thu: Audit processes, finding identification, root cause analysis techniques.
└── Fri-Sun: Complete Phase Deliverable (Risk Assessment & Remediation Plan).
```

---

## 6. WGU Competency Verification Checklist
- [ ] Can calculate risk priority based on Likelihood and Impact scores.
- [ ] Can map GDPR and SOC 2 requirements to explicit technical controls.
- [ ] Can construct an Audit Remediation Plan with root cause and corrective actions.
