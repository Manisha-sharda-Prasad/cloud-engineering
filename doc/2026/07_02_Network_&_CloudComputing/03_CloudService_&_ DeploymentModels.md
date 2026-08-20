## **1.IaaS (Infrastructure as a Service)**
* Provides raw,  computing resources over the internet, VM, storage,and networking hardware.
* Provider Manages: Physical hardware,data centers,virtualization, networking.
* Client Manage: Operating system (OS) installation, patching, runtime environments, middleware, networking rules, data, and applications.
* Analogy: Renting unfurnished apartment -landlord maintains the building structure, you bring all the furniture.
* AWS Examples:  **Amazon EC2**:  rent Virtual Servers, configure OS, manage network security, and install software.
* Amazon EBS: Raw virtual block storage attached to your EC2 instances.
* Amazon VPC: Virtual private network infrastructure where you define subnets, route tables, and gateways.

## **2. PaaS (Platform as a Service)**
* Provides a pre-configured hardware and software platform, allowing developers to build, run, and manage applications without the complexity of building and maintaining underlying infrastructure.
* Provider Manages: Physical hardware, virtualization, OS installation/patching, runtime environments, and capacity provisioning.
* You Manage: The application code and data.
* Analogy: Renting a fully furnished apartment. You only need to bring your personal belongings (your code and data).
* AWS Examples:
  * AWS Elastic Beanstalk: You deploy your application code, and AWS automatically handles provisioning, load balancing, and scaling.
  * Amazon RDS: AWS manages database engine updates, OS patching, automatic backups, and hardware failures, while you manage the database schemas and queries.
  * AWS Elastic Container Service (ECS) with AWS Fargate: You provide container configurations and images, while AWS runs and scales the containers without managing host VMs.

## **3. SaaS (Software as a Service)**
* Delivers complete, fully functional end-user applications hosted and managed entirely by a third-party vendor over the web.
* Provider Manages: The entire stack—from physical data centers up to the application code, maintenance, updates, and user interfaces.
* You Manage: User access controls, application settings, and profile data.
* Analogy: Staying in a fully serviced hotel room. You just show up, stay, and check out; the hotel handles maintenance, cleaning, and utilities.
* Examples:
  * AWS SaaS Services: Amazon QuickSight (BI analytics), Amazon WorkSpaces (virtual desktops), Amazon Connect (cloud contact center).
  * Industry SaaS Products: Microsoft 365, Google Workspace, Salesforce, Slack, Dropbox.