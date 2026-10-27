
#!/bin/bash

# EC2 Cost Estimator
# Estimates monthly compute costs for running EC2 instances
# with the specified Name tag.

REGION="ap-southeast-2"
TAG_KEY="Name"
TAG_VALUE="weintern-dev-ec2"

echo "EC2 Cost Estimator"
echo "------------------"

INSTANCES=$(aws ec2 describe-instances \
    --region "$REGION" \
    --filters "Name=instance-state-name,Values=running" \
              "Name=tag:$TAG_KEY,Values=$TAG_VALUE" \
    --query 'Reservations[].Instances[].[InstanceId,InstanceType]' \
    --output text) || exit 1

TOTAL=0

if [ -z "$INSTANCES" ] || [ "$INSTANCES" = "None" ]; then
    echo "No matching running EC2 instances found."
else
    while read -r ID TYPE; do
        case "$TYPE" in
            t2.micro) RATE=0.0116 ;;
            t3.micro) RATE=0.0104 ;;
            t3.small) RATE=0.0208 ;;
            *)
                echo "Price not configured for $TYPE"
                continue
                ;;
        esac

        MONTHLY=$(awk -v rate="$RATE" \
            'BEGIN {printf "%.2f", rate * 730}')

        echo "Instance ID: $ID"
        echo "Instance Type: $TYPE"
        echo "Estimated Monthly Cost: \$$MONTHLY USD"

        TOTAL=$(awk -v total="$TOTAL" -v cost="$MONTHLY" \
            'BEGIN {printf "%.2f", total + cost}')

        echo "------------------"
    done <<< "$INSTANCES"
fi

echo "Total Estimated Monthly Cost: \$$TOTAL USD"
echo "Monthly estimate assumes 730 hours."
echo "Note: Rates are examples, not verified AWS prices."

