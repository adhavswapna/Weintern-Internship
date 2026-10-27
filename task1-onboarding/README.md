# Task 1: Cloud Environment Onboarding

## Overview
This task covers the initial setup and verification of the AWS cloud environment for the WeIntern Cloud Internship.

## Objectives
- Understand the AWS cloud environment.
- Verify AWS CLI installation and configuration.
- Review IAM users, permissions, and security policies.
- Understand MFA and access security.
- Follow the required AWS region and resource-tagging conventions.

## AWS Environment

| Setting | Details |
|---|---|
| Cloud Provider | Amazon Web Services (AWS) |
| Environment | AWS Builder Lab |
| Default Region | Sydney |
| Region Code | `ap-southeast-2` |
| Project | WeIntern-Internship |
| Environment Tag | Learning |
| Owner Tag | Swapna |

## AWS CLI Verification

The AWS CLI is used to interact with AWS services from the terminal.

Verify the AWS CLI installation:

```bash
aws --version
```

Verify the configured AWS identity:

```bash
aws sts get-caller-identity --region ap-southeast-2
```

Check the configured region:

```bash
aws configure get region
```

For internship tasks, use the Sydney region, `ap-southeast-2`.

## IAM and Security

AWS Identity and Access Management (IAM) controls access to AWS services and resources.

Important security practices include:
- Use only the permissions required for assigned tasks.
- Avoid sharing access keys or secret credentials.
- Enable MFA wherever permitted.
- Review attached IAM policies and access permissions.
- Follow the AWS Builder Lab's access restrictions.

### IAM Verification Commands

List attached managed policies:

```bash
aws iam list-attached-user-policies --user-name swapnaadhav
```

List inline policies:

```bash
aws iam list-user-policies --user-name swapnaadhav
```

Check registered IAM MFA devices:

```bash
aws iam list-mfa-devices --user-name swapnaadhav
```

## Resource Tagging

Consistent resource tags help identify and organize internship resources.

| Tag Key | Example Value |
|---|---|
| Project | `WeIntern-Internship` |
| Environment | `Learning` |
| Owner | `Swapna` |

Apply the required tags when creating AWS resources, following the internship naming conventions.

## Access Restrictions

Some AWS operations may return `AccessDenied` because of IAM permissions or AWS Builder Lab organization-level restrictions.

If an operation is denied:
1. Review the error message.
2. Verify the active AWS identity and region.
3. Check the permissions required for the operation.
4. Contact the mentor or administrator if additional access is required.

## Outcome

The AWS environment, CLI configuration, IAM concepts, security practices, and resource-tagging conventions have been reviewed. Any remaining permission restrictions should be resolved with the mentor or administrator before proceeding with operations that require additional access.
