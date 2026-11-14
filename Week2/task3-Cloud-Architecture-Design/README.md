# AWS Three-Tier E-Commerce Application Architecture

A secure, scalable, highly available, and cost-optimized three-tier e-commerce architecture designed using Amazon Web Services (AWS).

---

## 1. Project Overview

The objective of this project is to design a production-oriented cloud architecture for an e-commerce web application using Amazon Web Services (AWS).

The proposed architecture follows a three-tier model:

1. **Presentation Tier** – Delivers the website interface and static content to customers.
2. **Application Tier** – Processes customer requests and application business logic.
3. **Data Tier** – Stores customer, product, shopping cart, and order information.

The architecture focuses on security, high availability, scalability, performance, and cost optimization.

## 2. Project Objectives

- Design a secure three-tier AWS architecture.
- Create network infrastructure using Amazon VPC.
- Distribute resources across two Availability Zones.
- Configure an Application Load Balancer.
- Deploy EC2 instances in private application subnets.
- Implement EC2 Auto Scaling.
- Use Amazon RDS PostgreSQL with Multi-AZ deployment.
- Store static content using Amazon S3.
- Deliver content using Amazon CloudFront.
- Implement security using AWS WAF, Shield, Security Groups, and IAM.
- Configure two NAT Gateways for private subnet connectivity.
- Monitor infrastructure using Amazon CloudWatch.
- Estimate monthly infrastructure costs using AWS Pricing Calculator.

## 3. Application Scenario

| Item | Details |
|---|---|
| Application | E-Commerce Website |
| Cloud Provider | Amazon Web Services |
| AWS Region | Asia Pacific (Mumbai) |
| Region Code | `ap-south-1` |
| Availability Zones | 2 |
| Architecture | Three-Tier Architecture |
| Database | PostgreSQL |

### Application Features

The e-commerce application allows customers to:

- Browse available products.
- View product details and images.
- Register and log in.
- Add products to shopping carts.
- Place orders.
- Store customer and order information.

## 4. Architecture Overview

The infrastructure is deployed inside an Amazon VPC across two Availability Zones in the Mumbai region.

The architecture uses AWS networking, compute, storage, database, security, and monitoring services.

### 4.1 Dynamic Application Request Flow

The logical request flow is:

**Customer → Internet → Route 53 (DNS Resolution) → CloudFront → AWS WAF → Application Load Balancer → Target Group → EC2 Instances → Amazon RDS**

- **Amazon Route 53:** Resolves the application domain name and directs users to CloudFront.
- **Amazon CloudFront:** Delivers content through globally distributed edge locations.
- **AWS WAF:** Inspects and filters incoming web requests according to configured security rules.
- **Application Load Balancer:** Distributes application traffic across healthy EC2 instances.
- **Target Group:** Registers EC2 instances and performs health checks.
- **Amazon EC2:** Processes application requests and business logic.
- **Amazon RDS:** Stores application data.

AWS WAF is associated with CloudFront to inspect incoming viewer requests. The Internet Gateway provides VPC connectivity for the public-facing ALB; it is not an application-layer step in the request flow.

### 4.2 Static Content Delivery

Amazon S3 stores static website files and product images.

CloudFront delivers static content through globally distributed edge locations.

CloudFront Origin Access Control (OAC) allows CloudFront to access the private S3 bucket without making the bucket publicly accessible.

**Static content flow:**

**Customer → Route 53 → CloudFront → Private Amazon S3 Bucket (using OAC)**

### 4.3 Architecture Components

| Tier | AWS Services | Purpose |
|---|---|---|
| Presentation | Route 53, CloudFront, S3, WAF | DNS resolution, content delivery, and web security |
| Application | ALB, Target Group, EC2, Auto Scaling | Traffic distribution and application processing |
| Data | Amazon RDS PostgreSQL | Database storage |
| Networking | VPC, Subnets, IGW, NAT Gateways | Network connectivity |
| Security | Shield, IAM, Security Groups | Infrastructure and access protection |
| Monitoring | Amazon CloudWatch | Metrics, logs, alarms, and performance monitoring |

## 5. AWS Services and Configuration

### 5.1 Amazon VPC

Amazon Virtual Private Cloud provides an isolated network environment for deploying AWS resources.

**Configuration:**

- VPC CIDR: `10.0.0.0/16`
- Two Availability Zones.
- Two public subnets.
- Two private application subnets.
- Two private database subnets.
- One Internet Gateway.
- Two NAT Gateways.

**Benefits:**

- Network isolation.
- Improved security.
- Controlled communication between application tiers.
- Availability across two Availability Zones.

### 5.2 Internet Gateway

An Internet Gateway connects the VPC to the Internet.

**Purpose:**

- Provides Internet connectivity to public subnets.
- Allows the internet-facing Application Load Balancer to receive incoming traffic.
- Supports communication between public resources and the Internet.

### 5.3 NAT Gateways

Two NAT Gateways are deployed, one in each Availability Zone.

**Configuration:**

| NAT Gateway | Placement |
|---|---|
| NAT Gateway 1 | Public Subnet 1 – AZ-A |
| NAT Gateway 2 | Public Subnet 2 – AZ-B |

Each private application subnet uses the NAT Gateway in its respective Availability Zone.

**Benefits:**

- Allows private EC2 instances to access the Internet for outbound connections.
- Supports software updates and external service communication.
- Prevents unsolicited inbound Internet connections.
- Reduces dependency on a single NAT Gateway.

NAT Gateways incur hourly and data-processing charges.

### 5.4 Amazon Route 53

Amazon Route 53 is an AWS DNS service.

**Benefits:**

- Domain name resolution.
- DNS routing.
- Health-check-based routing options.
- Integration with CloudFront.

Route 53 resolves the application domain name and directs users to the CloudFront distribution.

### 5.5 Amazon CloudFront

Amazon CloudFront is an AWS Content Delivery Network (CDN).

**Benefits:**

- Faster content delivery.
- Reduced latency.
- Improved website performance.
- Reduced origin requests through caching.
- Integration with AWS WAF.

CloudFront uses Amazon S3 for static content and the Application Load Balancer for dynamic application requests.

### 5.6 Amazon S3

Amazon Simple Storage Service provides scalable object storage.

**Used to store:**

- HTML files.
- CSS files.
- JavaScript files.
- Product images.
- Logos and static assets.

The S3 bucket remains private and uses CloudFront Origin Access Control (OAC).

**Benefits:**

- Durable object storage.
- Scalable storage capacity.
- Secure content delivery through CloudFront.
- Reduced load on application servers.

### 5.7 AWS WAF

AWS Web Application Firewall protects web applications by inspecting HTTP and HTTPS requests.

**Benefits:**

- Helps protect against SQL injection.
- Helps protect against cross-site scripting (XSS).
- Filters malicious web requests.
- Supports configurable security rules.
- Can be associated with CloudFront.

### 5.8 AWS Shield Standard

AWS Shield Standard provides basic protection against common Distributed Denial of Service (DDoS) attacks.

**Benefits:**

- Basic DDoS protection.
- Protection for supported AWS resources.
- Included at no additional charge.

### 5.9 Application Load Balancer (ALB)

The Application Load Balancer distributes incoming application traffic across healthy EC2 instances.

**Configuration:**

- One internet-facing ALB.
- Deployed across two public subnets.
- HTTPS listener on port `443`.
- Target group connected to EC2 instances.
- Health checks enabled.

**Benefits:**

- Traffic distribution.
- Improved application availability.
- Health-based routing.
- Multi-AZ support.

### 5.10 Target Group

The Target Group connects the Application Load Balancer to EC2 instances.

**Benefits:**

- Registers application servers.
- Performs health checks.
- Routes traffic to healthy targets.
- Supports integration with Auto Scaling.

The application servers listen on port `8080` in this design.

### 5.11 Amazon EC2

Amazon Elastic Compute Cloud provides virtual servers for application workloads.

**Configuration:**

| Setting | Configuration |
|---|---|
| Instance Type | `t2.micro` |
| Operating System | Linux |
| Initial Instance Count | 2 |
| Deployment | Private Application Subnets |
| Availability Zones | 2 |
| Application Port | 8080 |
| Access | Through Application Load Balancer |

**Benefits:**

- Runs application workloads.
- Provides flexible computing capacity.
- Supports scalable application deployment.
- Keeps application servers private.

### 5.12 EC2 Auto Scaling

EC2 Auto Scaling automatically adjusts the number of instances based on configured scaling policies and health checks.

**Example Configuration:**

| Setting | Value |
|---|---:|
| Minimum Capacity | 2 |
| Desired Capacity | 2 |
| Maximum Capacity | 4 |

**Benefits:**

- Automatically increases capacity when demand increases.
- Replaces unhealthy instances.
- Reduces capacity when demand decreases, subject to minimum capacity.
- Helps optimize computing costs.

The two EC2 instances represent the initial desired capacity. Auto Scaling can increase the number of instances up to four when required.

### 5.13 Amazon RDS for PostgreSQL

Amazon Relational Database Service (RDS) is a managed relational database service.

PostgreSQL is selected to store structured e-commerce information.

**Configuration:**

| Setting | Configuration |
|---|---|
| Database Engine | PostgreSQL |
| Instance Class | `db.t3.micro` (cost estimate assumption) |
| Deployment | Multi-AZ |
| Database Subnets | Private Database Subnets |
| Availability Zones | 2 |
| Automated Backups | Enabled |
| Encryption | Enabled |

**Data Stored:**

- Customer details.
- Product information.
- Shopping cart records.
- Order information.
- Transaction records.

**Benefits:**

- Managed database administration.
- Automated backups.
- Database monitoring.
- High availability with Multi-AZ deployment.

### 5.14 RDS Multi-AZ

RDS Multi-AZ maintains a standby database in another Availability Zone for supported configurations.

If the primary database experiences a supported failure, Amazon RDS can automatically fail over to the standby database.

**Benefits:**

- Improved database availability.
- Automatic failover.
- Reduced downtime during supported failures.
- Improved database infrastructure resilience.

The standby database is intended for failover and is not used for ordinary read scaling.

### 5.15 IAM Roles

AWS Identity and Access Management controls access to AWS resources.

EC2 IAM roles provide temporary permissions to application instances.

**Examples:**

- Access to required S3 resources.
- CloudWatch logging permissions.
- AWS Systems Manager permissions.

**Benefits:**

- Secure access management.
- No need for long-term access keys on EC2.
- Least-privilege permissions.
- Better control over AWS resource access.

### 5.16 Security Groups

Security Groups act as virtual firewalls for AWS resources.

**Security Group Configuration:**

| Security Group | Port | Allowed Source |
|---|---:|---|
| ALB Security Group | 443 | Intended client traffic |
| EC2 Security Group | 8080 | ALB Security Group |
| RDS Security Group | 5432 | EC2 Security Group |

Only required traffic should be allowed between tiers.

If CloudFront is intended to be the only public entry point, restrict direct access to the ALB origin using appropriate origin protection and security group rules.

### 5.17 Amazon CloudWatch

Amazon CloudWatch is an AWS monitoring and observability service used to monitor infrastructure and application performance.

**Monitoring Components:**

| AWS Resource | Monitoring Details |
|---|---|
| Application Load Balancer | Request count, response time, HTTP errors |
| EC2 Instances | CPU utilization and status checks |
| Auto Scaling Group | Scaling activities and instance health |
| Amazon RDS | CPU utilization, database connections, and storage |
| Application | Application logs and errors |

**CloudWatch Features:**

- CloudWatch Metrics – Collects infrastructure performance metrics.
- CloudWatch Logs – Collects and stores application and system logs.
- CloudWatch Alarms – Monitors configured thresholds and triggers notifications or actions.

**Benefits:**

- Infrastructure monitoring.
- Log collection and analysis.
- Performance tracking.
- Configurable alarms.
- Early identification of potential issues.

**Architecture Placement:**

CloudWatch is a regional AWS service. It is placed inside the AWS Region boundary but outside the VPC boundary in the architecture diagram.

It does not need to be deployed inside a public or private subnet.

Dashed monitoring connections should connect CloudWatch to the ALB, EC2 instances, Auto Scaling Group, and RDS.

## 6. Network and Subnet Design

The VPC is distributed across two Availability Zones in the Mumbai region.

### 6.1 VPC and Subnet Configuration

| Availability Zone | Subnet | CIDR Block | Purpose |
|---|---|---|---|
| AZ-A | Public Subnet 1 | `10.0.1.0/24` | ALB and NAT Gateway 1 |
| AZ-A | Private App Subnet 1 | `10.0.11.0/24` | EC2 application server 1 |
| AZ-A | Private DB Subnet 1 | `10.0.21.0/24` | RDS database subnet |
| AZ-B | Public Subnet 2 | `10.0.2.0/24` | ALB and NAT Gateway 2 |
| AZ-B | Private App Subnet 2 | `10.0.12.0/24` | EC2 application server 2 |
| AZ-B | Private DB Subnet 2 | `10.0.22.0/24` | RDS database subnet |

The AZ-A and AZ-B labels represent the two selected Availability Zones. Confirm the actual Availability Zone names available in the AWS account before deployment.

### 6.2 Network Traffic Flow

| Source | Destination | Purpose |
|---|---|---|
| Internet | Internet Gateway | Internet connectivity to the VPC |
| CloudFront | Application Load Balancer | Dynamic application requests |
| CloudFront | Amazon S3 | Static content delivery |
| Application Load Balancer | EC2 Instances | Application traffic |
| EC2 Instances | Amazon RDS | Database communication |
| Private EC2 Subnets | NAT Gateways | Outbound Internet access |
| CloudWatch | AWS Resources | Monitoring and log collection |

CloudWatch monitoring is a logical monitoring relationship, not ordinary application traffic.

### 6.3 Routing Configuration

**Public Subnet Route Tables:**

- Local VPC traffic uses the local route.
- Internet-bound traffic (`0.0.0.0/0`) routes through the Internet Gateway.

**Private Application Subnet Route Tables:**

- Local VPC traffic uses the local route.
- Internet-bound traffic (`0.0.0.0/0`) routes through the NAT Gateway in the same Availability Zone.

**Private Database Subnet Route Tables:**

- Local VPC traffic uses the local route.
- No direct default Internet route is configured.

EC2 instances communicate with RDS through private network connectivity within the VPC.

## 7. Security Architecture

Security is implemented through multiple layers to protect the application, network, and database.

| Security Component | Purpose |
|---|---|
| AWS WAF | Filters malicious web requests |
| AWS Shield Standard | Provides basic DDoS protection |
| Security Groups | Controls network traffic |
| IAM Roles | Controls AWS permissions |
| Private Subnets | Protects internal resources |
| S3 OAC | Secures S3 content access |
| Encryption | Protects data at rest and in transit |
| HTTPS | Secures communication between clients and the application |

### Additional Security Recommendations

- Enable encryption at rest and in transit.
- Do not expose RDS publicly.
- Avoid opening SSH access to everyone.
- Use least-privilege IAM policies.
- Prefer Systems Manager Session Manager for EC2 administration.
- Restrict ALB origin access when CloudFront is the intended public entry point.
- Store database credentials securely.
- Enable appropriate logging and monitoring.
- Regularly review Security Group rules and IAM permissions.

## 8. High Availability and Scalability

The architecture uses multiple AWS services to improve availability and support changing application demand.

| AWS Component | High Availability / Scalability Approach |
|---|---|
| VPC | Resources distributed across two Availability Zones |
| NAT Gateways | One in each Availability Zone |
| Application Load Balancer | Distributes traffic across healthy targets |
| EC2 Auto Scaling | Adjusts application capacity |
| RDS Multi-AZ | Provides standby database and automatic failover |
| CloudFront | Uses global edge locations for content delivery |
| S3 | Provides durable object storage |

These components help reduce single points of failure and support changing application demand.

## 9. Monitoring and Logging

Amazon CloudWatch monitors infrastructure and application performance.

### Important Monitoring Metrics

- EC2 CPU utilization.
- EC2 status checks.
- ALB request count.
- ALB response time.
- Unhealthy target count.
- RDS CPU utilization.
- Database connections.
- Database storage.
- Application logs.

### CloudWatch Alarms

CloudWatch alarms can be configured to notify administrators when monitoring thresholds are exceeded.

Examples include:

- High EC2 CPU utilization.
- Unhealthy ALB targets.
- High RDS CPU utilization.
- Low available database storage.
- Application errors.

Amazon SNS can be integrated with CloudWatch Alarms to send notifications.

## 10. Monthly AWS Cost Estimation

The following table summarizes the available AWS Pricing Calculator estimates.

| AWS Resource | Configuration | Count | Estimated Monthly Cost (USD) |
|---|---|---:|---:|
| Amazon VPC | Custom VPC | 1 | $0.00 |
| Public and Private Subnets | Six subnets | 6 | $0.00 |
| Internet Gateway | Standard IGW | 1 | $0.00 |
| NAT Gateway | Standard NAT Gateway | 2 | To be calculated |
| Application Load Balancer | Internet-facing ALB | 1 | $19.45 |
| Amazon EC2 | `t2.micro` | 2 | $7.96* |
| Amazon RDS | PostgreSQL Multi-AZ | 1 | $146.65 |
| Amazon S3 | Standard Storage | 1 | $1.25 |
| Amazon CloudFront | CDN | 1 | $0.50 |
| AWS WAF | Web ACL | 1 | $0.00* |
| AWS Shield Standard | DDoS Protection | 1 | $0.00 |
| Amazon Route 53 | DNS | 1 | $0.00* |
| Amazon CloudWatch | Monitoring | 1 | $0.00* |
| **Total of Available Estimates** | | | **$175.81** |

### Cost Notes

- The $175.81 figure is the initial subtotal from the available calculator values, not the final architecture cost.
- Both NAT Gateways must be included in the final calculation.
- NAT Gateway hourly and data-processing charges may apply.
- EC2 pricing must be verified for two `t2.micro` instances and the intended running hours.
- RDS pricing depends on the PostgreSQL instance class, Multi-AZ deployment, storage, and backup configuration.
- WAF, Route 53, and CloudWatch can incur additional usage-based charges even if the initial estimate shows $0.
- Data transfer and public IPv4 charges may also apply.
- Confirm that the AWS Pricing Calculator region is `ap-south-1` before finalizing the estimate.
- Verify that the RDS instance class used in the calculator matches the intended configuration.

### Cost Optimization Strategies

- Use appropriate EC2 instance sizes.
- Configure Auto Scaling policies.
- Monitor NAT Gateway data processing.
- Enable CloudFront caching.
- Review S3 storage usage.
- Monitor unused AWS resources.
- Review CloudWatch log retention.
- Select appropriate RDS storage and backup settings.

## 11. Design Decisions and Trade-offs

| Design Decision | Reason | Trade-off |
|---|---|---|
| Two Availability Zones | Improves availability | Additional infrastructure cost |
| Two NAT Gateways | AZ-level outbound redundancy | Higher NAT Gateway cost |
| Application Load Balancer | Distributes traffic | Hourly and usage charges |
| EC2 Auto Scaling | Adjusts capacity automatically | Requires scaling policies |
| RDS Multi-AZ | Improves database availability | Higher database cost |
| S3 and CloudFront | Faster content delivery | Storage and transfer charges |
| Private Subnets | Protects internal resources | Requires outbound networking |
| AWS WAF | Filters malicious requests | Additional configuration and possible charges |
| IAM Roles | Secure AWS access | Permission management |
| CloudWatch | Infrastructure monitoring | Monitoring and log usage charges may apply |

## 12. Project Deliverables

The project includes the following deliverables:

1. **AWS Architecture Diagram (PDF)** – Visual representation of the three-tier AWS architecture.
2. **Editable Architecture Diagram (.drawio)** – Editable source architecture diagram.
3. **Technical Design Document (README.md)** – Explanation of AWS services, networking, security, scalability, and design decisions.
4. **AWS Pricing Calculator Report (PDF)** – Estimated monthly infrastructure costs.

## 13. Conclusion

The proposed AWS Three-Tier E-Commerce Application Architecture provides a foundation for hosting a secure, scalable, and highly available web application.

The design separates presentation, application, and data workloads into independent tiers.

AWS services such as Application Load Balancer, EC2 Auto Scaling, Amazon RDS PostgreSQL Multi-AZ, S3, CloudFront, WAF, Shield, IAM, and CloudWatch work together to provide performance, security, and reliability.

The architecture uses two Availability Zones, six subnets, two NAT Gateways, and two initial EC2 instances to improve network availability and resource isolation.

The design also considers cost optimization through managed services, scalable computing resources, and CDN-based content delivery.

Before production deployment, the architecture should be validated through:

- Security reviews.
- Application load testing.
- Backup and recovery testing.
- Database failover testing.
- Network connectivity testing.
- Monitoring and alarm validation.
- Final cost estimation based on actual workload requirements.

---

**Project:** AWS Three-Tier E-Commerce Application Architecture  
**Cloud Provider:** Amazon Web Services (AWS)  
**Region:** Asia Pacific (Mumbai) – `ap-south-1`  
**Architecture:** Three-Tier Architecture
