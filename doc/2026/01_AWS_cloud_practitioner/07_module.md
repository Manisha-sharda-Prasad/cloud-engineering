## Introduction to Databases :-

## 1. Relational Database Services :
- collections of data into tables with rows and columns, 
- relationships exist between different tables.
- they use structured query language, or SQL, to manage and query data.
- AWS relational databases support database engines like MySQL, PostgreSQL, and Oracle.

## 1.1. Amazon RDS
- Managed standard relational database service (MySQL, PostgreSQL, Oracle, SQL Server).
- traits: Automates backups, patching, and provisioning; uses fixed provisioned storage.
- for: Standard workloads or applications requiring traditional enterprise engines like SQL Server or Oracle.

## 1.2. Amazon Aurora

- AWS's high-performance, cloud-native database engine compatible with MySQL and PostgreSQL.
- traits: Auto-scaling storage, 6-way data replication across 3 AZs, and sub-minute failovers.
- for: High-throughput, mission-critical production workloads requiring enterprise-grade speed and reliability.