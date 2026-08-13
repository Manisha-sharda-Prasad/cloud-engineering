# Phase 9: Human-Centered AI
**Duration:** Weeks 21–22 (2 Weeks)  
**Target WGU Course:** Human Centered AI (3 CUs)

---

## 1. Official WGU Competencies Covered
- [ ] Conduct ethical analysis of artificial intelligence systems and applications.
- [ ] Apply human-centered design principles to AI interface and system interaction.
- [ ] Implement mechanisms for continuous monitoring of AI impact on humans.
- [ ] Design robust human oversight and governance control frameworks for AI systems.

---

## 2. Comprehensive Study Topics

### 9.1 Human-Centered Design (HCD) for AI
- **Principles:** Prioritizing human agency, usability, accessibility, and mental models in AI interaction.
- **Interaction Paradigms:**
  - *AI as Automated Agent:* Full autonomy (Low human control).
  - *AI as Decision Support:* Recommender systems (Shared control).
  - *AI as Tool/Assistant:* User-initiated execution (High human control).

### 9.2 Ethics, Algorithmic Bias, & Fairness
- **Sources of AI Bias:**
  - *Historical Bias:* Existing societal disparities reflected in training data.
  - *Sampling Bias:* Non-representative data collection.
  - *Algorithmic Bias:* Objective functions amplifying disparities.
- **Fairness Metrics:** Demographic Parity, Equalized Odds, Equal Opportunity.
- **AI Safety & Privacy:** Data minimization, differential privacy, protection against unintended outcomes.

### 9.3 Explainability & Interpretability (XAI)
- **Black-Box Dilemma:** Deep neural networks vs. interpretable models (Decision Trees, Linear Models).
- **Explainable AI (XAI) Tools:**
  - **SHAP (SHapley Additive exPlanations):** Game-theoretic feature importance calculation.
  - **LIME (Local Interpretable Model-agnostic Explanations):** Local surrogate approximations.
- Generating human-understandable justifications for AI predictions (e.g., "Loan denied due to Debt-to-Income ratio > 45%").

### 9.4 Human Oversight & Monitoring Architecture
- **Oversight Frameworks:**
  - **Human-in-the-Loop (HITL):** Human approval required before system executes action.
  - **Human-on-the-Loop (HOTL):** System executes automatically, but human monitors and can intervene.
  - **Human-in-Command (HIC):** Human sets overarching rules and constraints; can revoke operational command.
- **Continuous Monitoring:** Tracking Data Drift, Concept Drift, Model Decay, and Human Feedback Loops.

---

## 3. Human Oversight Taxonomy

```
+-------------------------------------------------------------------------+
|                         HUMAN OVERSIGHT SPECTRUM                        |
+----------------------------+-----------------------+--------------------+
| Human-in-the-Loop (HITL)   | Human-on-the-Loop     | Human-in-Command   |
|                            | (HOTL)                | (HIC)              |
+----------------------------+-----------------------+--------------------+
| Human MUST approve every   | AI acts automatically;| Human sets policy  |
| action (e.g., Medical      | human monitors real-  | constraints & emergency|
| diagnosis recommendations)| time override dashboard| shutdown switches. |
+----------------------------+-----------------------+--------------------+
```

---

## 4. Phase Deliverable
**Project:** Human-Centered AI Governance & Ethics Blueprint  
**Requirement:** Expand the ML project from Phase 8 into a Human-Centered System:
1. Conduct an **Ethical Risk & Algorithmic Bias Assessment** identifying potential data biases.
2. Formulate an **Explainability (XAI) Strategy** implementing SHAP/LIME concepts for end users.
3. Design a **Human Oversight Architecture (HITL/HOTL)** specifying operational intervention points.
4. Draft a **Continuous AI Safety & Monitoring Plan** tracking model drift and user feedback loops.

---

## 5. Weekly Schedule & Action Plan

```
Week 21: Human-Centered Design, Ethics, & Algorithmic Bias
├── Mon-Tue: Principles of Human-Centered AI; user autonomy vs automation.
├── Wed-Thu: AI ethics frameworks; sources of bias (historical, sampling, algorithmic).
└── Fri-Sun: Quantitative fairness metrics (Demographic Parity, Equalized Odds).

Week 22: Explainability (XAI), Human Oversight, & Monitoring
├── Mon-Tue: Black-box vs interpretable models; SHAP and LIME methodologies.
├── Wed-Thu: Human-in-the-Loop (HITL) vs Human-on-the-Loop (HOTL) architecture.
└── Fri-Sun: Complete Phase Deliverable (HCAI Governance & Ethics Blueprint).
```

---

## 6. WGU Competency Verification Checklist
- [ ] Can identify historical and sampling biases within a given dataset.
- [ ] Can explain how SHAP/LIME values provide model explainability.
- [ ] Can design a Human-in-the-Loop oversight workflow for high-risk AI decisions.
