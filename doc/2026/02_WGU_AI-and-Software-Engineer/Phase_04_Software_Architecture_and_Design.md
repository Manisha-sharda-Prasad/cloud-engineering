# Phase 4: Software Architecture & Design
**Duration:** Weeks 8–10 (3 Weeks)  
**Target WGU Course:** Software Architecture and Design (3 CUs)

---

## 1. Official WGU Competencies Covered
- [ ] Analyze and evaluate software design patterns to solve software engineering problems.
- [ ] Explain how design patterns solve specific software architectural challenges.
- [ ] Implement an end-to-end software architecture and design solution.
- [ ] Justify architectural decisions against quality attributes and technical trade-offs.

---

## 2. Comprehensive Study Topics

### 4.1 Architectural Foundations & Principles
- **Architecture vs. Design:** High-level system structure/boundaries vs. localized code structure.
- **Coupling & Cohesion:** Strive for Low Coupling (loose dependencies) and High Cohesion (focused responsibilities).
- **SOLID Principles:**
  - **S:** Single Responsibility Principle
  - **O:** Open/Closed Principle
  - **L:** Liskov Substitution Principle
  - **I:** Interface Segregation Principle
  - **D:** Dependency Inversion Principle
- **DRY & KISS:** Don't Repeat Yourself; Keep It Simple, Stupid.

### 4.2 Architectural Styles & Patterns
- **Monolithic Architecture:** Single deployable unit, shared database, simple debugging, scaling limitations.
- **Layered (N-Tier) Architecture:** Presentation Layer $ightarrow$ Application/Service Layer $ightarrow$ Business Logic $ightarrow$ Data Access Layer.
- **Microservices Architecture:** Independently deployable services, fine-grained domain boundaries (Bounded Contexts), decentralized data management, API communication overhead.
- **Event-Driven Architecture (EDA):** Event Producers, Event Routers/Brokers (Kafka, EventBridge), Consumers, Pub/Sub, Asynchronous processing, Eventual Consistency.
- **Serverless Architecture:** Function-as-a-Service (FaaS - AWS Lambda), auto-scaling, pay-per-execution, statelessness.

### 4.3 Design Patterns (GoF)
- **Creational Patterns:**
  - *Factory Method:* Instantiating objects without exposing creation logic.
  - *Builder:* Constructing complex objects step-by-step.
  - *Singleton:* Ensuring a single instance globally (use with caution).
- **Structural Patterns:**
  - *Adapter:* Enabling incompatible interfaces to collaborate.
  - *Decorator:* Dynamically adding behavior to objects without modifying original class.
  - *Facade:* Providing a simplified interface to a library/framework/subsystem.
- **Behavioral Patterns:**
  - *Strategy:* Encapsulating interchangeable algorithms.
  - *Observer:* Subscribing to state changes across components.
  - *Command:* Encapsulating requests as objects for logging/queuing/undo.

### 4.4 Architectural Documentation & ADRs
- **C4 Model Hierarchy:**
  1. *Context Diagram:* System in its environment with external users/systems.
  2. *Container Diagram:* High-level tech stack (Web App, API Gateway, Microservice, Database).
  3. *Component Diagram:* Internal structure of a container.
  4. *Code Diagram:* Class/UML details.
- **Architecture Decision Records (ADRs):** Title, Status, Context, Decision, Consequences.

---

## 3. Architecture Decision Matrix

| Architectural Style | Scalability | Complexity | Deployment Speed | Fault Isolation |
| :--- | :--- | :--- | :--- | :--- |
| **Monolith** | Vertical (Limited) | Low | Fast (Initial) | Low (Single point of failure) |
| **Layered (N-Tier)** | Moderate | Low-Moderate | Moderate | Moderate |
| **Microservices** | Horizontal (High) | High | Fast (Per service) | High |
| **Event-Driven** | Extremely High | High | Fast | High |

---

## 4. Phase Deliverable
**Project:** Software Architecture Design Document (SADD) & C4 Diagrams  
**Requirement:** Create a complete architectural package for an enterprise application:
1. System Context Diagram and Container Diagram using the C4 model.
2. Complete GoF Design Pattern Implementation Code (Python): Demonstrate Factory, Strategy, and Observer patterns working in unison.
3. 3 Written **Architecture Decision Records (ADRs)** justifying:
   - Microservices vs. Monolith choice.
   - Database selection (Relational SQL vs. NoSQL Document/Key-Value).
   - Synchronous REST vs. Asynchronous Event-Driven communication.

---

## 5. Weekly Schedule & Action Plan

```
Week 8: SOLID Principles, Clean Code, & Layered Architectures
├── Mon-Tue: SOLID principles deep dive with concrete Python examples.
├── Wed-Thu: Layered architecture (Presentation, Business, Data layers) design.
└── Fri-Sun: Monolith vs. Microservices comparison and trade-off analysis.

Week 9: Microservices, Event-Driven Architecture, & Design Patterns
├── Mon-Tue: Event-driven architecture, Pub/Sub, message queues (Kafka, EventBridge).
├── Wed-Thu: Creational & Structural design patterns (Factory, Adapter, Decorator, Facade).
└── Fri-Sun: Behavioral design patterns (Strategy, Observer, Command), Python implementations.

Week 10: C4 Model, ADRs, & Architectural Deliverable
├── Mon-Tue: C4 modeling methodology (Context, Container, Component diagrams).
├── Wed-Thu: Authoring Architectural Decision Records (ADRs).
└── Fri-Sun: Complete Phase Deliverable (SADD + C4 Diagrams + Code Implementation).
```

---

## 6. WGU Competency Verification Checklist
- [ ] Can identify and correct violations of SOLID principles in existing code.
- [ ] Can choose between Monolithic and Microservices architecture with clear technical trade-off justifications.
- [ ] Can implement Strategy, Observer, and Factory patterns in Python.
- [ ] Can create C4 Context and Container diagrams for a complex distributed software system.
