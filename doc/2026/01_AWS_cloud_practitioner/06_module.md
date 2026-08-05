##  AWS Storage Types :

## 1. Block Storage: 
- Low-latency storage attached to instances like physical drives.
- can be encrypted, backed up via snapshots, and modified while in use without disrupting the instance.
## 1.1. EC2 Instance Store: 
- Unmanaged, attached to EC2 instances, high-performance storage
- Temporary block storage physically attached to the EC2 host computer (default storage).
- Data is deleted when the EC2 instance is stopped or terminated.
- High I/O performance needs like temporary buffers, caches, and scratch data.

## 1.2. Amazon EBS (Elastic Block Store) : 
- Managed, persistent block storage volumes,
- Data persists independently even if the EC2 instance is stopped or terminated.
- Supports incremental backups via EBS snapshots, detaching/reattaching, 
- automatic replication within an Availability Zone for high availability.
- Databases, file systems, and long-term application data retention.

## a. EBS Snapshots :
- incremental backups of EBS volumes
- first snapshot (check-point) of an EBS volume, has full copy of all the data  at that point in time.
- Each incremental snapshot contains references to the previous snapshots,
- Disaster recovery, migration, volume resizing, and mirroring production
- Snapshots stored redundantly in multiple Availability Zones using - 'Amazon S3'.
- Customer Role: set up schedules, defining retention periods, and maintaining encryption.
- Cost Control: Deleting outdated or unneeded snapshots, avoids unexpected storage fees.

## b. Amazon Data Lifecycle Manager (DLM) :
- Create an EBS snapshots policy using - AWS EC2 console,API calls,AWS CLI,SDKs,or AWS CloudFormation.
- Choose either an EBS volume or an EC2 instance as the target for the snapshot.
- choose to exclude the root volume or data volumes.
- Automates the creation, retention, and deletion of EBS snapshots
- configure elements of snapshots - tags, snapshot archiving, EBS fast snapshot restore, cross-Region copying.
- Reduces manual management errors, ensures compliance with backup policies, 
- schedules backups during off-peak hours.



## 2. Object Storage:
- offers unlimited scalability so you can store vast amounts of unstructured data
- using flat address spaces and rich metadata.
## 2.1. Amazon S3: 
- Fully managed, highly durable object store, 
- retrieving unlimited unstructured data (images, videos, documents) accessible from anywhere via HTTP/S.
- Containers for objects with globally unique names across all AWS accounts.
- Private by Default: newly created buckets, objects private until explicit access permissions are granted.
- Bucket Policies: Resource-based policies attached directly to buckets, allowed/denied actions for users and roles.
- Identity-Based Policies: 'AWS IAM' policies attached to users, groups, or roles.
- S3 Block Public Access: Account- or bucket-level setting, overrides public permissions to prevent accidental data exposure.

##  S3 Storage Classes :

## a. General & Ultra-Fast Access:
- S3 Standard: Default option for frequently accessed data (cloud apps,dynamic websites,analytics,mobile and gaming applications).
- S3 Express One Zone: Single-AZ storage for sub-millisecond, latency-sensitive applications, speed-10x faster and costs up to 80% lower than S3 Standard.
## b. Automated & Infrequent Access(IA):
- S3 Intelligent-Tiering: Automatically moves objects between 3 tiers:frequent,infrequent,and archive instant access tiers based on changing unknown access patterns to cut costs.
- S3 Standard-IA: Infrequently accessed data, requiring fast retrieval. Uses Multi-AZ for high availability. 
- One Zone-IA: Infrequent Access,Uses 1 AZ for secondary backups at a lower cost, as compared to S3 Standard-IA, which uses 3 zones.
## c. Archival & On-Premises:
- S3 Glacier Instant Retrieval: archiving data that is rarely accessed, requires millisecond retrieval. Cost savings -68% compared to the S3 Standard-IA.
- S3 Glacier Flexible Retrieval: archived data accessed 1–2 times per year. Bulk retrievals in up to 5–12 hours at no additional cost. Ideal for backup,disaster recovery, offsite data storage.
- S3 Glacier Deep Archive: long-term retention,digital preservation for data that might be accessed once or twice per year. Ideal for 7–10 years or longer. Ideal for financial, healthcare.
- S3 Outposts: Brings S3 object storage directly to on-premises environments for local data residency and processing needs. 



## 3.File Storage: 
- Shared networked file systems accessible by multiple systems concurrently.
- you can expand storage capacity as needs grow without managing physical infrastructure.
## 3.1. Amazon EFS: 
- Fully managed, scalable NFS file system for Linux workloads across AWS and on-premises.
## 3.2. Amazon FSx: 
- Fully managed third-party file systems 
- (e.g., Windows File Server, Lustre, NetApp ONTAP).




## 4. Additional Storage Services : 

## 4.1. AWS Storage Gateway: 
- Hybrid cloud storage service providing on-premises applications seamless access to AWS Cloud storage.
## 4.2. AWS Elastic Disaster Recovery: 
- Automated service for recovering physical, virtual, and cloud-based servers into AWS.
