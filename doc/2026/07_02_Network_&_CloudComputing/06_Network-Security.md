# Network Security : Defense in Depth :- 
- Cybersecurity strategy, deploying multiple layered defenses throughout an IT infrastructure.
- One mechanism fails, other layers immediately block the attack.

## Perimeter Security :
- **First line of defense**, Front Gate traffic checkpoint.
- **Monitors/ Controls boundary between untrusted external (internet) and internal networks**.
- Mechanisms: 
  - **Edge firewalls, Web Application Firewalls(WAF)**, 
  - Distributed Denial of Service (DDoS-clean traffic), 
  - DNS filtering, and intrusion prevention systems (IPS).
- Role: Stops attacks, malicious IP sweeps, before they reach internal resources.

---
## Network Segmentation :
- Divide **Internal network into Isolated smaller Subnets or Security Zones** to restrict movement, if an attacker breaches the Perimeter.
- Need good visibility,**Ongoing setup regularly,** not just one time setup.
- Mechanisms: 
  - Virtual Local Area Networks **(VLANs), 
  - VPCs with public/private subnets, 
  - NACLs, Security Groups,** and Micro-Segmentation.
- Role: Ensures **compromised public web server cannot directly access sensitive backend databases**.

---
## Host Security (Endpoint Protection) :
- **Protecting actual devices**, which applications should be downloaded in OS. 
- **Defend compute Instances, Servers, Containers,** and user workstations.
- Mechanisms: 
  - **Endpoint Detection and Response (EDR) (monitors devices)** , 
  - **OS-level Firewalls (filter traffic)**,
  - **Regular Patch Management (keeping OS updated, consistent to protect)**, 
  - **Vulnerability Scanning (checkup, tools, outdated software)**, 
  - **System Hardening (CIS benchmarks) - (disabling unnecessary logins/ports/services)**.
- Key Role: Detects and neutralizes malicious processes, privilege escalation attempts, or unauthorized configuration changes directly on the operating system.

---
## Identity & Access Management (IAM) :
- Concept of only Right people can touch the right resources.
- Ensures only **Verified Identities (human users/ applications/ services) can gain access** to specific resources, If roles assigned/ permissions given, Strictly stops Least Privilege.
- Mechanisms:
  - Multi-Factor Authentication (MFA), 
  - Single Sign-On (SSO), Role-Based Access Control (RBAC), 
  - Attribute-Based Access Control (ABAC), 
  - short-lived credentials/tokens.
- Key Role: Restricts radius of compromised credentials, ensuring users/ service roles have only the minimum permissions necessary for their tasks.

---
## Data Encryption (At-rest & In-transit).
- Allowed key can Enter/open the door, 
- Protect data confidentiality so that **important data is unreadable and unusable** without the corresponding cryptographic keys.
- **Encryption In-Transit**: 
  - Secures data moving over networks using **cryptographic protocols like TLS**( web traffic, banks logins),
  - **IPsec (network to network). It prevents eavesdropping, tampering, and man-in-the-middle (M-i-t-M) attacks**.
- **Encryption At-Rest**: 
  - Protects stored data on disks, databases, object stores, and backups using symmetric ciphers like AES-256, 
  - coupled with dedicated key management services (KMS), 
  - Hardware security modules (HSMs).