# Task 5: Set Up Basic Alerts

## Objective

Configure and verify basic monitoring alerts in the AWS development sandbox using Amazon CloudWatch and Amazon SNS. Document the CPU threshold alarm, email notification configuration, and cost-alert permission limitations.

## Environment

- **Cloud Provider:** Amazon Web Services (AWS)
- **AWS Region:** Asia Pacific (Sydney) — `ap-southeast-2`
- **AWS Account ID:** `230623977579`
- **Monitoring Service:** Amazon CloudWatch
- **Notification Service:** Amazon Simple Notification Service (SNS)

## 1. CPU Utilization Alarm

An existing CloudWatch alarm named `EC2-High-CPU-Alarm` was inspected and verified.

### Alarm Configuration

| Setting | Value |
|---|---|
| Alarm Name | `EC2-High-CPU-Alarm` |
| Metric Namespace | `AWS/EC2` |
| Metric Name | `CPUUtilization` |
| EC2 Instance ID | `i-02a5a692d3c3c47de` |
| Comparison Operator | GreaterThanThreshold |
| CPU Threshold | 70% |
| Evaluation Period | 1 |
| Period | 300 seconds (5 minutes) |
| Actions Enabled | Yes |
| SNS Topic | `EC2-CPU-Alert-Topic` |
| Region | `ap-southeast-2` |

### Verification Command

```bash
aws cloudwatch describe-alarms \
  --region ap-southeast-2 \
  --alarm-names EC2-High-CPU-Alarm \
  --query 'MetricAlarms[].{Name:AlarmName,State:StateValue,Threshold:Threshold,Metric:MetricName,ActionsEnabled:ActionsEnabled}' \
  --output table
```

### Verification Result

The alarm configuration was successfully retrieved.

- Alarm name: `EC2-High-CPU-Alarm`
- Current state: `OK`
- CPU threshold: `70.0`
- Metric: `CPUUtilization`
- Actions enabled: `True`

The `OK` state indicates that the alarm is not currently detecting a threshold breach. An actual transition to the `ALARM` state has not yet been verified.

## 2. CPU Metric Verification

CPU utilization metrics were retrieved from Amazon CloudWatch for the monitored EC2 instance.

### Command

```bash
aws cloudwatch get-metric-statistics \
  --region ap-southeast-2 \
  --namespace AWS/EC2 \
  --metric-name CPUUtilization \
  --dimensions Name=InstanceId,Value=i-02a5a692d3c3c47de \
  --start-time "$(date -u -d '30 minutes ago' +%Y-%m-%dT%H:%M:%SZ)" \
  --end-time "$(date -u +%Y-%m-%dT%H:%M:%SZ)" \
  --period 300 \
  --statistics Average Maximum \
  --output table
```

Metric data was returned for the monitored instance. The observed CPU values were below the configured 70% threshold.

## 3. Email Notifications Using Amazon SNS

The CloudWatch alarm is configured to publish notifications to the following SNS topic:

`EC2-CPU-Alert-Topic`

**SNS Topic ARN:**

`arn:aws:sns:ap-southeast-2:230623977579:EC2-CPU-Alert-Topic`

An email subscription was configured for the topic, and its confirmation status was verified.

### Verification Command

```bash
aws sns list-subscriptions-by-topic \
  --region ap-southeast-2 \
  --topic-arn arn:aws:sns:ap-southeast-2:230623977579:EC2-CPU-Alert-Topic \
  --query 'Subscriptions[].{Protocol:Protocol,Email:Endpoint,Status:SubscriptionArn}' \
  --output table
```

### Verification Result

The email subscription returned a subscription ARN instead of `PendingConfirmation`, indicating that the subscription is confirmed.

**Note:** The SNS subscription is confirmed, but successful delivery of an actual CloudWatch alarm notification has not yet been verified.

## 4. Alarm History

The CloudWatch alarm history was inspected to check its state transitions.

### Command

```bash
aws cloudwatch describe-alarm-history \
  --region ap-southeast-2 \
  --alarm-name EC2-High-CPU-Alarm \
  --history-item-type StateUpdate \
  --max-items 20 \
  --query 'AlarmHistoryItems[].{Time:Timestamp,Summary:HistorySummary}' \
  --output table
```

### Observation

The alarm history showed a transition from `INSUFFICIENT_DATA` to `OK`.

- `INSUFFICIENT_DATA`: CloudWatch did not yet have enough metric data to evaluate the alarm.
- `OK`: The alarm is not currently detecting a threshold breach.
- `ALARM`: The configured threshold has been breached according to the alarm's evaluation rules.

A transition to `ALARM` and receipt of an associated notification have not yet been demonstrated.

## 5. Cost Threshold Alert — Permission Limitation

Cost-alert configuration was investigated using AWS Budgets.

The following permissions were denied for the current IAM user:

- `budgets:ViewBudget`
- `budgets:CreateBudget`

The IAM policy simulation also reported an explicit deny for:

- `cloudwatch:PutMetricAlarm`

As a result, the current user cannot create or modify the relevant monitoring resources with the existing permissions.

### Required Follow-Up

The AWS lab administrator should review the applicable IAM and organizational restrictions and provide the necessary permissions if cost-alert configuration is required.

**Status:** Cost threshold alert not configured because of AWS permissions restrictions.

## 6. Evidence and Screenshots

Create a `screenshots` directory to store the evidence:

```bash
mkdir -p screenshots
```

Suggested screenshots:

| Screenshot | Evidence |
|---|---|
| `screenshots/cpu-alarm-overview.png` | CloudWatch CPU alarm configuration and threshold |
| `screenshots/cpu-alarm-history.png` | Alarm state and history |
| `screenshots/sns-subscription-confirmed.png` | Confirmed SNS email subscription |
| `screenshots/cpu-metrics.png` | CPU utilization metric data |
| `screenshots/budget-permission-error.png` | AWS Budgets permission error |

Only include screenshots that have actually been captured.

## 7. Task Status

| Requirement | Status |
|---|---|
| Inspect CPU utilization alarm | Completed |
| Verify CPU threshold configuration | Completed |
| Retrieve CPU utilization metrics | Completed |
| Verify SNS email subscription | Completed |
| Verify actual alarm trigger | Pending |
| Verify actual notification delivery | Pending |
| Configure cost threshold alert | Blocked by AWS permissions |
| Document configuration and limitations | Completed |

## Conclusion

The existing CloudWatch CPU utilization alarm was inspected successfully in the Sydney region. Its threshold is configured at 70%, its actions are enabled, and its SNS email subscription is confirmed.

The alarm is currently in the `OK` state. An actual threshold breach and notification delivery have not yet been verified. Cost-alert configuration remains blocked by the current IAM permissions.

The current findings and limitations are documented for the AWS cloud internship task.
