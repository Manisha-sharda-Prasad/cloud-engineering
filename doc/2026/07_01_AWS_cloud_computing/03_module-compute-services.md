# Serverless Computing :-
> Run applications without managing the underlying infrastructure.

---
## 1.AWS compute services :-
### 1.1. AWS Lambda :-
- Serverless compute that automatically handles scaling, availability, and maintenance.
- Function as a Service (FaaS) — Zero server management
### 1.2. Amazon ECS & EKS :-
- Container orchestration services that simplify running and managing containerized apps.
### 1.3. AWS Elastic Beanstalk :-
- Platform service that streamlines application deployment and environment management.

---
## 2. AWS unmanaged, managed, and fully-Managed compute services :-
### 2.1. Unmanaged (EC2) :-
- You manage OS, patches, and code; AWS manages hardware.
### 2.2. Managed :-
- AWS handles infrastructure overhead; you configure scaling and deployment.
### 2.3. Fully-Managed / Serverless (Lambda) :-
- AWS manages all servers and scaling; you only write code.

---
## 3. AWS Lambda :-
- Serverless compute service, that runs code(on demand) in response to events.
- Pay per request and execution duration
- handles execution, scaling, and resource allocation.
- automatically manages the infrastructure, scaling resources based on the volume requests
- Max Runtime:15 minutes per request.

### 3.1. Event-Driven :-
- Set Triggers
- Functions are triggered by events (e.g., file uploads, database changes, API calls).
### 3.2. Pay-per-Use :-
- You pay only for the compute time consumed by your code, measured in milliseconds.
### 3.3. Automatic Scaling: () :-
- Lambda automatically scales based on the number of incoming requests, without manual intervention.

---
## 4. Containers, Orchestration and VM on AWS :-
### 4.1. Containers :-
- Application-level packaging
- Package code with its dependencies,
- Speed - Seconds or milliseconds
- Primary Tool e.g. - Docker, Podman
- creates a consistent and portable runtime environment, across different systems.
- faster and lighter than virtual machines (VMs).

### 4.2. Virtual machines (VM) :-
- Hardware-level virtualization
- High (runs a complete Guest OS per VM)
- Speed - Minutes (boots full OS)
- Primary Tool e.g. - AWS EC2, VMware, Hyper-V
- A hypervisor partitions a physical server, helps run multiple independent OS on single physical machine.

### 4.3. Orchestration :-
- Automated system management 
- Handle operations- deployments, load balancing, auto-scaling and managing lifecycle of large number of containers
- Scale containers out when traffic increases, scale back in when calm down.
- Primary Tool e.g. - Kubernetes (EKS), Amazon ECS (for packaging an application).


---
## 5. Key AWS Container Orchestration Services :-
### 5.1. Amazon ECS :-
- AWS’s native tool to scale and manage Docker containers.
- integrated with native AWS services (like IAM, CloudWatch, and Route 53).
### 5.2. Amazon EKS :-
- AWS’s managed service to run open-source Kubernetes.
- hybrid/multi-cloud portability.
### 5.3. Amazon ECR :-
- A secure repository to store and fully managed container registry that stores your container images.
### 5.4. AWS Fargate :-
- A serverless compute engine that runs containers without managing underlying servers.
