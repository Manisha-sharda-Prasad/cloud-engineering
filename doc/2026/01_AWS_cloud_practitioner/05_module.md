## 1. Introduction to Networking in AWS:-
- Interconnected devices that can exchange data and resources

## 1.1.Subnets:
- used to organize resources, share resources publicly, or isolate resources to keep them private.

## Private subnets
- e.g. database that contains customers’ personal information and order histories.
- designed to isolate resources that shouldn't be directly exposed to the public internet.
## Public subnets 
- e.g. online store’s website,
- designed to provide direct internet access to resources placed inside them. 
- allowing access, they are connected with an internet gateway.



## 2. Boundaries around AWS resources:-

## 2.1.Amazon Virtual Private Cloud (VPC):
- VPC is used to establish boundaries around your AWS resources.
- solid box, and it represents your isolated, logically segmented network within AWS.
- it helps you to control your network resources and security.

## 2.2. Virtual private gateway:
- A virtual private gateway allows protected internet traffic to enter into the VPC.

## 2.3. Virtual private network(VPN):
- A VPN encrypts your internet traffic,
- helps protect it from anyone who might try to intercept or monitor it.



## 3. More Ways to Connect to the AWS Cloud :-

## 3.1. AWS Direct Connect 
- is a private, dedicated AWS connection to your data center or office.
- takes time to set up,
- not designed for remote worker.

## 3.2. AWS Client VPN 
- connects your remote workforce to AWS or on-premises with a VPN.
- ideal for a newly expanded worldwide remote workforce.

## 3.3. AWS Site-to-Site VPN 
- connect branch offices or data centers (fixed locations)
- not ideal for remote workers.
- is an encrypted network connection to your Amazon VPCs.

## 3.4. AWS PrivateLink 
- private connectivity between VPCs, AWS services, and on-premises applications 
- without exposing traffic to the public internet
- connects your VPC privately to services and resources as though they were in your VPC.



## 4. Network traffic in a VPC :-

- The movement of data packets traveling across a network
- A packet is a unit of data sent over the internet or a network.
- It enters into a VPC through an internet gateway. 
- Before a packet enter or exit from a subnet, it will run into several checks for permissions,
- If permissions defined, ACLs indicate what is allowed or denied.

## 4.1.  Network ACLs (Access Control Lists) :
- operate at the subnet level,
- Virtual firewall controlling traffic
- evaluating traffic before it enters or leaves a subnet,
- perform stateless packet filtering, remember nothing and check packets that cross the subnet border each way: inbound and outbound.
- When configuring your VPC, you can use your account’s default network ACL or create custom network ACLs.
- you can modify it by adding your own rules.

## 4.2. Security groups :
- operate at the instance level, 
- Virtual firewall for individual EC2 instances
- Control inbound and outbound traffic 
- add custom rules to configure which traffic should be allowed.
- It is the VPC component that checks packet permissions for an Amazon EC2 instance. 




## 5. Create an Internet Gateway and Route Traffic :

- First, create the internet gateway. Other-wise your users can't get to your resources. 
- Then, create route tables to route traffic,
- It allows internet traffic in and local traffic out.



## 6. Three Edge networking services :-
- important because organizations need lower latency,
- fast access to their data and content.
- tasks like caching data locally or closer to users, deliver faster.

## Translating domain names to IP addresses with DNS :-
- DNS is like the phone book of the internet. 
- DNS is the process of translating a domain name to an IP address.
- Customer enters web address and able to access the website, because of DNS resolution.

## 6.1. Amazon Route 53 :
- Is DNS that provides a reliable and cost-effective way to route end users to internet applications.
- connects user requests to infrastructure running in AWS, e.g.Amazon EC2 instances and load balancers. 
- also routes to infrastructure outside of AWS.
- ability to manage all the DNS records for domain names in single service.
- register new domain names directly in Route 53. 

## 6.2. Amazon CloudFront :
- content delivery network (CDN) service, delivers your content with faster loading times,cost savings.
- global network of delivery trucks that quickly brings web content to users around the world. 
- stores copies of your content at locations closer to your users. 
- means websites, videos, images, and applications load much faster, no matter where your customers are located.
- e.g. websites : streaming-workout videos, ecommerce-shopping, mobile-map data  

## 6.3. AWS Global Accelerator :
- uses intelligent traffic routing and fast failover if something goes wrong in your 1 application locations.
- networking service that helps your applications run faster  across the globe. 
- user requests through regular congested internet route, It creates express lane on the internet highway
- getting users to your application faster and more reliably.
- e.g. Gaming company - lag free gameplay; Banking app - fastaccess to accounts.

## 7. AWS Direct Connect 
- when lots of data needs to flow between corporate data centers and AWS. 
- huge data transfers can take a long time over the public Internet, opt for Direct Connect instead.
- use when need much higher bandwidth with a dedicated line like large data transfers between your on-premises network and AWS.