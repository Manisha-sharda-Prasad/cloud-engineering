# Distributed System :

## CAP Theorem :-
- https://www.youtube.com/watch?v=VdrEq0cODu4 | hi
- https://www.youtube.com/watch?v=xUBMRdTyd30 | bm

- The CAP Theorem, distributed data store can only guarantee two out of the three properties:

  - **Consistency (C)**: Every users see the exact same data at the same time.
  - **Availability (A)**: The system is always on but doesn't guarantee the accurate or recent response.
  - **Partition Tolerance (P)**: The system operates despite network failures(Partitions), inevitable in real-world, always have P.
- Must choose between C or A:
  - Prioritize Consistency (CP): Sacrifice A, stop serving Wrong/Stale data to the user. E.g. : Financial - Stocks, Bank
  - Prioritize Availability (AP): Sacrifice C, risk serving data to the user which can be Stale/Wrong/Outdated/Chache data. E.g. : Streaming - Netflix, YouTube, Comments/likes

---
## PAC-LEC Theorem :-

## Edge Computing :-
- [CloudFront,AWS,CDN](../07_01_AWS_cloud_computing/05_module-networking.md#62-amazon-cloudfront--cdn--)