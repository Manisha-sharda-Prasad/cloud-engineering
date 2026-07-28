## Amazon EC2 Overview :-
- Provides on-demand virtual server capacity (virtual machines/VMs) in the cloud.
- Faster,flexible, and cheaper than buying and maintaining physical servers on-premises.

## 1.Pay-as-You-Go Pricing :
- You only pay while instances are actively running,no charges when stopped.

## 2.Multi-Tenancy & Isolation:
- Multiple VMs share the same physical host hardware.
- A 'hypervisor' manages resource sharing and keeps each VM isolated and secure.

## 3.Launching & Scaling :
- AMI (Amazon Machine Image): Defines the OS and pre-installed software.
- Instance Type: Determines hardware resources (CPU, memory, network capability).
- Vertical Scaling: Easily resize instances up or down to match changing demand.

## 4.Steps to Get Started :
- Launch: Choose an AMI and instance type.
- Connect: Access via SSH (Linux), RDP (Windows), or AWS Systems Manager.
- Use: Run commands, install applications, and manage files.


## Instance Families & Best Use Cases :-
- 1.General Purpose: Balanced compute, memory, and networking (web servers, code repos).
- 2.Compute Optimized: High-performance processing (gaming servers, scientific modeling, ML).
- 3.Memory Optimized: Fast performance for large in-memory datasets (real-time analytics, databases).
- 4.Accelerated Computing: Hardware accelerators for heavy calculations (graphics, floating-point math).
- 5.Storage Optimized: High throughput & low latency for large, locally stored data (data warehousing).


## Provision AWS Resources :-
 Everything in AWS is powered by API calls behind the scenes :-

## 3 Ways to Provision & Interact:
- AWS Management Console: Web UI for visual navigation, testing, and manual setup.
- AWS CLI: Command-line tool for terminal commands, automation, and reducing manual errors via scripts.
- AWS SDK: Code libraries to control AWS services directly inside programming languages (e.g., Python, Java).

## Unmanaged Services (e.g., EC2):
- AWS Responsibilities: Hardware, physical infrastructure, and global facilities (Security of the cloud).
- Customer Responsibilities: Guest OS, updates, application configuration, data, and security groups/firewalls (Security in the cloud).