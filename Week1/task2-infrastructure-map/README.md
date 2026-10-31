# Task 2: AWS Infrastructure Map

## Project Overview

This project documents the existing AWS development infrastructure in the Sydney region using read-only AWS CLI commands.

The objective is to inspect AWS networking resources, identify the running EC2 instance, understand the network configuration, and represent the verified infrastructure in an architecture diagram.

## AWS Environment

| Property | Details |
|---|---|
| AWS Region | `ap-southeast-2` (Asia Pacific — Sydney) |
| AWS Account ID | `230623977579` |
| VPC ID | `vpc-0930c560add4e6a1f` |
| VPC CIDR | `172.31.0.0/16` |
| EC2 Instance Name | `weintern-dev-ec2` |
| EC2 Instance ID | `i-02a5a692d3c3c47de` |
| Instance Type | `t3.micro` |
| Instance State | `running` |

## Infrastructure Components

### 1. Virtual Private Cloud (VPC)

The inspection identified the default VPC in the Sydney region.

- **VPC ID:** `vpc-0930c560add4e6a1f`
- **IPv4 CIDR:** `172.31.0.0/16`
- **State:** `available`
- **Default VPC:** Yes

### 2. Subnets

Three subnets were identified across three Availability Zones.

| Availability Zone | Subnet ID | CIDR Block |
|---|---|---|
| `ap-southeast-2a` | `subnet-07fc743e3cc16e0d6` | `172.31.0.0/20` |
| `ap-southeast-2b` | `subnet-09e585f30ee84d9bd` | `172.31.32.0/20` |
| `ap-southeast-2c` | `subnet-0386163dc82fbb059` | `172.31.16.0/20` |

All three subnets belong to the same VPC.

The subnets have public IPv4 auto-assignment enabled. This setting alone does not guarantee public connectivity.

### 3. EC2 Instance

The following running EC2 instance was identified.

| Property | Value |
|---|---|
| Name | `weintern-dev-ec2` |
| Instance ID | `i-02a5a692d3c3c47de` |
| Instance Type | `t3.micro` |
| State | `running` |
| Availability Zone | `ap-southeast-2a` |
| VPC ID | `vpc-0930c560add4e6a1f` |
| Subnet ID | `subnet-07fc743e3cc16e0d6` |
| Private IPv4 | `172.31.12.224` |
| Public IPv4 | `54.206.47.86` |
| Security Group | `sg-087fd55a3a67725a8` |

The instance's private IP address belongs to the CIDR range of its subnet.

### 4. Route Table

The main route table identified during inspection is:

- **Route Table ID:** `rtb-01d029975330e51e8`
- **VPC ID:** `vpc-0930c560add4e6a1f`

The inspected routes are:

| Destination | Target | State |
|---|---|---|
| `172.31.0.0/16` | `local` | Active |
| `0.0.0.0/0` | `igw-0b24f15958bcc200b` | Active |

The local route supports communication within the VPC, subject to applicable network controls.

The default route directs IPv4 traffic destined for addresses outside the VPC toward the Internet Gateway.

The inspected route table has no explicit subnet associations. Subnets without explicit associations use the VPC's main route table.

### 5. Internet Gateway

The route table references the following Internet Gateway:

- **Internet Gateway ID:** `igw-0b24f15958bcc200b`
- **Associated VPC:** `vpc-0930c560add4e6a1f`

The Internet Gateway is the target of the active default IPv4 route in the inspected main route table.

The presence of an Internet Gateway route does not independently establish end-to-end internet connectivity.

### 6. Security Group

The EC2 instance uses the default security group.

- **Security Group ID:** `sg-087fd55a3a67725a8`
- **Name:** `default`
- **VPC ID:** `vpc-0930c560add4e6a1f`

The inspected security group rules are:

**Inbound**
- All protocols from resources associated with the same security group.
- No IPv4 CIDR-based inbound rules were returned.
- No IPv6 CIDR-based inbound rules were returned.

**Outbound**
- All protocols to IPv4 destination `0.0.0.0/0`.
- No IPv6 CIDR-based outbound rules were returned.

The inspected inbound rule does not allow unrestricted inbound connections from the public internet.

### 7. NAT Gateway

No NAT Gateway entries were established by the results documented for this task.

This finding is limited to the inspected region and the commands performed.

## Architecture Diagram

The logical architecture identified during inspection is:

```text
AWS Region: ap-southeast-2 (Sydney)
|
└── Default VPC: 172.31.0.0/16
    |
    ├── Subnet: ap-southeast-2a
    |   └── EC2: weintern-dev-ec2
    |       ├── Type: t3.micro
    |       ├── State: running
    |       ├── Private IP: 172.31.12.224
    |       ├── Public IP: 54.206.47.86
    |       └── Security Group: sg-087fd55a3a67725a8
    |
    ├── Subnet: ap-southeast-2b
    |
    ├── Subnet: ap-southeast-2c
    |
    └── Main Route Table
        ├── 172.31.0.0/16 → local
        └── 0.0.0.0/0 → Internet Gateway
```

This text diagram summarizes the verified configuration. The editable diagram is maintained separately in the Draw.io file.

## AWS CLI Commands Used

The following commands can be used to inspect the infrastructure.

### Describe VPCs

```bash
aws ec2 describe-vpcs \
  --region ap-southeast-2 \
  --output table
```

### Describe Subnets

```bash
aws ec2 describe-subnets \
  --region ap-southeast-2 \
  --query 'Subnets[].{SubnetId:SubnetId,VPC:VpcId,AZ:AvailabilityZone,CIDR:CidrBlock,State:State,PublicIP:MapPublicIpOnLaunch}' \
  --output table
```

### Describe EC2 Instances

```bash
aws ec2 describe-instances \
  --region ap-southeast-2 \
  --query 'Reservations[].Instances[].{InstanceId:InstanceId,Name:Tags[?Key==`Name`]|[0].Value,State:State.Name,InstanceType:InstanceType,VPC:VpcId,SubnetId:SubnetId,PrivateIP:PrivateIpAddress,PublicIP:PublicIpAddress,SecurityGroups:SecurityGroups[].GroupId}' \
  --output table
```

### Describe Route Tables

```bash
aws ec2 describe-route-tables \
  --region ap-southeast-2 \
  --query 'RouteTables[].{RouteTableId:RouteTableId,VPC:VpcId,Main:Associations[?Main==`true`].Main,AssociatedSubnets:Associations[].SubnetId,Routes:Routes[].{Destination:DestinationCidrBlock,Target:GatewayId,State:State}}' \
  --output json
```

### Describe Security Groups

```bash
aws ec2 describe-security-groups \
  --region ap-southeast-2 \
  --group-ids sg-087fd55a3a67725a8 \
  --query 'SecurityGroups[].{Name:GroupName,ID:GroupId,VPC:VpcId,Inbound:IpPermissions,Outbound:IpPermissionsEgress}' \
  --output json
```

### Describe Internet Gateways

```bash
aws ec2 describe-internet-gateways \
  --region ap-southeast-2 \
  --output table
```

### Describe NAT Gateways

```bash
aws ec2 describe-nat-gateways \
  --region ap-southeast-2 \
  --filter Name=state,Values=available,pending \
  --output table
```

## Project Deliverables

| File | Description |
|---|---|
| `README.md` | Project overview, verified infrastructure details, and AWS CLI commands |
| `task2-architecture-notes.md` | Detailed architecture findings, limitations, and inspection results |
| `task2-infrastructure-map.drawio` | Editable infrastructure diagram for Draw.io |

Ensure that the files exist in the project directory before submission.

## Limitations

1. The inspection covers the Sydney region (`ap-southeast-2`) only.
2. Resource visibility depends on the permissions granted to the IAM identity.
3. RDS and Lambda could not be verified during the earlier inspection because the relevant requests returned `AccessDenied`.
4. The earlier EC2 query result was superseded by the latest successful inspection, which identified the running instance.
5. Public IP assignment and an Internet Gateway route do not guarantee public accessibility.
6. The inspection did not establish end-to-end connectivity.
7. No application-level dependencies were established.
8. No AWS resources were created, modified, or deleted during this task.

## Conclusion

This project documents the existing AWS development infrastructure in the Sydney region.

The inspection confirmed the default VPC, three subnets, main route table, Internet Gateway route, default security group, and running EC2 instance.

The README and supporting architecture notes provide a record of the inspected environment, while the Draw.io diagram provides a visual representation of the verified components.

The documentation distinguishes confirmed configuration from assumptions and limitations, supporting accurate infrastructure mapping and future investigation.
