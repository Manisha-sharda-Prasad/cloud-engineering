## 1. Amazon EC2 Overview :-
- Provides on-demand virtual server capacity (virtual machines/VMs) in the cloud.
- Faster,flexible, and cheaper than buying and maintaining physical servers on-premises.

## 1.1.Pay-as-You-Go Pricing :
- You only pay while instances are actively running,no charges when stopped.

## 1.2.Multi-Tenancy & Isolation:
- Multiple VMs share the same physical host hardware.
- A 'hypervisor' manages resource sharing and keeps each VM isolated and secure.

## 1.3.Launching & Scaling :
- AMI (Amazon Machine Image): Defines the OS and pre-installed software.
- Instance Type: Determines hardware resources (CPU, memory, network capability).
- Vertical Scaling: Easily resize instances up or down to match changing demand.

## 1.4.Steps to Get Started :
- Launch: Choose an AMI and instance type.
- Connect: Access via SSH (Linux), RDP (Windows), or AWS Systems Manager.
- Use: Run commands, install applications, and manage files.



## 2.EC2 Instance Types:-
- 1.General Purpose: Balanced compute, memory, and networking (web servers, code repos).
- 2.Compute Optimized: High-performance processing (gaming servers, scientific modeling, ML).
- 3.Memory Optimized: Fast performance for large in-memory datasets (real-time analytics, databases).
- 4.Accelerated Computing: Hardware accelerators for heavy calculations (graphics, floating-point math).
- 5.Storage Optimized: High throughput & low latency for large, locally stored data (data warehousing).



## 3.Provision AWS Resources :-
 Everything in AWS is powered by API calls behind the scenes :-

## 3.1. 3 Ways to Provision & Interact:
- AWS Management Console: Web UI for visual navigation, testing, and manual setup.
- AWS CLI: Command-line tool for terminal commands, automation, and reducing manual errors via scripts.
- AWS SDK: Code libraries to control AWS services directly inside programming languages (e.g., Python, Java).

## 3.2.Unmanaged Services (e.g., EC2):
- AWS Responsibilities: Hardware, physical infrastructure, and global facilities (Security of the cloud).
- Customer Responsibilities: Guest OS, updates, application configuration, data, and security groups/firewalls (Security in the cloud).



## 4.Launching an Amazon EC2 Instance & AMIs:-

## 4.1. 3 Required Configurations: 
- AMI, Instance Type, and Storage (type & size).

## 4.2 What is an AMI? 
- A pre-configured template containing the OS, storage setup, and software.

## 4.3 3 Ways to Get AMIs: 
- Build custom, use standard AWS AMIs, or buy from AWS Marketplace.

## 4.4 Key AMI Benefit: 
- Ensures identical, repeatable environments for quick and error-free scaling.



## 5. Amazon EC2 Pricing Models :-

## 5.1 On-Demand: 
- Pay for compute capacity by the hour or second with no long-term commitments
- for flexible workload, short-term.
## 5.2.Reserved Instances: 
- Commit to a 1- or 3-year term for significant savings
## 5.3.Spot Instances: 
- Bid for unused capacity at a discount, but can be interrupted by AWS with short notice
## 5.4.Savings Plans: 
- Flexible pricing model offering lower prices
- exchange for a commitment to a consistent amount of usage (measured in $/hour) for a 1- or 3-year term
## 5.5 Dedicated Hosts:
- Physical servers dedicated for your use, helping you meet compliance requirements 
- ideal for strict compliance and licensing needs.



## 6. Scaling Amazon EC2 :-
- Ensures high performance while cutting costs by paying only for active resources.
- Example: Amazon EC2 Auto Scaling:
  - Minimum: Baseline instances that run 24/7 for minimum service.
  - Desired: Target instances running to handle normal everyday traffic.
  - Maximum: Hard limit on instances to control costs and prevent over-scaling.

## S6.1. Scalability: 
- Scale up (bigger instance) or out (more instances) for growth.
## 6.2. Elasticity: 
- Real-time auto-scaling (up/down) to match fluctuating demand.
## 6.3. High Availability: 
- Deploying across multiple AZs prevents single points of failure.
## 6.4. Auto Scaling: 
- Uses CloudWatch metrics to scale within min/desired/max limits.



## 7. Directing Traffic with Elastic Load Balancing :-
- Example: In hospital booking systems, ELB spreads high patient traffic across multiple servers so the site stays up.

## 7.1. Elastic Load Balancing: 
- Distributes incoming traffic across EC2 instances to prevent overload and act as a single point of entry.
## 7.2. ELB Benefits: 
- Ensures efficient traffic distribution, scales automatically with demand, and simplifies backend management.
## 7.3. Routing Methods:
- Uses strategies like Round Robin, Least Connections, IP Hash, and Least Response Time to manage load.


