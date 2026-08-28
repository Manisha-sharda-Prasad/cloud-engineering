# Serverless Computing :-
> Run applications without managing the underlying infrastructure.

---
## AWS compute services :-

### 1.AWS Lambda :-
- Serverless compute service, that runs code(on demand) in response to events.
- **Function as a Service (FAAS)** — Zero server management
- Handles infrastructure, execution, scaling, resource allocation, availability, and maintenance .
- Pay per Use: only for the compute time consumed by your code, measured in milliseconds.
- Max Runtime: 15 minutes per request.
- Event-Driven: Set Triggers,Functions triggered by events (e.g., file uploads, database changes, API calls).
- Automatic Scaling: automatically scales, based on number of incoming requests.
### 2.Amazon ECS :-
- AWS’s native tool to scale and manage Docker containers.
- integrated with native AWS services (like IAM, CloudWatch, and Route 53).
- ECS-EKS - Container orchestration services that simplify running and managing containerized apps
### 3.Amazon EKS :-
- AWS’s managed service to run open-source Kubernetes.
- hybrid/multi-cloud portability.
### 4.AWS Elastic Beanstalk :-
- Platform service that streamlines application deployment and environment management.

---
## AWS unmanaged, managed, and fully-Managed compute services :-
### 1.Unmanaged (EC2) :-
- You manage OS, patches, and code; AWS manages hardware.
### 2.Managed :-
- AWS handles infrastructure overhead; you configure scaling and deployment.
### 3.Fully-Managed / Serverless (Lambda,S3,SNS) :-
- AWS manages all servers and scaling; you only write code.

---
## Containers, Orchestration and VM on AWS :-
### 1.Containers :-
- Application-level packaging, Package code with its dependencies,
- Speed - Seconds or milliseconds
- Primary Tool e.g. - Docker, Podman
- consistent and portable runtime environment, across different systems.
- faster and lighter than VMs.

### 2.Virtual machines (VM) :-
- Hardware-level virtualization
- High (runs a complete Guest OS per VM)
- Speed - Minutes (boots full OS)
- Primary Tool e.g. - AWS EC2, VMware, Hyper-V
- A hypervisor partitions a physical server, helps run multiple independent OS on single physical machine.

### 3.Orchestration :-
- Automated system management 
- Handle operations- deployments, load balancing, auto-scaling and managing lifecycle of large number of containers
- Scale containers out when traffic increases, scale back in when calm down.
- Primary Tool e.g. - Kubernetes (EKS), Amazon ECS (for packaging an application).

---
## Key AWS Container Orchestration Services :ECS,EKS,ECR,Fargate:-

### 1.Amazon ECR :-
- A secure repository to store and fully managed container registry that stores your container images.
### 2. AWS Fargate :-
- A serverless compute engine that runs containers without managing underlying servers.
