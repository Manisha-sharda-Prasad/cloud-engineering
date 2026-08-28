# Modern Web Application Architecture :
###  End-to-end journey of a user **request-response lifecycle** :

*   **DNS Resolution:** Translating the domain name into an IP address, route to the closest server (e.g.**Route 53**).
*   **API Gateway & Backend:** Traffic controller, validate requests and route them to specific microservices, which perform  heavy lifting.
*   **Traffic Management:** Utilizing **Nginx** for reverse proxying and **Load Balancers** to distribute traffic evenly (NLB - low-latency/high-performance; ALB - advanced path-based routing) .
*   **CDN / Content Delivery:** Caching static assets at edge locations using services like **CloudFront** - minimize latency.
*   **Security:** Using  **Web Application Firewall (WAF)** - filters out malicious traffic like SQL injection.
*   **Data & Async Tasks:** Interaction with databases (**SQL/NoSQL**) and message queues like **Kafka/SQS** for background processing.
*   **Monitoring & Optimization:** Ongoing support through authentication services, caching (e.g.**Redis**), and monitoring tools like **CloudWatch**.


![img_1.png](img_1.png)

---

```mermaid
flowchart TD
    Client([🙎‍♂️HTTP Request]) --> Route53[AWS Route 53]
    Client <--> CloudFront[AWS CloudFront 🟡]
    Route53  --> WAF[WAF : Web Application Firewall 🟡]
    WAF --> APIGW[API Gateway\nAuthentication\nRate-limiting & Throttling\n...]

    APIGW --> LB[Load Balancer\nALB / NLB\n-TLS termination\n-caching\n-Authentication\n...]

    subgraph Observability
        AWScloudWatch
        Prometheus
        DataDog
    end

    Microservices -.-> Observability

    subgraph Microservices["Microservices Architecture"]
        direction TB
        K8s["Kubernetes Cluster - \n service 1 (pod 1), \n service 2 (pod 2), \n service 3 (pod 3)\n..."]
        Lambda[AWS \nLambda 1, \n Lambda 2, \n Lambda 3\n...]
        EC2[Amazon \n EC2 1, \n EC2 2, \n EC2 3\n...]
    end

    LB --> Microservices
    Microservices --> Redis[(Redis Cache)]
    Microservices --> Kafka[Apache Kafka]
    Microservices --> Postgres[(PostgreSQL)]
    Microservices --> Dynamo[(Amazon DynamoDB)]

```
