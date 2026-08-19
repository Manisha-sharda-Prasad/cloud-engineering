
# **Circuit Breaker :**
- A pattern in microservices architectures, acts as a safeguard for system failures.

### Key Concepts:
* **Cascading Failures:** 
    * Single service failure can trigger a chain reaction, effects an entire ecosystem(e.g. cart failure >>payment).

* **Resilience Strategies:**
    * **Retry Pattern:** for **Transient Faults**, minor network glitches.(e.g.analogy- for-loop)
    * **Circuit Breaker Pattern:** for **Persistent Faults** to prevent resource exhaustion and stop the uncertain errors.
  
* **Circuit Breaker States:**
    * **Closed:** Normal operation; requests flow freely while metrics are tracked.
    * **Open:** The circuit trips if failure are met; requests rejected immediately, prevents overwhelming a failing system.
    * **Half-Open:** A testing phase, allows limited number of requests to check if the underlying service has recovered.

### Implementation:
* **Resilience 4j:** 
    * Modern standard for Java developers, 
    * provides code example, how to configure failure thresholds, wait durations, and test calls.