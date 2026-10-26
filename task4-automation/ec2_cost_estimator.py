import subprocess
import json

REGION = "ap-southeast-2"
TAG_KEY = "Environment"
TAG_VALUE = "Learning"

# Example hourly prices in USD
PRICES = {
    "t2.micro": 0.0116,
    "t3.micro": 0.0104,
    "t3.small": 0.0208
}

def get_instances():
    result = subprocess.run([
        "aws", "ec2", "describe-instances",
        "--region", REGION,
        "--filters", "Name=instance-state-name,Values=running",
        "--output", "json"
    ], capture_output=True, text=True, check=True)

    data = json.loads(result.stdout)
    instances = []

    for reservation in data["Reservations"]:
        instances.extend(reservation["Instances"])

    return instances

def main():
    print("EC2 Cost Estimator")
    print("------------------")

    instances = get_instances()
    total = 0

    for instance in instances:
        tags = {
            tag["Key"]: tag["Value"]
            for tag in instance.get("Tags", [])
        }

        if tags.get(TAG_KEY) != TAG_VALUE:
            continue

        instance_type = instance["InstanceType"]
        price = PRICES.get(instance_type)

        print("Instance ID:", instance["InstanceId"])
        print("Instance Type:", instance_type)

        if price is None:
            print("Price not configured")
        else:
            monthly = price * 730
            total += monthly
            print("Estimated Monthly Cost: $", round(monthly, 2))

        print("------------------")

    print("Total Estimated Monthly Cost: $", round(total, 2))
    print("Note: Prices are examples, not verified AWS rates.")

if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError:
        print("AWS CLI failed. Check your AWS credentials and permissions.")
    except FileNotFoundError:
        print("AWS CLI was not found. Please install it.")

