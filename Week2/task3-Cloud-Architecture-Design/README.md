# AWS Three-Tier E-Commerce Application Architecture

A secure, scalable, highly available, and cost-optimized three-tier e-commerce architecture designed using Amazon Web Services (AWS).

## 1. Project Overview

The objective of this project is to design a production-oriented cloud architecture for an e-commerce web application using AWS services.

The architecture follows a three-tier model:

1. **Presentation Tier** – Delivers the website interface and static content.
2. **Application Tier** – Processes customer requests and application business logic.
3. **Data Tier** – Stores customer, product, shopping cart, and order information.

The architecture focuses on security, high availability, scalability, performance, and cost optimization.

## 2. Project Objectives

- Design a secure three-tier AWS architecture.
- Deploy network infrastructure using Amazon VPC.
- Distribute resources across two Availability Zones.
- Implement load balancing using Application Load Balancer.
- Configure EC2 Auto Scaling for application scalability.
- Use Amazon RDS Multi-AZ for database availability.
- Store static website content using Amazon S3.
- Deliver content using Amazon CloudFront.
- Implement security using AWS WAF, Shield, Security Groups, and IAM roles.
- Configure NAT Gateways for private subnet outbound connectivity.
- Monitor infrastructure using Amazon CloudWatch.
- Estimate monthly infrastructure costs using AWS Pricing Calculator.

## 3. Application Scenario

**Application:** E-Commerce Website  
**Cloud Provider:** Amazon Web Services (AWS)  
**AWS Region:** Asia Pacific (Mumbai) – `ap-south-1`  
**Availability Zones:** Two Availability Zones

The application allows customers to:

- Browse products.
- View product details and images.
- Add products to shopping carts.
- Register and log in.
- Place orders.
- Store customer and order information.

The infrastructure is designed to support changing traffic levels while maintaining application security and availability.

## 4. Architecture Overview

The infrastructure is deployed inside an Amazon VPC across two Availability Zones.

### 4.1 Application Request Flow

The logical application traffic flow is:

**Customers → Internet → Amazon Route 53 → Amazon CloudFront → AWS WAF → Application Load Balancer → Target Group → EC2 Auto Scaling Group → Amazon RDS**

Route 53 performs DNS resolution, while CloudFront delivers cached content and forwards dynamic requests to the configured application origin.

AWS WAF inspects incoming web requests.

The Application Load Balancer distributes dynamic application traffic across healthy EC2 instances.

### 4.2 Static Content Delivery

Amazon S3 stores static website assets and product images.

CloudFront delivers these files through its globally distributed edge locations.

CloudFront Origin Access Control (OAC) provides secure access to the private S3 bucket.

### 4.3 Architecture Components

| Tier | AWS Services | Purpose |
|---|---|---|
| Presentation Tier | Route 53, CloudFront, S3, AWS WAF | DNS management, security filtering, and static content delivery |
| Application Tier | Application Load Balancer, Target Group, EC2, Auto Scaling | Traffic distribution and application processing |
| Data Tier | Amazon RDS PostgreSQL Multi-AZ | Database storage and management |
| Network Infrastructure | VPC, Internet Gateway, NAT Gateways, Subnets | Network isolation and connectivity |
| Security and Monitoring | AWS Shield, IAM, Security Groups, CloudWatch | Security, access control, and monitoring |

## 5. AWS Services and Their Benefits

### 5.1 Amazon VPC

Amazon Virtual Private Cloud provides an isolated network environment for deploying AWS resources.

**Configuration:**
- One VPC.
- CIDR block: `10.0.0.0/16`.
- Two Availability Zones.
- Two public subnets.
- Two private application subnets.
- Two private database subnets.
- One Internet Gateway.
- Two NAT Gateways.

**Key Benefits:**
- Network isolation.
- Improved security.
- Controlled communication between application tiers.
- High availability across Availability Zones.

### 5.2 Internet Gateway

An Internet Gateway enables communication between the VPC and the Internet.

**Purpose:**
- Provides Internet connectivity to public subnets.
- Allows the internet-facing Application Load Balancer to receive incoming requests.
- Supports Internet connectivity for public-facing AWS resources.

**Key Benefits:**
- Enables communication between the VPC and the Internet.
- Supports public application access.

### 5.3 NAT Gateways

Two NAT Gateways are deployed, one in each Availability Zone.

**Configuration:**
- NAT Gateway 1 in Public Subnet 1.
- NAT Gateway 2 in Public Subnet 2.
- Private application subnets use the NAT Gateway in their respective Availability Zones.

**Purpose:**
- Allows private EC2 instances to access the Internet for software updates.
- Supports outbound communication with external services.
- Prevents unsolicited inbound Internet connections to private instances.

**Key Benefits:**
- Provides outbound Internet connectivity.
- Improves network availability.
- Reduces dependency on a single NAT Gateway.

### 5.4 Amazon Route 53

Amazon Route 53 is an AWS DNS service that translates domain names into IP addresses or routes users to application endpoints.

**Key Benefits:**
- Domain name resolution.
- Reliable DNS routing.
- Health-check-based routing options.

### 5.5 Amazon CloudFront

Amazon CloudFront is an AWS Content Delivery Network (CDN).

It delivers website content through globally distributed edge locations.

**Key Benefits:**
- Faster content delivery.
- Reduced latency.
- Improved website performance.
- Reduced repeated requests to origin servers.

### 5.6 Amazon S3

Amazon Simple Storage Service provides scalable object storage.

**Used to store:**
- HTML files.
- CSS files.
- JavaScript files.
- Product images.
- Logos and static assets.

The S3 bucket remains private, with CloudFront Origin Access Control (OAC) configured for authorized access.

**Key Benefits:**
- Highly durable storage.
- Scalability.
- Secure storage of static assets.

### 5.7 AWS WAF

AWS Web Application Firewall protects web applications by inspecting incoming HTTP/HTTPS requests.

In this architecture, WAF is associated with the CloudFront distribution.

**Key Benefits:**
- Helps block SQL injection attempts.
- Helps protect against cross-site scripting (XSS).
- Filters malicious web requests.
- Provides configurable security rules.

### 5.8 AWS Shield Standard

AWS Shield Standard provides protection against common Distributed Denial of Service (DDoS) attacks.

**Key Benefits:**
- Basic DDoS protection.
- Helps protect supported AWS resources.
- Included at no additional charge.

### 5.9 Application Load Balancer (ALB)

The Application Load Balancer distributes incoming HTTP/HTTPS traffic across healthy application servers.

It operates at Layer 7 of the OSI model.

**Configuration:**
- Internet-facing ALB.
- Deployed across two public subnets.
- HTTPS listener on port 443.
- Target group containing EC2 instances.
- Health checks enabled.

**Key Benefits:**
- Traffic distribution.
- Improved application availability.
- Health-based routing.
- Support for multiple Availability Zones.

### 5.10 Target Group

A Target Group is a collection of registered targets that receive traffic from the load balancer.

In this architecture, EC2 instances are registered as targets.

**Key Benefits:**
- Connects ALB to application servers.
- Performs health checks.
- Routes traffic to healthy instances.

### 5.11 Amazon EC2

Amazon Elastic Compute Cloud provides virtual servers to run application workloads.

**Configuration:**
- Linux-based EC2 instances.
- Deployed in private application subnets.
- Distributed across two Availability Zones.
- Receives application traffic from the ALB.
- No direct public Internet access.

**Key Benefits:**
- Flexible computing capacity.
- Supports application workloads.
- Scalable infrastructure.

### 5.12 EC2 Auto Scaling

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

### 5.13 Amazon RDS for PostgreSQL

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
- Database subnet group across two Availability Zones.
- Private database subnets.
- Automated backups enabled.
- Storage encryption enabled.

**Key Benefits:**
- Managed database administration.
- Automated backup support.
- Database monitoring.
- High availability with Multi-AZ.

### 5.14 RDS Multi-AZ

Multi-AZ maintains a standby database in another Availability Zone for supported configurations.

If the primary database experiences a supported failure, RDS can automatically fail over to the standby database.

**Key Benefits:**
- Improved database availability.
- Automatic failover.
- Reduced downtime during supported failures.

### 5.15 IAM Roles

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

### 5.16 Security Groups

Security Groups act as virtual firewalls for AWS resources.

| Security Group | Port | Allowed Source |
|---|---:|---|
| ALB Security Group | 443 | Intended client traffic or restricted CloudFront origin traffic |
| EC2 Security Group | 8080 | ALB Security Group only |
| RDS Security Group | 5432 | EC2 Security Group only |

Only required traffic should be allowed between tiers.

**Key Benefits:**
- Controls inbound and outbound traffic.
- Prevents unauthorized access.
- Protects application and database resources.

### 5.17 Amazon CloudWatch

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

The VPC is distributed across two Availability Zones in the Mumbai region.

### 6.1 Subnet Configuration

| Availability Zone | Subnet | CIDR Block | Purpose |
|---|---|---|---|
| AZ-A (`ap-south-1a`) | Public Subnet 1 | 10.0.1.0/24 | ALB and NAT Gateway 1 |
| AZ-A (`ap-south-1a`) | Private App Subnet 1 | 10.0.11.0/24 | EC2 application instances |
| AZ-A (`ap-south-1a`) | Private DB Subnet 1 | 10.0.21.0/24 | RDS database subnet group |
| AZ-B (`ap-south-1b`) | Public Subnet 2 | 10.0.2.0/24 | ALB and NAT Gateway 2 |
| AZ-B (`ap-south-1b`) | Private App Subnet 2 | 10.0.12.0/24 | EC2 application instances |
| AZ-B (`ap-south-1b`) | Private DB Subnet 2 | 10.0.22.0/24 | RDS database subnet group |

### 6.2 Network Traffic Flow

| Source | Destination | Purpose |
|---|---|---|
| Internet | Internet Gateway | VPC Internet connectivity |
| Internet Gateway | Public Subnets | Public resource connectivity |
| Application Load Balancer | EC2 Instances | Application traffic |
| EC2 Instances | NAT Gateways | Outbound Internet access |
| EC2 Instances | Amazon RDS | Database communication |
| CloudFront | Amazon S3 | Static content delivery |
| CloudFront | ALB | Dynamic application requests |

### 6.3 Routing Configuration

- Public subnet route tables use the Internet Gateway for Internet-bound traffic.
- Private application subnet route tables use their respective NAT Gateways for outbound Internet access.
- Private database subnet route tables do not have direct Internet routes.
- Application instances communicate with RDS through private network connectivity.

## 7. Security Architecture

Security is implemented through multiple layers.

| Security Component | Purpose |
|---|---|
| AWS WAF | Filters malicious web requests |
| AWS Shield Standard | Provides basic DDoS protection |
| Security Groups | Controls network traffic |
| IAM Roles | Provides controlled AWS permissions |
| Private Subnets | Protects internal resources from direct Internet access |
| S3 OAC | Provides authorized CloudFront access to private S3 content |
| Encryption | Protects data at rest and in transit |

**Additional Security Recommendations:**
- Enable encryption at rest and in transit.
- Do not expose RDS publicly.
- Avoid opening SSH access to everyone.
- Use least-privilege IAM policies.
- Prefer Systems Manager Session Manager for EC2 administration.
- Restrict ALB origin access to CloudFront when CloudFront is the intended public entry point.
- Store database credentials securely using AWS Secrets Manager or another approved secrets-management solution.

## 8. High Availability and Scalability

The architecture uses multiple AWS services to improve application availability and handle changing application demand.

| AWS Component | High Availability / Scalability Approach |
|---|---|
| VPC | Resources distributed across two Availability Zones |
| Internet Gateway | Provides Internet connectivity to the VPC |
| NAT Gateways | One NAT Gateway in each Availability Zone |
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
- Application logs.

CloudWatch alarms can notify administrators when configured thresholds are exceeded.

Monitoring helps identify infrastructure failures, performance problems, and unusual resource utilization.

## 10. Monthly AWS Cost Estimate

The current AWS Pricing Calculator estimate is:

| AWS Service | Estimated Monthly Cost (USD) |
|---|---:|
| AWS Shield Standard | $0.00 |
| AWS WAF | $0.00* |
| Amazon CloudFront | $0.50 |
| Application Load Balancer | $19.45 |
| Amazon EC2 | $7.96 |
| Amazon RDS Multi-AZ | $146.65 |
| Amazon S3 | $1.25 |
| Amazon Route 53 | $0.00* |
| Amazon CloudWatch | $0.00* |
| **Total Initial Estimate** | **$175.81** |

### Cost Notes

- These costs are estimates based on the current calculator configuration.
- A $0 estimate does not necessarily mean a service is always free.
- AWS WAF, Route 53, and CloudWatch may incur charges depending on usage and configuration.
- Verify that the EC2 estimate includes the intended number of running instances across both Availability Zones.
- Both NAT Gateways introduce hourly and data-processing charges.
- Public IPv4 addresses and data transfer may also incur charges.
- RDS Multi-AZ, storage, and backup usage affect the final cost.

**Important:** The $175.81 figure is the initial estimate, not a verified final cost for the complete architecture. The final estimate must be recalculated after including two NAT Gateways, the intended EC2 instance count, and all other required resources.

Cost optimization can be achieved through appropriate instance sizing, Auto Scaling, monitoring, and CloudFront caching.

## 11. Design Decisions and Trade-offs

| Design Decision | Reason | Trade-off |
|---|---|---|
| Two Availability Zones | Improves availability | Additional infrastructure cost |
| Application Load Balancer | Distributes application traffic | Hourly and usage charges |
| EC2 Auto Scaling | Automatically adjusts capacity | Requires scaling policies |
| RDS Multi-AZ | Improves database availability | Higher cost than Single-AZ |
| Two NAT Gateways | Provides AZ-level outbound redundancy | Additional NAT Gateway charges |
| S3 and CloudFront | Improves static content delivery | Storage and data transfer charges |
| Private Subnets | Protects internal resources | Requires outbound networking planning |
| AWS WAF | Filters malicious web traffic | Additional configuration and possible charges |
| IAM Roles | Provides controlled AWS access | Requires permission management |

## 12. Project Deliverables

The project includes the following deliverables:

1. **AWS Architecture Diagram (PDF)** – Visual representation of the three-tier AWS architecture.
2. **Editable Architecture Diagram (.drawio)** – Editable source architecture diagram.
3. **Technical Design Document (README.md)** – Explanation of AWS components, network infrastructure, security, scalability, and design decisions.
4. **AWS Pricing Calculator Report (PDF)** – Estimated monthly infrastructure costs.

## 13. Conclusion

The proposed AWS Three-Tier E-Commerce Application Architecture provides a foundation for hosting a secure, scalable, and highly available web application.

The design separates presentation, application, and data workloads into independent tiers.

AWS services such as Application Load Balancer, EC2 Auto Scaling, Amazon RDS Multi-AZ, S3, CloudFront, WAF, Shield, IAM, and CloudWatch work together to provide performance, security, and reliability.

The architecture uses two Availability Zones, separate public and private subnets, and two NAT Gateways to improve network availability and resource isolation.

The design also considers cost optimization through managed services, scalable computing resources, and CDN-based content delivery.

Before production deployment, the architecture should be validated through security reviews, load testing, backup and recovery testing, failover testing, and an updated cost estimate based on actual workload requirements.

---


