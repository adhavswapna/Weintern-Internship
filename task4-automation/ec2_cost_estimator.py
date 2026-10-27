
import subprocess
import json
import sys

# AWS configuration
REGION = "ap-southeast-2"
TAG_KEY = "Name"
TAG_VALUE = "weintern-dev-ec2"

# Example hourly prices in USD (not verified live AWS rates)
PRICES = {
    "t2.micro": 0.0116,
    "t3.micro": 0.0104,
    "t3.small": 0.0208
}

HOURS_PER_MONTH = 730


def get_instances():
    """Retrieve running EC2 instances from AWS."""
    result = subprocess.run(
        [
            "aws",
            "ec2",
            "describe-instances",
            "--region",
            REGION,
            "--filters",
            "Name=instance-state-name,Values=running",
            "--output",
            "json"
        ],
        capture_output=True,
        text=True,
        check=True
    )

    data = json.loads(result.stdout)
    instances = []

    for reservation in data.get("Reservations", []):
        instances.extend(reservation.get("Instances", []))

    return instances


def main():
    print("EC2 Cost Estimator")
    print("------------------")
    print(f"AWS Region: {REGION}")
    print(f"Instance Filter: {TAG_KEY}={TAG_VALUE}")
    print()

    instances = get_instances()
    total = 0.0
    matched_instances = 0

    for instance in instances:
        tags = {
            tag["Key"]: tag["Value"]
            for tag in instance.get("Tags", [])
        }

        # Process only instances matching the configured Name tag
        if tags.get(TAG_KEY) != TAG_VALUE:
            continue

        matched_instances += 1

        instance_id = instance["InstanceId"]
        instance_type = instance["InstanceType"]

        print(f"Instance ID: {instance_id}")
        print(f"Instance Type: {instance_type}")

        hourly_price = PRICES.get(instance_type)

        if hourly_price is None:
            print("Price not configured for this instance type.")
        else:
            monthly_cost = hourly_price * HOURS_PER_MONTH
            total += monthly_cost

            print(f"Example Hourly Cost: ${hourly_price:.4f} USD")
            print(f"Estimated Monthly Cost: ${monthly_cost:.2f} USD")

        print("------------------")

    if matched_instances == 0:
        print("No matching running EC2 instances found.")

    print(f"Total Estimated Monthly Cost: ${total:.2f} USD")
    print(f"Monthly estimate assumes {HOURS_PER_MONTH} hours.")
    print("Note: Example prices only; actual AWS rates may differ.")
    print("Estimate excludes EBS storage, data transfer, taxes,")
    print("and other AWS charges.")


if __name__ == "__main__":
    try:
        main()

    except subprocess.CalledProcessError as error:
        print("AWS CLI command failed.")

        if error.stderr:
            print(error.stderr.strip())

        print("Check AWS credentials, permissions, and account.")
        sys.exit(1)

    except FileNotFoundError:
        print("AWS CLI was not found. Please install AWS CLI.")
        sys.exit(1)

    except json.JSONDecodeError:
        print("Could not parse the AWS CLI response.")
        sys.exit(1)

