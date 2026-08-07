## Introduction to Databases :-

## 1. Relational Database Services :
- collections of data into tables with rows and columns, 
- relationships exist between different tables.
- they use structured query language, or SQL, to manage and query data.
- AWS relational databases support database engines like MySQL, PostgreSQL, and Oracle.

## 1.1. Amazon RDS :
- Managed standard relational database service like - MySQL, PostgreSQL, Oracle, SQL Server.
- traits: Automates backups, patching, and fixed provisioning storage.
- for: Standard workloads/applications requiring traditional enterprise engines like - SQL Server or Oracle.

## 1.2. Amazon Aurora :
- AWS's high-performance, cloud-native database engine compatible with MySQL and PostgreSQL.
- traits: Auto-scaling storage, 6-way data replication across 3 AZs, and sub-minute failovers.
- for: High-throughput, mission-critical, gaming applications, media and content management, 
- requiring speed and reliability.


## 2. NoSQL Database Services :
- Non-relational, schema-flexible databases
- Instead of row and column relationships, it contains data using key-value pairs and identified by unique keys.

## 2.1. Amazon DynamoDB
- AWS's fully managed, serverless NoSQL database supporting key-value and document formats.
- traits: Delivers single-digit millisecond performance, auto-scales instantly, and uses built-in multi-AZ replication.
- for: Internet-scale web apps, real-time user profiles, shopping carts, and gaming state stores.