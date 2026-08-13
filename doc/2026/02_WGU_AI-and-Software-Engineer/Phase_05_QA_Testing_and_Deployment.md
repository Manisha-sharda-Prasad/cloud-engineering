# Phase 5: QA, Testing & Deployment
**Duration:** Weeks 11–13 (3 Weeks)  
**Target WGU Course:** Software Quality Assurance and Deployment (4 CUs)

---

## 1. Official WGU Competencies Covered
- [ ] Evaluate software quality attributes using established quality models and metrics.
- [ ] Select and apply appropriate software quality assurance methods and testing levels.
- [ ] Implement automated testing suites and construct comprehensive test cases.
- [ ] Build CI/CD automation pipelines for continuous build, test, and release.
- [ ] Evaluate and select deployment, rollback, disaster recovery, and production monitoring strategies.

---

## 2. Comprehensive Study Topics

### 5.1 Software Quality & Testing Levels
- **QA vs. QC vs. Testing:** Prevention (QA) vs. Detection (QC) vs. Execution (Testing).
- **Testing Pyramid:** Unit Tests (Base, high volume) $ightarrow$ Integration Tests $ightarrow$ System Tests $ightarrow$ End-to-End (E2E) / UI Tests (Apex, low volume).
- **Testing Types:** Functional, Regression, Smoke, Sanity, Performance (Load, Stress, Endurance), Security testing.

### 5.2 Test Design Techniques & Automation
- **Black-Box Techniques:** Boundary Value Analysis (BVA), Equivalence Partitioning (EP), Decision Table Testing.
- **White-Box Techniques:** Statement Coverage, Branch Coverage, Path Coverage.
- **Automated Testing in Python (`pytest`):**
  - Fixtures (`@pytest.fixture`), Test Parameterization (`@pytest.mark.parametrize`).
  - Mocking & Stubbing (`unittest.mock`, `mocker`).
  - Code Coverage evaluation using `pytest-cov`.

### 5.3 Quality Metrics & Quality Models
- **ISO/IEC 25010 Quality Model:** Functional Suitability, Performance Efficiency, Compatibility, Usability, Reliability, Security, Maintainability, Portability.
- **Engineering Metrics:**
  - Defect Density: $rac{	ext{Total Defects}}{	ext{Size (KLOC or Points)}}$
  - Code Coverage Target (% of codebase executed by tests).
  - Defect Escape Rate (Bugs found in production vs. staging).

### 5.4 CI/CD, Deployment, & Rollback Strategies
- **CI/CD Pipeline Stages:** Source Commit $ightarrow$ Automated Build $ightarrow$ Unit/Integration Tests $ightarrow$ Artifact Packaging $ightarrow$ Staging Deployment $ightarrow$ E2E Testing $ightarrow$ Production Deployment.
- **GitHub Actions Configuration:** Workflows, jobs, steps, runners, secrets management.
- **Deployment Strategies:**
  - *Recreate:* Shutdown old, launch new (Downtime required).
  - *Rolling:* Incrementally replace instances (No downtime, mixed versions active).
  - *Blue/Green:* Identical parallel environments; instant router switch (Zero downtime, fast rollback, double cost).
  - *Canary:* Release to small subset of users (e.g., 5%) before full rollout.
- **Rollback Mechanics:** Automated rollback triggers based on error rate thresholds; database migration rollback strategies (up/down scripts).

### 5.5 Observability, Monitoring, & Disaster Recovery
- **3 Pillars of Observability:** Logs (event records), Metrics (numeric time-series data), Traces (request path through services).
- **Disaster Recovery Metrics:**
  - **RTO (Recovery Time Objective):** Maximum acceptable duration of downtime.
  - **RPO (Recovery Point Objective):** Maximum acceptable duration of data loss measured in time.

---

## 3. Deployment Strategy Comparison

| Strategy | Downtime | Zero-Downtime Rollback | Infrastructure Cost | Risk Level |
| :--- | :--- | :--- | :--- | :--- |
| **Recreate** | Yes | Slow | Low | High |
| **Rolling** | No | Moderate | Low-Medium | Medium |
| **Blue/Green**| No | Instant | High (2x capacity) | Low |
| **Canary** | No | Instant (for target group)| Medium | Lowest |

---

## 4. Phase Deliverable
**Project:** CI/CD Pipeline, Automated Test Suite, & Operations Playbook  
**Requirement:** Using the architecture from Phase 4:
1. Build a Python test suite using `pytest` achieving >85% code coverage (unit tests, mock integration tests).
2. Write a production GitHub Actions workflow file (`.github/workflows/deploy.yml`) executing testing, linting, and simulated deployment.
3. Author a **Deployment & Disaster Recovery Playbook**: Document Blue/Green deployment steps, automated rollback conditions, and RTO/RPO target analysis.

---

## 5. Weekly Schedule & Action Plan

```
Week 11: Testing Levels, Test Design, & Pytest Automation
├── Mon-Tue: Testing pyramid, Equivalence Partitioning, Boundary Value Analysis.
├── Wed-Thu: Python `pytest` framework, assertions, fixtures, parameterization.
└── Fri-Sun: Mocking external APIs/databases with `unittest.mock`; test coverage analysis.

Week 12: Quality Metrics, CI/CD Pipelines, & GitHub Actions
├── Mon-Tue: Quality metrics (defect density, code coverage, escape rates), ISO 25010.
├── Wed-Thu: CI/CD core mechanics; GitHub Actions workflow syntax, jobs, secrets.
└── Fri-Sun: Construct pipeline running automated test suite on every git push.

Week 13: Deployment Strategies, Observability, & Disaster Recovery
├── Mon-Tue: Recreate, Rolling, Blue/Green, Canary deployment mechanics.
├── Wed-Thu: Observability (Logs, Metrics, Traces), RTO, RPO, disaster recovery planning.
└── Fri-Sun: Complete Phase Deliverable (Test Suite + CI/CD Workflow + DR Playbook).
```

---

## 6. WGU Competency Verification Checklist
- [ ] Can write pytest unit tests utilizing parameterization and mocking.
- [ ] Can construct a multi-stage GitHub Actions CI/CD pipeline script.
- [ ] Can select and justify a deployment strategy (e.g., Blue/Green vs. Canary) for a specific SLA.
- [ ] Can define RTO and RPO targets and build an operational recovery plan.
