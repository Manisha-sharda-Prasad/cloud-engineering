# Distributed System :

## CAP Theorem :-
- https://www.youtube.com/watch?v=VdrEq0cODu4 
- https://www.youtube.com/watch?v=xUBMRdTyd30 

The CAP Theorem, distributed data store can only guarantee two out of the three properties:
- **Consistency (C)**: Every users see the exact same data at the same time.
- **Availability (A)**: The system is always on but doesn't guarantee the accurate or recent response.
- **Partition Tolerance (P)**: The system operates despite network failures(Partitions), inevitable in real-world, always have P.

Must choose between C or A:
- **Prioritize Consistency (CP)**: Sacrifice A, stop serving Wrong/Stale data to the user. E.g. Financial - Stocks, Bank.
- **Prioritize Availability (AP)**: Sacrifice C, risk serving data to the user which can be Stale /Wrong /Outdated /Chache data. E.g. Streaming - Netflix, YouTube, Comments/likes

---
## PACELC-Theorem :-

Extends CAP theorem, trade-offs in distributed systems not just during network failures, but during normal operation.
- Partition P: If network split happens pick A or C?
- **A / C**: Choose (Availability) or strict data sync (Consistency).
- Else: When the network is healthy and has no partitions -
- **L / C**: Choose fast response time (Latency) or data sync (Consistency)


---
## Edge Computing & CDNs:-
- [AWS CloudFront-CDN, Route 53 Latency, Edge Caching]
- [05_module-networking.md](../00_AWS_Cloud_Practitioner/05_module-networking.md)
