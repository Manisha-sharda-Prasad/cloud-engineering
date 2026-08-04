## Introduction to Storage :-

## 1. AWS Storage Types :

## 1.1. Block Storage: 
- Low-latency storage attached to instances like physical drives.
- can be encrypted, backed up via snapshots, and modified while in use without disrupting the instance.
## a. EC2 Instance Store: 
- Unmanaged, attached to EC2 instances for temporary data.
- high-performance storage directly attached to the physical host.
## b. Amazon EBS: 
- Managed, persistent block storage volumes that persist independently of EC2 instance lifecycles.

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
- streamlines the recovery of your physical, virtual, and cloud-based servers into AWS.