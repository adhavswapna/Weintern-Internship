# Task 4: Automate with a Shell / Python Script

## Description
This project contains Python and Shell scripts to list running AWS EC2 instances with a specific tag and estimate their monthly cost.

## Tools Used
- AWS CLI
- Python 3
- Bash Shell

## AWS Configuration
- **Region:** Sydney (`ap-southeast-2`)
- **Tag Key:** `Environment`
- **Tag Value:** `Learning`

## Files
- `ec2_cost_estimator.py` – Lists matching running EC2 instances and estimates monthly costs using Python and AWS CLI.
- `ec2_cost_estimator.sh` – Lists matching running EC2 instances and estimates monthly costs using a Bash script.

## Prerequisites
1. AWS CLI must be installed and configured.
2. AWS credentials must have permission to describe EC2 instances.
3. Python 3 is required to run the Python script.
4. Bash is required to run the Shell script.
5. `awk` is used by the Shell script to calculate costs.

## How to Run

### Run the Python Script
```bash
python3 ec2_cost_estimator.py
```

### Run the Shell Script
```bash
chmod +x ec2_cost_estimator.sh
./ec2_cost_estimator.sh
```

## Cost Estimation
The scripts use example hourly rates for selected EC2 instance types:

| Instance Type | Example Hourly Rate (USD) |
|---|---:|
| t2.micro | $0.0116 |
| t3.micro | $0.0104 |
| t3.small | $0.0208 |

The estimated monthly cost is calculated using:

**Monthly Cost = Hourly Rate × 730 hours**

These rates are illustrative examples and are not verified current AWS prices. Actual costs may vary depending on the instance type, AWS pricing, Region, and other charges.

## Current Test Result
No running EC2 instances matching the `Environment=Learning` tag were found in the Sydney Region during testing.

Therefore, the script displayed a total estimated monthly cost of **$0 USD**.

## Safety
These scripts only retrieve EC2 instance information. They do not create, stop, or modify AWS resources.

## Conclusion
This task demonstrates basic cloud automation using AWS CLI, Python, and Bash. The scripts filter running EC2 instances by tag and provide an estimated monthly cost summary.
