## 1. Going Global & Infrastructure : -
- Expand applications worldwide using AWS Regions (geographic clusters)
- Availability Zones (isolated data centers) for high availability.

## 1.1.Choosing Regions & Edge Locations:
- Pick Regions based on compliance, latency, cost, and service availability; 
- use Edge Locations to cache content closer to users for lower latency.
## 1.2.IaC & CloudFormation:
- Infrastructure as Code (IaC) defines cloud setup in code files, 
- while AWS CloudFormation automates consistent deployment of these resources.


## 2. Choosing AWS RegionsDefinition : -
- Select specific geographic locations globally 
- where AWS hosts data centers to run your infrastructure and store data.

## Key Considerations:
## 2.1. Compliance & Data Privacy: 
- Select regions that meet local regulations and data residency laws (e.g.GDPR)General Data Protection Regulation .
- (GDPR)- designed to protect the personal data and privacy within the European Union (EU).
## 2.2. Latency & Proximity:
- Pick regions closest to your users to ensure low latency and performance.
## 2.3. Service Availability: 
- Verify the region supports the specific AWS services and features your app requires.
## 2.4. Pricing: 
- Choose cost-effective regions, as service rates vary globally by location.
- Tax laws and regulations can also play a role in cost.



## 3. AWS Global Infrastructure Core Pillars :-

## 3.1. Difference between these advantages:
## High Availability:
- capability of a system to operate continuously without failing.
- applications can handle the failure  without significant downtime.
## Agility: 
- ability to quickly adapt to changing requirements or market conditions.
- Rapid deployment and provisioning of global infrastructure in seconds.
## Elasticity: 
- ability of a system to scale resources up or down automatically in response to changes in demand.



## 4. Key elements of AWS Global Infrastructure:
## AWS Regions: 
- Isolated geographical areas worldwide containing multiple physical data center clusters.
## Availability Zones (AZs):
- Separate, distinct locations with one or more data centers that 
- are isolated from failures in other areas
## Edge Locations: 
- Locations that cache content to deliver data, video, and applications to users with lower latency


## 5. CloudFormation (IaC tools)
- IaC- define your infrastructure in a file, like a blueprint for your AWS architecture.
- deployments are consistent across different environments.
- deploy the same template in multiple accounts or multiple Regions. 
- less room for human error, totally automated process.
- set up AWS resources using code to automate provisioning and the management of infrastructure. 
- designed to handle complex infrastructure setups. 
