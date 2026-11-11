# AWS Three-Tier E-Commerce Application

A secure, scalable, highly available and cost-optimized three-tier e-commerce architecture designed using Amazon Web Services (AWS).

## 1. Project Overview

The objective of this project is to design a production-ready cloud architecture for an e-commerce web application using AWS services.

The architecture follows a three-tier model:

1. **Presentation Tier** – Delivers the website interface and static content.
2. **Application Tier** – Processes customer requests and application business logic.
3. **Data Tier** – Stores customer, product, shopping cart and order information.

The architecture focuses on security, high availability, scalability, performance and cost optimization.

## 2. Project Objectives

- Design a three-tier web application architecture.
- Implement load balancing for high availability.
- Configure EC2 Auto Scaling for the application tier.
- Use Amazon RDS Multi-AZ for database availability.
- Use Amazon S3 and CloudFront for static content delivery.
- Implement security using AWS WAF, Shield, Security Groups and IAM roles.
- Estimate monthly infrastructure costs using AWS Pricing Calculator.

## 3. Application Scenario

**Application:** E-Commerce Website  
**AWS Region:** Asia Pacific (Mumbai) – `ap-south-1`

The application allows customers to:
- Browse products.
- View product details and images.
- Add products to shopping carts.
- Register and log in.
- Place orders.
- Store customer and order information.

## 4. Architecture Overview

The infrastructure is deployed inside an Amazon VPC across two Availability Zones.

### Request Flow

**Customer → Route 53 → CloudFront / AWS WAF → Application Load Balancer → Target Group → EC2 Auto Scaling → Amazon RDS**

Amazon S3 stores static website assets and product images. CloudFront delivers these assets through its global edge locations.

### Architecture Tiers

| Tier | AWS Services | Purpose |
|---|---|---|
| Presentation Tier | Route 53, CloudFront, S3 | DNS management and static content delivery |
| Application Tier | ALB, Target Group, EC2, Auto Scaling | Traffic distribution and application processing |
| Data Tier | Amazon RDS PostgreSQL | Database storage and management |

## 5. AWS Services and Their Benefits

### 5.1 Amazon VPC

Amazon Virtual Private Cloud provides an isolated network environment for AWS resources.

**Configuration:**
- One VPC.
- Two Availability Zones.
- Two public subnets.
- Two private application subnets.
- Two private database subnets.

**Key Benefits:**
- Network isolation.
- Improved security.
- Controlled communication between application tiers.

### 5.2 Amazon Route 53

Route 53 is an AWS DNS service that translates domain names into IP addresses or routes users to application endpoints.

**Key Benefits:**
- Domain name resolution.
- Reliable DNS routing.
- Health-check-based routing options.

### 5.3 Amazon CloudFront

CloudFront is an AWS Content Delivery Network (CDN).

It delivers website content through globally distributed edge locations.

**Key Benefits:**
- Faster content delivery.
- Reduced latency.
- Improved website performance.
- Reduced load on origin servers.

### 5.4 Amazon S3

Amazon Simple Storage Service provides scalable object storage.

**Used to store:**
- HTML files.
- CSS files.
- JavaScript files.
- Product images.
- Logos and static assets.

The S3 bucket should remain private, with CloudFront Origin Access Control (OAC) configured for authorized access.

**Key Benefits:**
- Highly durable storage.
- Scalability.
- Secure storage of static assets.

### 5.5 Application Load Balancer (ALB)

The Application Load Balancer distributes incoming HTTP/HTTPS traffic across healthy application servers.

**Configuration:**
- Internet-facing ALB.
- Two public subnets.
- HTTPS listener on port 443.
- Target group containing EC2 instances.
- Health checks enabled.

**Key Benefits:**
- Traffic distribution.
- Improved application availability.
- Health-based routing.

### 5.6 Target Group

A target group is a collection of registered targets that receive traffic from the load balancer.

In this architecture, EC2 instances are registered as targets.

**Key Benefits:**
- Connects ALB to application servers.
- Performs health checks.
- Routes traffic to healthy instances.

### 5.7 Amazon EC2

Amazon Elastic Compute Cloud provides virtual servers to run application workloads.

**Configuration:**
- Linux-based EC2 instances.
- Deployed in private application subnets.
- Receives traffic from the ALB.
- No direct public access.

**Key Benefits:**
- Flexible computing capacity.
- Supports application workloads.
- Scalable infrastructure.

### 5.8 EC2 Auto Scaling

EC2 Auto Scaling automatically adjusts the number of instances based on configured scaling policies.

**Example Configuration:**

| Setting | Value |
|---|---:|
| Minimum Capacity | 2 |
| Desired Capacity | 2 |
| Maximum Capacity | 4 |

These are proposed design assumptions and should be validated against workload requirements.

**Key Benefits:**
- Automatically increases capacity.
- Reduces capacity when demand decreases.
- Replaces unhealthy instances.
- Helps optimize compute costs.

### 5.9 Amazon RDS for PostgreSQL

Amazon Relational Database Service (RDS) is a managed relational database service.

PostgreSQL is selected for storing structured e-commerce information.

**Data Stored:**
- Customer details.
- Product information.
- Shopping cart records.
- Order information.
- Transaction records.

**Configuration:**
- Database engine: PostgreSQL.
- Deployment: Multi-AZ.
- Private database subnets.
- Automated backups enabled.
- Encryption enabled.

**Key Benefits:**
- Managed database administration.
- Automated backup support.
- Database monitoring.
- High availability with Multi-AZ.

### 5.10 RDS Multi-AZ

Multi-AZ maintains a standby database in another Availability Zone for supported configurations.

If the primary database experiences a supported failure, RDS can automatically fail over to the standby database.

**Key Benefits:**
- Improved database availability.
- Automatic failover.
- Reduced downtime during supported failures.

### 5.11 AWS WAF

AWS Web Application Firewall protects web applications by inspecting incoming HTTP/HTTPS requests.

**Key Benefits:**
- Helps block SQL injection attempts.
- Helps protect against cross-site scripting (XSS).
- Filters malicious web requests.
- Provides configurable security rules.

### 5.12 AWS Shield Standard

AWS Shield Standard provides protection against common Distributed Denial of Service (DDoS) attacks.

**Key Benefits:**
- Basic DDoS protection.
- Helps protect supported AWS resources.
- Included at no additional charge.

### 5.13 IAM Roles

AWS Identity and Access Management controls permissions to AWS resources.

EC2 IAM roles provide application instances with temporary permissions to access required AWS services.

**Examples:**
- Access to required S3 resources.
- CloudWatch logging permissions.
- Systems Manager permissions, if required.

**Key Benefits:**
- Secure access management.
- No need to store long-term access keys on EC2.
- Least-privilege permissions.

### 5.14 Security Groups

Security Groups act as virtual firewalls for AWS resources.

| Security Group | Port | Allowed Source |
|---|---:|---|
| ALB Security Group | 443 | Intended client traffic or CloudFront origin traffic |
| EC2 Security Group | 8080 | ALB Security Group only |
| RDS Security Group | 5432 | EC2 Security Group only |

Only required traffic should be allowed between tiers.

**Key Benefits:**
- Controls inbound and outbound traffic.
- Prevents unauthorized access.
- Protects application and database resources.

### 5.15 Amazon CloudWatch

Amazon CloudWatch monitors AWS resources and application performance.

**Monitoring Metrics:**
- EC2 CPU utilization.
- ALB request count.
- ALB response time.
- Unhealthy target count.
- RDS CPU utilization.
- Database connections.
- Application logs.

**Key Benefits:**
- Infrastructure monitoring.
- Log collection.
- Performance tracking.
- Configurable alarms and alerts.

## 6. Network and Subnet Design

The VPC is distributed across two Availability Zones.

| Availability Zone | Subnet | Purpose |
|---|---|---|
| AZ 1 | Public Subnet 1 | Application Load Balancer |
| AZ 1 | Private App Subnet 1 | EC2 application instances |
| AZ 1 | Private DB Subnet 1 | RDS database subnet group |
| AZ 2 | Public Subnet 2 | Application Load Balancer |
| AZ 2 | Private App Subnet 2 | EC2 application instances |
| AZ 2 | Private DB Subnet 2 | RDS database subnet group |

Private application instances may require outbound internet access for updates or external integrations. NAT Gateways or VPC endpoints should be considered according to requirements.

## 7. Security Architecture

Security is implemented through multiple layers:

| Security Component | Purpose |
|---|---|
| AWS WAF | Filters malicious web requests |
| AWS Shield Standard | Provides basic DDoS protection |
| Security Groups | Controls network traffic |
| IAM Roles | Provides controlled AWS permissions |
| Private Subnets | Protects internal resources from direct internet access |
| S3 OAC | Provides authorized CloudFront access to private S3 content |

Additional recommendations:
- Enable encryption at rest and in transit.
- Do not expose RDS publicly.
- Avoid opening SSH to everyone.
- Use least-privilege IAM policies.
- Prefer Systems Manager Session Manager for administration.

## 8. High Availability and Scalability

| AWS Component | Approach |
|---|---|
| VPC | Resources distributed across two Availability Zones |
| Application Load Balancer | Distributes traffic across healthy targets |
| EC2 Auto Scaling | Adjusts application capacity based on demand |
| RDS Multi-AZ | Provides standby database and automatic failover |
| CloudFront | Uses global edge locations for content delivery |
| Amazon S3 | Provides durable object storage |

These components help reduce single points of failure and support changing application demand.

## 9. Monitoring

Amazon CloudWatch is used to monitor infrastructure and application performance.

Important metrics include:
- EC2 CPU utilization.
- ALB request count and response time.
- Unhealthy target count.
- RDS CPU utilization.
- Database connections.

CloudWatch alarms can notify administrators when configured thresholds are exceeded.

## 10. Monthly AWS Cost Estimate

The current AWS Pricing Calculator estimate is:

| AWS Service | Estimated Monthly Cost (USD) |
|---|---:|
| AWS Shield Standard | $0.00 |
| AWS WAF | $0.00 |
| Amazon CloudFront | $0.50 |
| Application Load Balancer | $19.45 |
| Amazon EC2 | $7.96 |
| Amazon RDS Multi-AZ | $146.65 |
| Amazon S3 | $1.25 |
| Amazon Route 53 | $0.00 |
| Amazon CloudWatch | $0.00 |
| **Total Estimated Monthly Cost** | **$175.81** |

**Cost Notes:**
- These costs are estimates based on the current calculator configuration.
- A $0 estimate does not necessarily mean a service is always free.
- WAF, Route 53 and CloudWatch may incur charges depending on usage and configuration.
- Verify that the EC2 estimate includes the intended number of running instances across both Availability Zones.
- NAT Gateways, data transfer, public IPv4 addresses and other required components should also be included where applicable.
- Actual costs may vary depending on usage and AWS pricing.

## 11. Design Decisions and Trade-offs

| Design Decision | Reason | Trade-off |
|---|---|---|
| Two Availability Zones | Improves availability | Additional infrastructure cost |
| Application Load Balancer | Distributes application traffic | Hourly and usage charges |
| EC2 Auto Scaling | Automatically adjusts capacity | Requires scaling policies |
| RDS Multi-AZ | Improves database availability | Higher cost than Single-AZ |
| S3 and CloudFront | Improves static content delivery | Storage and data transfer charges |
| Private Subnets | Protects internal resources | Requires outbound networking planning |
| AWS WAF | Filters malicious web traffic | Additional configuration and possible charges |
| IAM Roles | Provides controlled AWS access | Requires permission management |

## 12. Project Deliverables

The project includes the following deliverables:

1. **Architecture Diagram (PDF)** – Visual representation of the three-tier AWS architecture.
2. **Editable Architecture Diagram (.drawio)** – Editable source diagram.
3. **Technical Design Document (README.md)** – Explanation of all AWS components, security, scalability and design decisions.
4. **AWS Pricing Calculator Report (PDF)** – Estimated monthly infrastructure cost.

## 13. Conclusion

The proposed AWS three-tier e-commerce architecture provides a foundation for a secure, scalable and highly available web application.

The design separates presentation, application and data workloads.

AWS services such as Application Load Balancer, EC2 Auto Scaling, Amazon RDS Multi-AZ, S3, CloudFront, WAF and Shield work together to provide performance, security and reliability.

The architecture also considers cost optimization through managed services, scalable computing resources and CDN-based content delivery.

Before production deployment, the design should be validated through security reviews, load testing, backup and recovery testing, and an updated cost estimate based on actual workload requirements.
