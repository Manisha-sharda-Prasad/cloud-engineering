## Introduction to Storage :-

## 1. AWS Storage Types :

## 1.1. Block Storage: 
- Low-latency storage attached to instances like physical drives.
- can be encrypted, backed up via snapshots, and modified while in use without disrupting the instance.
## a. EC2 Instance Store: 
- Unmanaged, attached to EC2 instances, high-performance storage
- Temporary block storage physically attached to the EC2 host computer (default storage).
- Data is deleted when the EC2 instance is stopped or terminated.
- High I/O performance needs like temporary buffers, caches, and scratch data.

## b. Amazon EBS (Elastic Block Store) : 
- Managed, persistent block storage volumes,
- Data persists independently even if the EC2 instance is stopped or terminated.
- Supports incremental backups via EBS snapshots, detaching/reattaching, 
- automatic replication within an Availability Zone for high availability.
- Databases, file systems, and long-term application data retention.

## Amazon EBS data lifecycle management 
- involves creating, backing up, and deleting volumes and snapshots. 
- This process optimizes storage costs and helps to ensure data protection
## EBS Snapshots :
- incremental backups of EBS volumes
- create multiple new volumes, created from a snapshot are an exact copy of the original volume
- Disaster recovery, migration, volume resizing, and mirroring production
- Snapshots of EBS volumes, stored redundantly in multiple Availability Zones using Amazon S3.



## 1.2. Object Storage:
- offers unlimited scalability so you can store vast amounts of unstructured data
- using flat address spaces and rich metadata.
## a. Amazon S3: 
- Fully managed, highly durable object store accessible from anywhere via HTTP/S.
- for storing and retrieving any amount of data from anywhere.

## 1.3.File Storage: 
- Shared networked file systems accessible by multiple systems concurrently.
- you can expand storage capacity as needs grow without managing physical infrastructure.
## a. Amazon EFS: 
- Fully managed, scalable NFS file system for Linux workloads across AWS and on-premises.
## b. Amazon FSx: 
- Fully managed third-party file systems 
- (e.g., Windows File Server, Lustre, NetApp ONTAP).




## 2. Additional Storage Services : 

## a. AWS Storage Gateway: 
- Hybrid cloud storage service providing on-premises applications seamless access to AWS Cloud storage.
## b. AWS Elastic Disaster Recovery: 
- Automated service for recovering physical, virtual, and cloud-based servers into AWS.
