## **1.IaaS (Infrastructure as a Service)**
* Raw, computing services VM, storage,and networking hardware.
* Manages: Hardware, data centers, networking.
* Client Manage: OS installation, patching, runtime environments,data, and applications.
* Analogy: Renting unfurnished apartment, landlord maintains building, you bring furniture.
* Examples:  
  * Amazon EC2: rent Virtual Servers, configure OS, manage Network Security, and install software.
  * Amazon EBS: Raw Virtual Block storage, attached to your EC2 instances.
  * Amazon VPC: VPN Infrastructure, you define subnets, route tables, and gateways.

## **2. PaaS (Platform as a Service)**
* Provides pre-configured hardware and software platform, developers build, run, and manage applications only not building infrastructure.
* Manages: Physical hardware, virtualization, OS installation/patching, runtime environments, and capacity provisioning.
* Client Manage: The application code and data.
* Analogy: Renting a fully furnished apartment. You only bring your personal belongings (your code and data).
* Examples:
  * AWS Elastic Beanstalk: deploy application code, AWS handles provisioning, load balancing, and scaling.
  * Amazon RDS: manages database engine updates, OS patching, automatic backups, and hardware failures, you manage the schemas and queries.
  * AWS Elastic Container Service (ECS) with AWS Fargate: You provide container configurations and images, AWS runs and scales  containers without managing host VMs.

## **3. SaaS (Software as a Service)**
* Delivers complete, fully functional end-user applications and manage entirely by a third-party vendor over the web.
* Manages: The entire stack—from physical data centers, application code, maintenance, updates, and UI.
* Client Manage: User access controls, application settings, and profile data.
* Analogy: Staying in hotel room. Stay and check out; hotel handles maintenance, cleaning.
* Examples:
  * AWS SaaS Services: Amazon QuickSight (BI analytics), Amazon WorkSpaces (virtual desktops), Amazon Connect (cloud contact center).
  * Industry SaaS Products: Microsoft 365, Google Workspace, Salesforce, Slack, Dropbox.



