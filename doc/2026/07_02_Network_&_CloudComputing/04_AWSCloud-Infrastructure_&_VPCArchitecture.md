# Core AWS Building Blocks:

## Compute:
> Ec2, lambda, ECS, EKS
- [02_module-ec2.md](../07_01_AWS_cloud_computing/02_module-ec2.md)
- [03_module-compute-services.md](../07_01_AWS_cloud_computing/03_module-compute-services.md) | AWS Lambda and ECS/EKS

---
## Storage: 
> S3, EBS, EFS, FSX
- [06_module-storage.md](../07_01_AWS_cloud_computing/06_module-storage.md)

---
## Database: 
> RDS, DynamoDB
- [07_module-database.md](../07_01_AWS_cloud_computing/07_module-database.md)

---
## Networking: 
> VPC, Subnets, Internet Gateways(IGW), NAT Gateways, Route Tables, Security Groups,  NACLs
- [05_module-networking.md](../07_01_AWS_cloud_computing/05_module-networking.md)


---
### Bastion Hosts:

- A Bastion Host ("Jump Box") specialized EC2 instance placed in a Public Subnet. 
- act as a secure gateway to access instances located in private subnets.

### SSH?
- SSH (Secure Shell) secure network protocol used to remotely log into a server over the internet.
- SSH into an EC2 instance, opens an encrypted terminal session - allows to run commands and manage that server as if you were sitting right in front of it. 
- It operates on Port 22.

### SSH & Bastion Work Together:
- In a secure AWS VPC architecture, most critical resources — databases or application servers placed in - Private Subnets. 
- Private - no public IP addresses, so cannot be reached directly from the outside internet.
- Bastion Hosts > to access, run updates, manage files, or troubleshoot does:
  - First Jump: SSH from local computer into the Bastion Host using its public IP address.
  - Second Jump: From inside the Bastion Host, initiate second SSH connection to target EC2 instance in private subnet using its private IP address.
- Why Do We Need This?
  - For security: Minimizing attack surface, only expose /Tightly lock - Bastion Host. 
  - Exposing private servers to the internet is a security risk. 
  - Allow SSH traffic from specific home /office IP address.

---
## VPC Isolation Design Pattern:
Public Subnets (IGW routed) for Load Balancers / Bastions. 
- 

Private Subnets (NAT Routed) for Application Compute / Microservices.
- 

Isolated Database Subnets (No internet route) for RDS/Databases.
- 

---
## VPC Tiering Structure:

![img_2.png](img_2.png)

**Public Subnets Tier:**
* Has a direct route (0.0.0.0/0) to the IGW. Hosts edge ingress components like Application Load Balancers (ALBs) and Bastion Hosts.

**Private Subnets Tier:** 
* Routes outbound internet traffic (0.0.0.0/0) to a NAT Gateway (no direct IGW route). Hosts application servers and microservices.

**Isolated Database Tier:**
* Has no route to the internet, keeping databases strictly isolated from external access.
