# Task 1: Cloud Account Onboarding

## 1. Project Overview

**Internship:** WeIntern Cloud Internship  
**Task:** Task 1 — Cloud Account Onboarding  
**Cloud Provider:** Amazon Web Services (AWS)  
**Operating System:** Ubuntu Linux  
**AWS CLI Version:** 2.38.5  
**AWS Region:** Asia Pacific (Mumbai) — `ap-south-1`  
**IAM Username:** `swapnaadhav`

### Objective

The objective of this task was to set up the AWS command-line environment, configure AWS credentials, create and verify an IAM user, attach the required IAM policies, configure MFA, and review account permissions and resource-tagging conventions.

---

## 2. Prerequisites

The following tools and resources were used:

- Ubuntu Linux operating system.
- AWS Command Line Interface (AWS CLI) version 2.
- AWS account or authorized training environment.
- IAM user credentials with appropriate permissions.
- Internet connectivity.
- Access to the AWS Management Console.

---

## 3. AWS CLI Installation and Configuration

### Step 1: Verify AWS CLI Installation

The AWS CLI was installed on Ubuntu.

Command:

```bash
aws --version
```

Expected output format:

```text
aws-cli/2.38.5 Python/... Linux/...
```

**Status:** Completed.

### Step 2: Verify AWS CLI Configuration

The default AWS CLI profile was configured.

Command:

```bash
aws configure list
```

This command displays the configured credential sources, default region, and output format.

The configured AWS region for this task was:

```text
ap-south-1
```

**Status:** Completed.

### Step 3: Verify AWS Identity

The AWS Security Token Service (STS) command was used to verify the identity associated with the configured credentials.

Command:

```bash
aws sts get-caller-identity
```

Verified account details:

| Field | Value |
|---|---|
| AWS Account ID | `230623977579` |
| IAM Username | `swapnaadhav` |
| Identity Type | IAM User |
| Region Configured | `ap-south-1` |

The command successfully returned the AWS account ID, user ID, and Amazon Resource Name (ARN).

**Status:** Completed.

---

## 4. IAM User Verification

An IAM user named `swapnaadhav` was created for the internship activities.

### Command Used

```bash
aws iam get-user
```

### IAM User Details

| Field | Value |
|---|---|
| Username | `swapnaadhav` |
| IAM ARN | `arn:aws:iam::230623977579:user/swapnaadhav` |
| Path | `/` |
| Creation Date | `2026-10-25` |

The command successfully returned the IAM user details and associated tags.

**Status:** Completed.

---

## 5. IAM Policies and Permissions

The following AWS managed policies were considered for the internship tasks.

| Policy Name | Purpose | Recommendation |
|---|---|---|
| `AmazonS3FullAccess` | Full access to Amazon S3 resources | Attach only when required for the static website task |
| `CloudFrontFullAccess` | Manage CloudFront distributions | Attach when CDN configuration is required |
| `AmazonEC2ReadOnlyAccess` | View EC2 resources | Useful for EC2 monitoring and automation |
| `CloudWatchFullAccess` | Manage CloudWatch monitoring resources | Attach only when required |
| `IAMReadOnlyAccess` | View IAM users, roles, and policies | Useful for IAM verification |
| `IAMUserChangePassword` | Allow an IAM user to change their own password | Useful when applicable to the account configuration |

### Policy Verification

The following command lists the AWS managed policies attached to the IAM user:

```bash
aws iam list-attached-user-policies --user-name swapnaadhav
```

The user was configured with seven managed policies according to the onboarding checklist.

**Note:** Use the command output to verify the exact policy names attached to the user. The policy recommendations above are not a substitute for that output.

### Security Considerations

- Follow the principle of least privilege.
- Grant only the permissions required for each task.
- Avoid granting full access to AWS services unless necessary.
- Do not attach additional policies without authorization.
- Remember that AWS Organizations policies, permission boundaries, and explicit denies can restrict actions even when IAM policies grant permissions.

---

## 6. IAM User Tags

Tags were reviewed to support resource organization, identification, and cost management.

The following project tags were present on the IAM user.

| Tag Key | Tag Value |
|---|---|
| `Project` | `WeIntern-Internship` |
| `Environment` | `Learning` |
| `Owner` | `Swapna` |

### Tag Verification Command

```bash
aws iam get-user
```

The output confirmed that the three expected project tags were present.

An additional tag was also found:

| Tag Key | Tag Value |
|---|---|
| `AKIATLMSCUBVZKKI6E4K` | `AWS CLI on Ubuntu` |

This additional tag requires review because its key resembles an AWS access key ID.

It should be confirmed with the mentor or account administrator whether this tag was intentionally added. Do not expose access keys or other credentials in project documentation.

### Tagging Convention

The standard tagging convention for this project is:

- **Project:** `WeIntern-Internship`
- **Environment:** `Learning`
- **Owner:** `Swapna`

These tags help identify the project, its environment, and its owner.

---

## 7. Multi-Factor Authentication (MFA)

MFA was reviewed during the onboarding process.

### AWS Builder ID MFA

MFA was enabled for the AWS Builder ID.

**Status:** Completed.

### IAM User MFA

The IAM user did not have an MFA device registered.

Verification command:

```bash
aws iam list-mfa-devices --user-name swapnaadhav
```

The command returned an empty list:

```json
{
    "MFADevices": []
}
```

### Issue Identified

IAM user MFA setup was blocked because the current IAM user lacked the required permission to create a virtual MFA device.

The missing permission reported during setup was:

```text
iam:CreateVirtualMFADevice
```

Depending on the setup process, additional permissions may also be required to assign and manage the MFA device.

### Recommended Action

Contact the mentor or AWS account administrator to request assistance with IAM MFA configuration.

**Important:** AWS Builder ID MFA and IAM user MFA are separate authentication configurations. Enabling one does not automatically enable the other.

---

## 8. Access Key Verification

The IAM user's access-key metadata was checked using the AWS CLI.

Command:

```bash
aws iam list-access-keys --user-name swapnaadhav
```

The output showed one active access key.

| Field | Status |
|---|---|
| IAM Username | `swapnaadhav` |
| Access Key Status | Active |
| Access Key Creation Date | `2026-10-25` |

The access key was configured for AWS CLI use on Ubuntu.

### Security Best Practices

- Never upload access keys or secret access keys to GitHub.
- Never include secret access keys in README files or screenshots.
- Avoid sharing credentials in reports or messages.
- Rotate or deactivate credentials if they are exposed.
- Use temporary credentials or an approved role-based authentication method when available.

The access key ID itself is not a secret authentication credential, but it should still be handled carefully and omitted from public documentation unless required.

---

## 9. AWS Sandbox Access Verification

Access to certain AWS services was tested during onboarding.

### S3 Access

An attempt to list S3 buckets was restricted by the AWS environment.

### EC2 Access

An attempt to describe EC2 regions was also restricted.

### Issue Identified

The AWS environment reported access-denied errors associated with an organization-level explicit deny.

An explicit deny takes precedence over an allow granted by an IAM policy.

Therefore, attaching additional IAM policies alone may not resolve these restrictions.

### Recommended Action

Ask the mentor or account administrator to confirm:

1. Whether the training account permits S3 and EC2 operations.
2. Whether a dedicated AWS training sandbox is available.
3. Which services are allowed for the internship tasks.
4. Whether any additional permissions are required.
5. Whether the restrictions are intentional security controls.

**Status:** Partially verified; some service operations remain restricted.

---

## 10. Onboarding Checklist

| No. | Requirement | Status | Evidence or Notes |
|---|---|---|---|
| 1 | Install AWS CLI | Completed | AWS CLI v2.38.5 installed on Ubuntu |
| 2 | Configure AWS CLI | Completed | Default profile configured |
| 3 | Configure AWS Region | Completed | `ap-south-1` |
| 4 | Verify AWS Identity | Completed | `aws sts get-caller-identity` succeeded |
| 5 | Create IAM User | Completed | `swapnaadhav` |
| 6 | Attach IAM Policies | Completed | Seven managed policies reported in the checklist |
| 7 | Configure Builder ID MFA | Completed | MFA enabled |
| 8 | Configure IAM User MFA | Blocked | Required permissions unavailable |
| 9 | Verify AWS Sandbox Access | Restricted | Some operations denied |
| 10 | Review Tagging Conventions | Partially Completed | Expected tags present; additional tag needs review |

---

## 11. AWS CLI Commands Reference

The following commands were used to verify the onboarding configuration.

### Check AWS CLI Version

```bash
aws --version
```

### Check AWS CLI Configuration

```bash
aws configure list
```

### Verify AWS Identity

```bash
aws sts get-caller-identity
```

### Get IAM User Details

```bash
aws iam get-user
```

### List Attached Managed Policies

```bash
aws iam list-attached-user-policies --user-name swapnaadhav
```

### List Inline IAM Policies

```bash
aws iam list-user-policies --user-name swapnaadhav
```

### Check IAM MFA Devices

```bash
aws iam list-mfa-devices --user-name swapnaadhav
```

### List IAM Access-Key Metadata

```bash
aws iam list-access-keys --user-name swapnaadhav
```

These commands can be run again to verify the current configuration, provided the configured identity has the required permissions.

---

## 12. Issues and Recommendations

### Issue 1: IAM User MFA

**Problem:** The IAM user has no registered MFA device.

**Cause:** The current identity lacks the required permission to create a virtual MFA device.

**Recommendation:** Request assistance from the AWS account administrator or mentor.

### Issue 2: Restricted AWS Service Access

**Problem:** Certain S3 and EC2 operations were denied.

**Cause:** The environment reported an organization-level explicit deny.

**Recommendation:** Confirm the permitted services and available sandbox permissions with the mentor.

### Issue 3: Additional IAM User Tag

**Problem:** An unexpected tag key resembling an access key ID was present.

**Recommendation:** Confirm whether the tag is intentional and remove or correct it only if authorized.

### Issue 4: Least-Privilege Policy Review

**Problem:** Some recommended policies grant broad permissions.

**Recommendation:** Review the exact managed policies attached to the IAM user and retain only those necessary for the assigned internship tasks.

---

## 13. Mentor Communication

The following message can be used to report the outstanding issues.

**Subject: Task 1 — Cloud Account Onboarding Status and Permission Clarification**

Hi,

I have completed most of the Cloud Account Onboarding task.

**Completed:**
- Installed AWS CLI v2 on Ubuntu.
- Configured the default AWS CLI profile and Mumbai region (`ap-south-1`).
- Verified my AWS identity using STS.
- Created and verified the IAM user `swapnaadhav`.
- Configured the initial managed policies.
- Enabled MFA for my AWS Builder ID.
- Reviewed the IAM user tags and access-key metadata.

**Pending / Blocked:**
- IAM user MFA setup is blocked because the current IAM user lacks the required permission to create a virtual MFA device.
- Access to some AWS services, including certain S3 and EC2 operations, is restricted by an organization-level explicit deny.
- One additional IAM user tag requires clarification.

Could you please confirm whether a training sandbox with the required permissions is available and advise how I should complete the remaining onboarding steps?

Thank you.

---

## 14. Learning Outcomes

Through this task, I learned how to:

- Install and configure AWS CLI on Ubuntu.
- Configure an AWS region and default profile.
- Verify AWS identity using STS.
- Create and inspect IAM users.
- Review managed IAM policies and access permissions.
- Inspect IAM MFA device configuration.
- Verify access-key metadata.
- Review IAM tags and project tagging conventions.
- Identify permission-denied errors and understand the impact of organization-level restrictions.
- Apply basic AWS credential-security and least-privilege practices.

---

## 15. Conclusion

The main AWS account onboarding activities were completed successfully. The AWS CLI was installed and configured, the IAM user was verified, the initial policies were configured, and the required project tags were reviewed.

IAM user MFA registration and access to certain AWS services remain pending because of permission restrictions. These issues have been documented for review with the mentor or AWS account administrator.

This task established the initial AWS CLI and IAM foundation for the remaining WeIntern Cloud Internship tasks.

---

**Task:** Task 1 — Cloud Account Onboarding  
**Project:** WeIntern-Internship  
**Environment:** Learning  
**Owner:** Swapna  
**Region:** `ap-south-1`  
**Status:** Mostly Completed — Permission-Related Items Pending
