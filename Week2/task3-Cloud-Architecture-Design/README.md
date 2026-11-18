# WeIntern Cloud Computing Internship – Task 3

## AWS Three-Tier E-Commerce Application Architecture

## 1. Project Overview

This project focuses on designing a highly available, scalable, secure, and fault-tolerant three-tier architecture for an e-commerce application using Amazon Web Services (AWS).

The architecture follows AWS best practices by separating the application into three layers:

- Presentation Layer
- Application Layer
- Data Layer

The infrastructure is designed in the AWS Mumbai Region (`ap-south-1`).

## 2. Project Objectives

The main objectives of this project are:

- Design a scalable three-tier cloud architecture.
- Understand AWS networking and VPC components.
- Implement public and private subnet architecture.
- Design secure communication between application layers.
- Understand load balancing and auto-scaling.
- Design a highly available database architecture.
- Implement security, monitoring, and backup strategies.
- Estimate the monthly infrastructure cost using AWS Pricing Calculator.

## 3. Architecture Overview

The application uses a three-tier architecture.

### 3.1 Presentation Layer

The presentation layer handles user requests and displays the website.

AWS services used:

- Amazon Route 53 – DNS management.
- Amazon CloudFront – Content delivery and caching.
- AWS WAF – Web application protection.
- Application Load Balancer (ALB) – Distributes incoming application traffic.
- Amazon S3 – Stores static website content.

### 3.2 Application Layer

The application layer processes business logic and user requests.

AWS services used:

- Amazon EC2 – Runs the application servers.
- EC2 Auto Scaling – Automatically adjusts the number of instances.
- Application Load Balancer – Distributes traffic across application servers.

### 3.3 Data Layer

The data layer stores and manages application data.

AWS services used:

- Amazon RDS for PostgreSQL – Managed relational database.
- Multi-AZ deployment – Provides database high availability.
- Private subnets – Protect database resources from direct internet access.

## 4. AWS Services Used

| AWS Service | Purpose |
|---|---|
| Amazon VPC | Creates an isolated network environment |
| Public Subnets | Hosts internet-facing resources |
| Private Subnets | Hosts application and database resources |
| Internet Gateway | Allows public subnet resources to communicate with the internet |
| NAT Gateway | Allows private subnet resources to access the internet securely |
| Route 53 | DNS management |
| CloudFront | Content delivery network |
| AWS WAF | Protects the application against web attacks |
| Application Load Balancer | Distributes incoming traffic |
| Amazon EC2 | Hosts application servers |
| EC2 Auto Scaling | Automatically scales application instances |
| Amazon S3 | Stores static website files |
| Amazon RDS | Manages the PostgreSQL database |
| IAM | Manages access and permissions |
| CloudWatch | Monitors AWS resources |
| AWS Shield | Provides DDoS protection |

## 5. Network Architecture

### 5.1 AWS Region

- Region: Asia Pacific (Mumbai)
- Region Code: `ap-south-1`

### 5.2 VPC Design

A dedicated Amazon VPC is designed to isolate the application infrastructure.

The VPC contains public and private subnets distributed across multiple Availability Zones.

### 5.3 Subnet Design

The architecture uses the following subnet structure:

| Subnet Type | Purpose |
|---|---|
| Public Subnet 1 | Application Load Balancer and NAT Gateway |
| Public Subnet 2 | Application Load Balancer and NAT Gateway |
| Private Application Subnet 1 | EC2 application instances |
| Private Application Subnet 2 | EC2 application instances |
| Private Database Subnet 1 | RDS database |
| Private Database Subnet 2 | RDS standby database |

### 5.4 Internet Gateway

An Internet Gateway is attached to the VPC to provide internet connectivity to resources in public subnets.

### 5.5 NAT Gateways

Two NAT Gateways are designed in separate Availability Zones to provide internet access to private subnet resources.

This supports availability and allows private application instances to download updates without being directly accessible from the internet.

## 6. Application Request Flow

### 6.1 Dynamic Application Request Flow

The request flow is:

1. The user accesses the e-commerce application.
2. Route 53 resolves the domain name.
3. CloudFront receives the request.
4. AWS WAF inspects incoming traffic.
5. The Application Load Balancer receives and distributes the request.
6. The request is forwarded to an EC2 application instance.
7. The application processes the request.
8. The application communicates with the RDS database.
9. The database returns the required information.
10. The application sends the response back to the user.

### 6.2 Static Content Request Flow

Static content is delivered using Amazon S3 and CloudFront.

1. The user requests static content.
2. CloudFront checks its cache.
3. If the content is cached, CloudFront delivers it directly.
4. If the content is not cached, CloudFront retrieves it from the S3 bucket.
5. CloudFront delivers the content to the user.

Origin Access Control (OAC) is used to restrict direct access to the S3 origin and allow CloudFront to access the bucket securely.

## 7. Compute and Database Design

### 7.1 Amazon EC2

EC2 instances are deployed in private application subnets.

They host the application and process user requests.

### 7.2 EC2 Auto Scaling

Auto Scaling is used to maintain application availability and handle changes in traffic.

It can:

- Add instances when application demand increases.
- Remove instances when demand decreases.
- Replace unhealthy instances.
- Maintain the desired number of running instances.

### 7.3 Application Load Balancer

The Application Load Balancer distributes incoming requests across healthy EC2 instances.

It improves application availability and prevents a single application server from handling all requests.

### 7.4 Amazon RDS PostgreSQL

Amazon RDS for PostgreSQL is used as the managed relational database.

The database is deployed in private database subnets.

### 7.5 Multi-AZ Deployment

Multi-AZ deployment provides high availability by maintaining a standby database in another Availability Zone.

In case of a primary database failure, RDS can automatically fail over to the standby instance.

## 8. Security Architecture

Security is implemented at different layers.

### 8.1 IAM

AWS Identity and Access Management is used to control access to AWS resources.

IAM roles and policies follow the principle of least privilege.

### 8.2 Security Groups

Security Groups control inbound and outbound traffic.

Example security rules:

| Resource | Allowed Traffic |
|---|---|
| Application Load Balancer | HTTP/HTTPS from permitted sources |
| EC2 Instances | Application traffic from the ALB Security Group |
| RDS Database | PostgreSQL traffic from the EC2 Security Group |

The database is not exposed directly to the public internet.

### 8.3 AWS WAF

AWS WAF helps protect the application against common web attacks and unwanted traffic.

### 8.4 AWS Shield

AWS Shield provides protection against Distributed Denial of Service (DDoS) attacks.

### 8.5 Private Subnets

Application and database resources are deployed in private subnets to reduce direct internet exposure.

## 9. High Availability and Scalability

The architecture uses multiple AWS services to improve availability and scalability.

- Resources are distributed across multiple Availability Zones.
- Application Load Balancer distributes traffic across healthy instances.
- EC2 Auto Scaling adjusts application capacity based on demand.
- RDS Multi-AZ supports database availability.
- Two NAT Gateways are designed across separate Availability Zones.
- CloudFront improves content delivery and reduces latency.

## 10. Monitoring and Logging

Amazon CloudWatch is used to monitor AWS infrastructure and application performance.

Monitoring includes:

- EC2 CPU utilization.
- Application Load Balancer metrics.
- Auto Scaling activity.
- RDS database metrics.
- Application health and performance.

CloudWatch alarms can be configured to notify administrators when metrics cross defined thresholds.

## 11. Cost Estimation

AWS Pricing Calculator is used to estimate the monthly cost of the proposed architecture.

The cost estimate considers services such as:

- Amazon EC2
- Application Load Balancer
- Amazon RDS
- NAT Gateways
- Amazon S3
- Amazon CloudFront
- Amazon Route 53
- AWS WAF

Actual costs depend on instance types, storage, data transfer, traffic, deployment configuration, and usage.

The detailed cost estimation report is included in the project documentation.

## 12. Architecture Design Decisions

The following design decisions were made:

1. **Three-tier architecture:** Separates presentation, application, and database responsibilities.
2. **Multiple Availability Zones:** Improves infrastructure availability.
3. **Private application subnets:** Prevents direct public access to application servers.
4. **Private database subnets:** Protects sensitive database resources.
5. **Application Load Balancer:** Distributes traffic across application instances.
6. **Auto Scaling:** Supports changing application traffic.
7. **RDS Multi-AZ:** Improves database availability.
8. **CloudFront and S3:** Supports efficient and secure static content delivery.
9. **IAM and Security Groups:** Restricts access to AWS resources.
10. **CloudWatch:** Supports infrastructure monitoring.

## 13. Documentation and Project Deliverables

All project documentation, architecture diagrams, screenshots, and supporting files are available in the Google Drive folder below.

**Google Drive – Task 3 Documentation and Deliverables:**

[View Task 3 Project Documentation](https://drive.google.com/drive/folders/1K_MgdmBW6T5s7hM4y0SY9FBC8jnhTinU?usp=drive_link)

The folder contains the project materials, including:

- AWS three-tier architecture diagram (PDF).
- Editable architecture diagram (`.drawio`).
- Technical design documentation.
- AWS Pricing Calculator cost estimation report (PDF).
- Project screenshots and supporting evidence.

## 14. Conclusion

This project demonstrates the design of a scalable, secure, and highly available three-tier e-commerce application architecture using AWS services.

The architecture combines networking, compute, storage, database, security, monitoring, and content delivery services.

It demonstrates how AWS services can work together to build a reliable cloud infrastructure that can support an e-commerce application while following cloud architecture best practices.
