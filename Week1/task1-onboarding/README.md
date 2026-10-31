# Task 1: Cloud Environment Onboarding

## Overview

This task covers the initial setup and verification of the AWS cloud environment for the WeIntern Cloud Internship. It includes AWS CLI installation and configuration, identity verification, IAM user review, MFA status checks, and security best practices.

## Objectives

- Understand the AWS cloud environment.
- Install and verify AWS CLI.
- Configure and verify the AWS region.
- Verify the active AWS identity.
- Review IAM users, permissions, and security policies.
- Understand MFA and access security.
- Follow resource-tagging conventions.
- Identify and document AWS access restrictions.

## AWS Environment

| Setting | Details |
|---|---|
| Cloud Provider | Amazon Web Services (AWS) |
| Environment | AWS Builder Lab |
| Operating System | Ubuntu Linux |
| AWS CLI | Version 2.x |
| IAM Username | `swapnaadhav` |
| Default Region | Sydney |
| Region Code | `ap-southeast-2` |
| Project | `WeIntern-Internship` |
| Environment Tag | `Learning` |
| Owner Tag | `Swapna` |

## 1. AWS CLI Installation and Configuration

AWS CLI is used to interact with AWS services through the terminal.

Verify the AWS CLI installation:

```bash
aws --version
```

Configure AWS CLI:

```bash
aws configure
```

Check the current configuration:

```bash
aws configure list
```

Check the configured default region:

```bash
aws configure get region
```

The configured region for the internship tasks is Sydney (`ap-southeast-2`).

## 2. AWS Identity Verification

The AWS Security Token Service (STS) command was used to verify the active AWS identity.

```bash
aws sts get-caller-identity
```

Identity verification was successful.

The command returned the AWS account ID and IAM user ARN, confirming that the AWS CLI was authenticated with the expected account.

## 3. IAM User Verification

AWS Identity and Access Management (IAM) controls access to AWS services and resources.

The IAM user details were checked using:

```bash
aws iam get-user
```

The IAM username was verified as:

`swapnaadhav`

## 4. IAM Policy Review

The IAM policies attached to the user were reviewed.

List attached managed policies:

```bash
aws iam list-attached-user-policies --user-name swapnaadhav
```

List inline policies:

```bash
aws iam list-user-policies --user-name swapnaadhav
```

The inline policy command returned an empty policy list.

This indicates that no inline policies were attached to the IAM user. Managed policies were reviewed separately.

## 5. Multi-Factor Authentication (MFA)

MFA provides an additional layer of security for AWS account access.

Two separate MFA configurations were reviewed:

### AWS Builder ID MFA
- AWS Builder ID MFA was enabled separately.
- It is separate from IAM user MFA.

### IAM User MFA
- IAM user MFA enrollment is still pending.
- No IAM MFA device was registered during verification.
- The previous enrollment attempt was blocked because the required IAM permission was unavailable.
- Additional permissions or administrator assistance are required.

Check registered IAM MFA devices:

```bash
aws iam list-mfa-devices --user-name swapnaadhav
```

## 6. IAM Access Key Verification

The IAM access-key configuration was reviewed using:

```bash
aws iam list-access-keys --user-name swapnaadhav
```

An active access key was identified for AWS CLI authentication.

**Security note:** Access key IDs and secret access keys must not be shared publicly or committed to GitHub. Credentials should be stored securely.

## 7. Resource Tagging

Resource tags help organize and identify AWS resources.

The project tagging conventions were reviewed.

| Tag Key | Example Value |
|---|---|
| Project | `WeIntern-Internship` |
| Environment | `Learning` |
| Owner | `Swapna` |

These tags should be applied to internship resources according to the project conventions.

An unusual IAM tag was also identified and requires confirmation from the mentor or administrator.

## 8. AWS Security Best Practices

The following security practices were considered during onboarding:

- Follow the principle of least privilege.
- Enable MFA wherever permissions allow.
- Protect AWS access keys and secret credentials.
- Review IAM users and attached policies.
- Use the correct AWS region for assigned tasks.
- Apply consistent resource tags.
- Avoid unnecessary administrator permissions.
- Never commit credentials to GitHub.
- Follow AWS Builder Lab restrictions.

## 9. Access Restrictions and Challenges

Some AWS operations returned `AccessDenied` errors because of IAM permissions or AWS Builder Lab organization-level restrictions.

The IAM MFA enrollment was also blocked because the required permission was unavailable.

When an operation is denied:

1. Review the error message.
2. Verify the active AWS identity and region.
3. Check the permissions required for the operation.
4. Document the restriction.
5. Contact the mentor or administrator if additional access is required.

These restrictions were documented rather than bypassed.

## 10. Key Learnings

- Installed and configured AWS CLI on Ubuntu.
- Verified AWS identity using STS.
- Reviewed IAM user details and policies.
- Understood the difference between AWS Builder ID MFA and IAM user MFA.
- Reviewed access-key security.
- Understood AWS resource-tagging conventions.
- Learned how IAM permissions and organizational restrictions affect AWS operations.
- Practised following least-privilege security principles.

## 11. Task Outcome

The AWS cloud environment was successfully onboarded and verified using AWS CLI.

IAM user details, policies, MFA configuration, access keys, and resource-tagging conventions were reviewed.

Some IAM operations remain restricted due to unavailable permissions. These items have been documented for mentor or administrator follow-up.

## Task 1 Completion Summary

| Activity | Status |
|---|---|
| AWS CLI installation | Completed |
| AWS CLI configuration | Completed |
| Sydney region configuration | Completed |
| AWS identity verification | Completed |
| IAM user verification | Completed |
| IAM managed policy review | Reviewed |
| Inline policy review | Completed – no inline policies found |
| AWS Builder ID MFA | Enabled |
| IAM user MFA | Pending – permission required |
| Access key review | Completed |
| Resource tagging review | Completed |
| Access restrictions documentation | Completed |
