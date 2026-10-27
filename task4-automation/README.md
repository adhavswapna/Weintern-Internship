# Task 4: Automate with Shell and Python Scripts

## Project Description

This project demonstrates cloud automation using Python, Bash, and the AWS CLI. The scripts identify running Amazon EC2 instances with a specified Name tag and estimate their monthly compute costs using example hourly rates.

## Tools and Technologies

- Amazon Web Services (AWS)
- Amazon EC2
- AWS Command Line Interface (AWS CLI)
- Python 3
- Bash Shell
- Linux Terminal

## AWS Configuration

| Configuration | Value |
|---|---|
| AWS Region | Sydney (`ap-southeast-2`) |
| Tag Key | `Name` |
| Tag Value | `weintern-dev-ec2` |
| Monthly Hours | 730 hours |
| Currency | USD |

## Project Files

### 1. `ec2_cost_estimator.py`

The Python script uses the AWS CLI to retrieve running EC2 instances in the configured Region.

Features:
- Retrieves running EC2 instances.
- Filters instances using the `Name=weintern-dev-ec2` tag.
- Displays the EC2 instance ID and instance type.
- Estimates monthly compute costs for supported instance types.
- Calculates the total estimated monthly cost.
- Handles AWS CLI errors and invalid JSON responses.

### 2. `ec2_cost_estimator.sh`

The Bash script performs similar operations using AWS CLI commands and `awk`.

Features:
- Retrieves running EC2 instances matching the configured Name tag.
- Displays instance IDs and instance types.
- Estimates monthly compute costs using example hourly rates.
- Calculates the total estimated monthly cost.
- Displays a message when no matching instances are found.

## Prerequisites

Before running the scripts, ensure that:

1. AWS CLI is installed.
2. AWS credentials are configured.
3. The configured AWS identity has permission to describe EC2 instances.
4. Python 3 is installed for the Python script.
5. Bash and `awk` are available for the Shell script.

## Example Hourly Rates

The scripts use the following illustrative hourly rates:

| Instance Type | Example Hourly Rate (USD) |
|---|---:|
| `t2.micro` | $0.0116 |
| `t3.micro` | $0.0104 |
| `t3.small` | $0.0208 |

**Note:** These rates are examples, not verified current AWS prices. Actual prices depend on the instance configuration, Region, operating system, pricing model, and other factors.

## Cost Calculation

The scripts estimate monthly compute costs using:

**Estimated Monthly Cost = Example Hourly Rate × 730 Hours**

For example, using the illustrative rate for a `t3.micro` instance:

`$0.0104 × 730 = $7.592 USD per month`

The result is approximately **$7.59 USD per month**.

This is an estimate, not an actual AWS bill.

The estimate excludes EBS storage, data transfer, taxes, and other applicable AWS charges. It also assumes the instance runs for the entire 730-hour month.

## How to Run

Navigate to the project directory:

```bash
cd ~/weintern-cloud-internship/task4-automation
```

### Run the Python Script

```bash
python3 ec2_cost_estimator.py
```

### Run the Shell Script

Make the script executable:

```bash
chmod +x ec2_cost_estimator.sh
```

Execute it:

```bash
./ec2_cost_estimator.sh
```

## Verification

To verify that AWS CLI can retrieve running EC2 instances in the configured Region, run:

```bash
aws ec2 describe-instances \
  --region ap-southeast-2 \
  --filters "Name=instance-state-name,Values=running" \
  --query 'Reservations[].Instances[].[InstanceId,InstanceType]' \
  --output table
```

To check for instances matching the project's Name tag, run:

```bash
aws ec2 describe-instances \
  --region ap-southeast-2 \
  --filters \
    "Name=instance-state-name,Values=running" \
    "Name=tag:Name,Values=weintern-dev-ec2" \
  --query 'Reservations[].Instances[].[InstanceId,InstanceType]' \
  --output table
```

## Test Results

The scripts report the matching running EC2 instances and their estimated monthly costs.

If no running instances match the configured Name tag, the scripts display a message indicating that no matching instances were found and report a total estimated monthly cost of $0.00 USD.

Record the actual output from your latest test when documenting the final results.

## Safety

These scripts use read-only EC2 describe operations. They do not create, stop, start, terminate, or modify EC2 instances.

The cost calculations are illustrative estimates and should not be treated as official AWS pricing.

## Conclusion

Task 4 demonstrates basic cloud automation using AWS CLI, Python, and Bash. Both scripts filter running EC2 instances by a specified tag and calculate illustrative monthly compute costs for supported instance types.
