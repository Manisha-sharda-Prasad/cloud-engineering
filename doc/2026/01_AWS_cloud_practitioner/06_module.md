## Introduction to Storage :-

## 1. AWS Storage Types :

## 1.1. Block Storage: 
- Low-latency storage attached to instances like physical drives.
## a. EC2 Instance Store: 
- Unmanaged, ephemeral (temporary) high-performance storage directly attached to the physical host.
## b. Amazon EBS: 
- Managed, persistent block storage volumes that persist independently of EC2 instance lifecycles.

## 1.2. Object Storage: 
- Scalable storage for unstructured data using flat address spaces and rich metadata.
## a. Amazon S3: 
- Fully managed, highly durable object store accessible from anywhere via HTTP/S.

## 1.3.File Storage: 
- Shared, networked file systems accessible by multiple systems concurrently.
## a. Amazon EFS: 
- Fully managed, scalable NFS file system for Linux workloads across AWS and on-premises.
## b. Amazon FSx: 
- Fully managed third-party file systems (e.g., Windows File Server, Lustre, NetApp ONTAP).

## 2. Additional Storage Services : 

## 2.1. AWS Storage Gateway: 
- Hybrid cloud storage service providing on-premises applications seamless access to AWS Cloud storage.
## 2.2. AWS Elastic Disaster Recovery: 
- Automated service for recovering physical, virtual, and cloud-based servers into AWS.