# **Microservices Resilience Patterns :**
- Essential strategies for maintaining system stability when individual services fail.
- In a microservices architecture, a failure in one service can lead to **cascading failures**, brings down the entire system.


## **Top 5 Resilience Patterns & Strategies:**
* **Circuit Breaker :** For **Persistent Faults:** uncertain errors; Safeguard Pattern, Stops requests to a failing service for specific duration and prevents system failures.
* **Retry Pattern :** For **Transient Faults:** network glitches; Automatically retries failed requests, using **Exponential Backoff** to avoid overwhelming the system.
* **Fallback Pattern :** Provides an alternative for user, shows cached response when a service is unavailable.
* **Bulkhead Pattern :** Isolates critical services into separate compartments, so that one service's failure doesn't impact others.
* **Timeout Pattern :** Cancels requests that take too long to respond, ensuring the system remains responsive.



## **Circuit Breaker Pattern:**
### Key Concepts:
* **Cascading Failures:** 
    * Single service failure can trigger a chain reaction, effects an entire ecosystem(e.g. cart failure >>payment).

* **Circuit Breaker States:**
    * **Closed:** Normal operation; requests flow freely while metrics are tracked.
    * **Open:** The circuit trips if failure are met; requests rejected immediately, prevents overwhelming a failing system.
    * **Half-Open:** A testing phase, allows limited number of requests to check if the underlying service has recovered.

### Implementation Tools:
* **Resilience 4j:** Modern standard for Java developers,provides code example - configure failure thresholds, wait durations, and test calls.
*  **Hystrix:** as key libraries for implementing these patterns
* **Chaos Monkey:** to test system for future failures.**Chaos engineering**- A practice intentionally injecting failures into  production environment.


# **Idempotency and Intelligent Retry :**

### Idempotency keys :
- Ensures system consistency in distributed networks where failures, network latency, and retries are common.
- Serve as unique identifiers that allow systems to distinguish between different requests. 
- By storing these keys alongside the operation results, the system can:

* **Prevent Duplicate Transactions:** 
  * If the same key is submitted multiple times, system recognizes duplication and avoids re-processing the payment. 
* **Handle Retries Safely:** 
  * If original request was processed but the response was lost, system return the previously stored result instead of creating new. 


