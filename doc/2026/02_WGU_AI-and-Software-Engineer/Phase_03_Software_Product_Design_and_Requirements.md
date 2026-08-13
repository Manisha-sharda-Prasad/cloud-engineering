# Phase 3: Software Product Design & Requirements
**Duration:** Weeks 6–7 (2 Weeks)  
**Target WGU Course:** Software Product Design and Requirement Engineering (3 CUs)

---

## 1. Official WGU Competencies Covered
- [ ] Manage requirement changes and evaluate their impact on overall software design.
- [ ] Design and conduct usability testing to validate software user experience.
- [ ] Identify, categorize, and document distinct requirement types.
- [ ] Elicit stakeholder needs and constraints through structured requirements engineering.
- [ ] Translate business requirements into technical software design models.

---

## 2. Comprehensive Study Topics

### 3.1 Product vs. Project Dynamics
- **Product Management:** Long-term vision, continuous customer value creation, lifecycle management.
- **Project Management:** Time-bound execution, deliverable focus, budget and schedule management.
- **Stakeholder Analysis:** Mapping internal/external stakeholders, power-interest grid, constraints identification.

### 3.2 Requirements Classification
- **Business Requirements:** High-level goals of the organization (e.g., "Increase conversion rate by 15%").
- **User Requirements:** Goal-oriented tasks users must perform (e.g., "User wants to download monthly invoice").
- **Functional Requirements:** Specific system behaviors and functions (e.g., "System shall generate a downloadable PDF upon clicking 'Download'").
- **Non-Functional Requirements (NFRs / Quality Attributes):**
  - *Performance:* Response time < 200ms.
  - *Availability:* 99.99% uptime.
  - *Security:* TLS 1.3 encryption for data in transit; AES-256 for data at rest.
  - *Scalability:* Support 10,000 concurrent active users.
- **Constraints & Assumptions:** Regulatory restrictions, technology stack limitations, fixed budgets.

### 3.3 Elicitation & Documentation Artifacts
- **Elicitation Methods:** Stakeholder interviews, questionnaires, job shadowing, prototyping, workshops.
- **User Stories:** `As a <role>, I want <goal/feature>, So that <benefit/reason>`.
  - **INVEST Criteria:** Independent, Negotiable, Valuable, Estimable, Small, Testable.
- **Acceptance Criteria:** Given-When-Then format.
- **Software Requirements Specification (SRS):** IEEE 830 / ISO/IEC/IEEE 29148 standards structure.
- **Requirement Traceability Matrix (RTM):** Mapping requirements to architecture, code, and test cases.

### 3.4 Requirement Change & Impact Analysis
- **Change Management Workflow:**
  $$	ext{Change Request} ightarrow 	ext{Impact Analysis} ightarrow 	ext{CCB Review} ightarrow 	ext{Architecture/Design Update} ightarrow 	ext{Cost/Schedule Adjustment} ightarrow 	ext{Implementation \& Testing}$$
- **Evaluating Ripple Effects:** Assessing how modified functional requirements affect existing NFRs and database schemas.

### 3.5 Usability Testing & Human-Centered UX
- Usability goals: Learnability, Efficiency, Memorability, Errors, Satisfaction (LEMES).
- Test scenario creation, task completion rate metrics, usability feedback iteration.

---

## 3. Requirement Breakdown Example

```
[Business Requirement] 
└── Enable seamless subscription management to reduce churn by 10%.
    ├── [User Requirement] 
    │   └── Customer wants to pause their subscription without cancelling.
    │       ├── [Functional Requirement]
    │       │   └── System shall provide a 'Pause Subscription' option (1 to 3 months duration).
    │       └── [Non-Functional Requirement]
    │           └── Subscription status change must process in under 1.5 seconds.
```

---

## 4. Phase Deliverable
**Project:** Software Requirements Specification (SRS) & Impact Analysis Report  
**Requirement:** Produce a production-grade SRS for a cloud software product, containing:
1. Executive Summary & Business Objectives.
2. Stakeholder Matrix & Power/Interest Grid.
3. Functional Requirements (minimum 10) with Given-When-Then Acceptance Criteria.
4. Non-Functional Requirements categorized by Reliability, Security, and Scalability.
5. Simulated **Change Request Scenario**: Document an incoming requirement change, run an Impact Analysis, and update the architectural design downstream.

---

## 5. Weekly Schedule & Action Plan

```
Week 6: Requirements Elicitation, Taxonomy, & User Stories
├── Mon-Tue: Stakeholder analysis, business vs. user vs. functional/non-functional requirements.
├── Wed-Thu: Writing user stories (INVEST framework) and Given-When-Then acceptance criteria.
└── Fri-Sun: Elicitation techniques, requirement prioritization frameworks (MoSCoW, RICE).

Week 7: SRS Authoring, Change Management, & Usability Testing
├── Mon-Tue: Writing an IEEE standard Software Requirements Specification (SRS).
├── Wed-Thu: Change control workflows, Requirement Traceability Matrix (RTM), impact analysis.
└── Fri-Sun: Usability testing principles, complete Phase Deliverable SRS document.
```

---

## 6. WGU Competency Verification Checklist
- [ ] Can categorize any requirement into Business, Functional, or Non-Functional.
- [ ] Can write complete User Stories with INVEST principles and explicit Acceptance Criteria.
- [ ] Can trace a requirement from business goal to test case via an RTM.
- [ ] Can execute an impact analysis for a late-stage requirement modification.
