
import subprocess
import json

REGION = "ap-southeast-2"
TAG_VALUE = "weintern-dev-ec2-secure"

# Example hourly prices
PRICES = {
    "t2.micro": 0.0116,
    "t3.micro": 0.0104,
    "t3.small": 0.0208
}

HOURS = 730

print("EC2 Cost Estimator")
print("------------------")

# Get running EC2 instances using AWS CLI
result = subprocess.run(
    ["aws", "ec2", "describe-instances",
     "--region", REGION,
     "--filters", "Name=instance-state-name,Values=running",
     "--output", "json"],
    capture_output=True, text=True, check=True
)

data = json.loads(result.stdout)

total = 0
count = 0

for reservation in data["Reservations"]:
    for instance in reservation["Instances"]:

        # Check instance tag
        tags = {tag["Key"]: tag["Value"] for tag in instance.get("Tags", [])}

        if tags.get("Name") == TAG_VALUE:

            count += 1
            instance_id = instance["InstanceId"]
            instance_type = instance["InstanceType"]

            print("\nInstance ID:", instance_id)
            print("Instance Type:", instance_type)

            price = PRICES.get(instance_type)

            if price:
                cost = price * HOURS
                total += cost

                print("Hourly Cost: $", price)
                print("Monthly Cost: $", round(cost, 2))
            else:
                print("Price not available.")

if count == 0:
    print("No matching running instances found.")

print("------------------")
print("Total Monthly Cost: $", round(total, 2))
print("Note: Prices are examples, not live AWS rates.")


