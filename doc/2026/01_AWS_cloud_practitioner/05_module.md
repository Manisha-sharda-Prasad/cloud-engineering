## 1. Introduction to Networking:-

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

## AWS Direct Connect 
- is a private, dedicated AWS connection to your data center or office.

## AWS Client VPN 
- connects your remote workforce to AWS or on-premises with a VPN.

## AWS Site-to-Site VPN 
- is an encrypted network connection to your Amazon VPCs.

## AWS PrivateLink 
- connects your VPC privately to services and resources as though they were in your VPC.


## 4. Network traffic in a VPC :-

- The movement of data packets traveling across a network
- A packet is a unit of data sent over the internet or a network.
- It enters into a VPC through an internet gateway. 
- Before a packet enter or exit from a subnet, it will run into several checks for permissions,
- If permissions defined, ACLs indicate what is allowed or denied.

## 5. Network ACLs (Virtual firewall controlling traffic) :-
- When configuring your VPC, you can use your account’s default network ACL or create custom network ACLs.
- your account’s default network ACL allows all inbound and outbound traffic, 
- you can modify it by adding your own rules.