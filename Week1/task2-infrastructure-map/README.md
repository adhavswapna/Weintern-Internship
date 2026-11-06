# Task 2: AWS Infrastructure Map

## 1. Project Overview

This project documents the existing AWS development infrastructure in the Sydney region using read-only AWS CLI commands.

The objective is to inspect AWS networking resources, identify the running EC2 instance, understand the network configuration, and represent the verified infrastructure in an architecture diagram.

The infrastructure map includes the VPC, subnets, Internet Gateway, route table, Network ACL, security group, and EC2 instance.

## 2. AWS Environment

| Property | Details |
|---|---|
| AWS Region | `ap-southeast-2` (Asia Pacific – Sydney) |
| AWS Account ID | `230623977579` |
| VPC ID | `vpc-0930c560add4e6a1f` |
| VPC CIDR | `172.31.0.0/16` |
| VPC Type | Default VPC |
| EC2 Instance Name | `weintern-dev-ec2-secure` |
| EC2 Instance ID | `i-07b31d3e659a962ac` |
| Instance Type | `t3.micro` |
| Instance State | `running` |
| Availability Zone | `ap-southeast-2b` |
| Private IP | `172.31.39.91` |
| Public IP | `54.206.174.161` |

## 3. Infrastructure Components

### 3.1 Virtual Private Cloud (VPC)

The inspection identified the default VPC in the Sydney region.

- **VPC ID:** `vpc-0930c560add4e6a1f`
- **IPv4 CIDR:** `172.31.0.0/16`
- **State:** `available`
- **Default VPC:** Yes

The VPC provides the logical network boundary for the AWS resources.

### 3.2 Subnets

Three default subnets were identified across three Availability Zones.

| Availability Zone | Subnet ID | CIDR Block | Public IP Auto-Assignment |
|---|---|---|---|
| `ap-southeast-2a` | `subnet-07fc743e3cc16e0d6` | `172.31.0.0/20` | Enabled |
| `ap-southeast-2b` | `subnet-09e585f30ee84d9bd` | `172.31.32.0/20` | Enabled |
| `ap-southeast-2c` | `subnet-0386163dc82fbb059` | `172.31.16.0/20` | Enabled |

All three subnets belong to the same VPC.

The subnets have public IPv4 address auto-assignment enabled. Their default route table also has an active route to the Internet Gateway.

### 3.3 EC2 Instance

The following running EC2 instance was identified.

| Property | Value |
|---|---|
| Name | `weintern-dev-ec2-secure` |
| Instance ID | `i-07b31d3e659a962ac` |
| Instance Type | `t3.micro` |
| State | `running` |
| Availability Zone | `ap-southeast-2b` |
| VPC ID | `vpc-0930c560add4e6a1f` |
| Subnet ID | `subnet-09e585f30ee84d9bd` |
| Private IPv4 | `172.31.39.91` |
| Public IPv4 | `54.206.174.161` |
| Security Group | `sg-0af88d09a81ead51a` |

The EC2 instance is deployed in the default subnet in Availability Zone `ap-southeast-2b`.

The instance runs Amazon Linux 2023. Docker was installed and successfully tested using the `hello-world` container.

### 3.4 Route Table

The following main route table was identified:

- **Route Table ID:** `rtb-01d029975330e51e8`
- **VPC ID:** `vpc-0930c560add4e6a1f`
- **Main Route Table:** Yes
- **Association State:** `associated`

The inspected routes are:

| Destination | Target | State |
|---|---|---|
| `172.31.0.0/16` | `local` | Active |
| `0.0.0.0/0` | `igw-0b24f15958bcc200b` | Active |

The local route supports communication within the VPC, subject to applicable network controls.

The default route directs IPv4 traffic destined for addresses outside the VPC toward the Internet Gateway.

The inspected route table is the VPC's main route table. Subnets without an explicit route table association use the main route table.

### 3.5 Internet Gateway

The following Internet Gateway was identified:

- **Internet Gateway ID:** `igw-0b24f15958bcc200b`
- **Associated VPC:** `vpc-0930c560add4e6a1f`
- **Attachment State:** `available`

The Internet Gateway is attached to the default VPC.

The main route table contains an active default IPv4 route (`0.0.0.0/0`) pointing to this Internet Gateway.

This configuration provides an internet-routing path for eligible resources. Actual connectivity also depends on subnet configuration, security groups, Network ACL rules, and other network controls.

### 3.6 Network ACL

The inspection identified one default Network ACL.

| Property | Value |
|---|---|
| Network ACL ID | `acl-0553986d8a57b9609` |
| VPC ID | `vpc-0930c560add4e6a1f` |
| Default Network ACL | Yes |

The Network ACL is associated with all three default subnets.

| Subnet | Subnet ID |
|---|---|
| `ap-southeast-2a` | `subnet-07fc743e3cc16e0d6` |
| `ap-southeast-2b` | `subnet-09e585f30ee84d9bd` |
| `ap-southeast-2c` | `subnet-0386163dc82fbb059` |

The inspected Network ACL rules are:

| Direction | Rule Number | Destination/Source | Action |
|---|---|---|---|
| Inbound | 100 | `0.0.0.0/0` | Allow |
| Inbound | 32767 | `0.0.0.0/0` | Deny |
| Outbound | 100 | `0.0.0.0/0` | Allow |
| Outbound | 32767 | `0.0.0.0/0` | Deny |

The default Network ACL allows inbound and outbound IPv4 traffic through rule 100. The final deny rules apply to traffic not matched by earlier rules.

### 3.7 Security Group

The EC2 instance uses the custom security group `weintern-dev-sg`.

- **Security Group ID:** `sg-0af88d09a81ead51a`
- **Name:** `weintern-dev-sg`
- **VPC ID:** `vpc-0930c560add4e6a1f`

The inspected security group configuration includes:

**Inbound**
- SSH access using TCP port `22`.
- Source restricted to a specific IPv4 address range (`/32`).

**Outbound**
- All IPv4 traffic is allowed.

The security group acts as a virtual firewall controlling traffic to and from the EC2 instance.

### 3.8 NAT Gateway

The AWS CLI inspection returned an empty result for NAT Gateways in the Sydney region.

Therefore, no NAT Gateway was identified in the inspected region.

## 4. Architecture Diagram

The following logical architecture represents the inspected AWS resources.

```text
Internet
   |
   |
Internet Gateway
igw-0b24f15958bcc200b
   |
   |
Main Route Table
rtb-01d029975330e51e8
   |
   | 0.0.0.0/0 -> Internet Gateway
   |
Default VPC: 172.31.0.0/16
vpc-0930c560add4e6a1f
   |
   |--------------------|--------------------|
   |                    |                    |
   |                    |                    |
Subnet 2a               Subnet 2b             Subnet 2c
172.31.0.0/20           172.31.32.0/20        172.31.16.0/20
   |                    |                    |
                        |
                 EC2 Instance
             weintern-dev-ec2-secure
                   t3.micro
               172.31.39.91
                        |
                 Security Group
                 weintern-dev-sg

Network ACL:
acl-0553986d8a57b9609
Associated with all three subnets.

NAT Gateway:
Not configured.
```

The editable architecture diagram is maintained separately in the Draw.io file.

## 5. AWS CLI Commands Used

The following AWS CLI commands were used to inspect the infrastructure.

### Describe VPCs

```bash
aws ec2 describe-vpcs \
  --region ap-southeast-2 \
  --output table \
  --no-cli-pager
```

### Describe Subnets

```bash
aws ec2 describe-subnets \
  --region ap-southeast-2 \
  --output table \
  --no-cli-pager
```

### Describe EC2 Instances

```bash
aws ec2 describe-instances \
  --region ap-southeast-2 \
  --output table \
  --no-cli-pager
```

### Describe Route Tables

```bash
aws ec2 describe-route-tables \
  --region ap-southeast-2 \
  --output table \
  --no-cli-pager
```

### Describe Internet Gateways

```bash
aws ec2 describe-internet-gateways \
  --region ap-southeast-2 \
  --output table \
  --no-cli-pager
```

### Describe Network ACLs

```bash
aws ec2 describe-network-acls \
  --region ap-southeast-2 \
  --output table \
  --no-cli-pager
```

### Describe Security Groups

```bash
aws ec2 describe-security-groups \
  --region ap-southeast-2 \
  --output table \
  --no-cli-pager
```

### Describe NAT Gateways

```bash
aws ec2 describe-nat-gateways \
  --region ap-southeast-2 \
  --output table \
  --no-cli-pager
```

## 6. Project Deliverables

| File | Description |
|---|---|
| `README.md` | Project overview, infrastructure details, and AWS CLI commands |
| `task2-architecture-notes.md` | Detailed architecture findings and inspection results |
| `task2-infrastructure-map.drawio` | Editable AWS infrastructure architecture diagram |

Ensure that all required files exist in the project directory before submission.

## 7. Limitations

1. The inspection covers the Sydney region (`ap-southeast-2`) only.
2. Resource visibility depends on the permissions granted to the IAM identity.
3. RDS and Lambda resources were not verified during the earlier inspection because the relevant requests returned `AccessDenied`.
4. The EC2 information in this README reflects the latest identified working instance, not the older instance details in the previous version.
5. Public IP assignment and an Internet Gateway route do not independently guarantee end-to-end internet connectivity.
6. The inspection did not establish application-level connectivity.
7. No NAT Gateway was identified in the inspected region.
8. The AWS CLI inspection commands used for documenting these resources are read-only and did not modify the inspected infrastructure.

## 8. Conclusion

This project documents the existing AWS development infrastructure in the Sydney region.

The inspection confirmed the default VPC, three default subnets, main route table, Internet Gateway, default Network ACL, custom EC2 security group, and running EC2 instance.

The inspection also confirmed that no NAT Gateway was identified in the region.

The README and supporting architecture diagram provide a visual and written record of the AWS environment. This documentation helps explain how the networking components are organised and how the EC2 instance is connected to the VPC.

The project demonstrates practical understanding of AWS networking resources and infrastructure inspection using AWS CLI.
