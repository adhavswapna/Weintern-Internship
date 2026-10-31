# WEINTERN CLOUD INTERNSHIP – TASK 3

## Deploying a Static Website Using Amazon S3 and CloudFront

## 1. Project Overview

This project demonstrates the deployment of a responsive static portfolio website using **Amazon S3 and Amazon CloudFront**.

The website is developed using HTML and CSS and hosted in a private Amazon S3 bucket. Amazon CloudFront acts as a Content Delivery Network (CDN), distributing website content to users over HTTPS.

Origin Access Control (OAC) is configured to allow CloudFront to securely access the private S3 bucket without making the bucket publicly accessible.

This project was completed as part of the **WeIntern Cloud Internship – Week 1, Task 3**.

## 2. Objectives

- Create an Amazon S3 bucket for storing static website files.
- Develop and upload a responsive HTML portfolio website.
- Configure Amazon CloudFront as a content delivery network.
- Configure Origin Access Control (OAC).
- Keep the S3 bucket private using Block Public Access.
- Configure a bucket policy allowing access only through the intended CloudFront distribution.
- Enable HTTPS for secure website delivery.
- Verify the deployment using AWS CLI and a web browser.
- Document the deployment process and configuration files.

---

## 3. Project Architecture

```text
                 User / Web Browser
                         |
                         | HTTPS
                         v
                 Amazon CloudFront
                   (CDN Distribution)
                         |
                         v
                Origin Access Control
                      (OAC)
                         |
                         v
                  Private Amazon S3
                    (index.html)
```

### How the Architecture Works

1. The portfolio website is developed using HTML and CSS.
2. The `index.html` file is uploaded to an Amazon S3 bucket.
3. The S3 bucket remains private with all Block Public Access settings enabled.
4. Amazon CloudFront receives requests from website visitors.
5. CloudFront uses Origin Access Control (OAC) to authenticate requests to the S3 origin.
6. The S3 bucket policy allows `s3:GetObject` access only to the configured CloudFront distribution.
7. CloudFront delivers website content to visitors over HTTPS.

---

## 4. AWS Resources

| Resource | Configuration |
|---|---|
| Cloud Provider | Amazon Web Services (AWS) |
| AWS Region | Asia Pacific (Sydney) |
| Region Code | `ap-southeast-2` |
| S3 Bucket | `weintern-task3-s3-swapnaadhav` |
| CloudFront Distribution ID | `EAGMUDC8KCZVQ` |
| CloudFront Domain | `dwpuiw40xj1jx.cloudfront.net` |
| Origin Access Control ID | `E2M1DLNO7XA6O4` |
| OAC Name | `weintern-task3-oac-swapnaadhav` |
| Default Root Object | `index.html` |
| Viewer Protocol Policy | Redirect HTTP to HTTPS |
| Encryption | AES256 |
| Allowed Methods | GET and HEAD |
| Price Class | PriceClass_100 |

### Deployed Website

**Website URL:**

https://dwpuiw40xj1jx.cloudfront.net/

The website presents a personal portfolio introducing Swapna Adhav as a DevOps Intern and highlighting the AWS static website deployment project.

---

## 5. Technologies Used

| Technology | Purpose |
|---|---|
| Amazon S3 | Stores static website files |
| Amazon CloudFront | Distributes website content |
| Origin Access Control | Secures access between CloudFront and S3 |
| AWS CLI | Creates, configures and verifies AWS resources |
| HTML5 | Structures the portfolio website |
| CSS3 | Website styling and responsive design |
| Git | Version control |
| GitHub | Source code hosting and documentation |
| Ubuntu Linux | Development environment |

---

## 6. Repository Structure

```text
task3-static-website/
│
├── README.md
│
├── index.html
│
├── distribution-config.json
│
├── oac-config.json
│
└── bucket-policy.json
```

### File Description

| File | Description |
|---|---|
| `README.md` | Project documentation and deployment instructions |
| `index.html` | Responsive personal portfolio website |
| `distribution-config.json` | CloudFront distribution configuration |
| `oac-config.json` | Origin Access Control configuration |
| `bucket-policy.json` | S3 bucket policy allowing CloudFront access |

---

## 7. Implementation Steps

### Step 1: Configure AWS CLI

Configure AWS CLI with an IAM user or role that has the required permissions.

```bash
aws configure
```

Set the AWS region:

```bash
aws configure set region ap-southeast-2
```

Verify the AWS identity:

```bash
aws sts get-caller-identity
```

**Security:** Never include AWS access keys, secret keys or session tokens in GitHub repositories.

### Step 2: Create the S3 Bucket

Create the S3 bucket in the Sydney region.

```bash
aws s3api create-bucket \
  --bucket weintern-task3-s3-swapnaadhav \
  --region ap-southeast-2 \
  --create-bucket-configuration LocationConstraint=ap-southeast-2
```

Run this command only if the bucket does not already exist.

### Step 3: Enable S3 Block Public Access

Enable all four Block Public Access settings.

```bash
aws s3api put-public-access-block \
  --bucket weintern-task3-s3-swapnaadhav \
  --public-access-block-configuration \
  "BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=true,RestrictPublicBuckets=true"
```

Verify the configuration:

```bash
aws s3api get-public-access-block \
  --bucket weintern-task3-s3-swapnaadhav
```

This ensures that the bucket is not publicly accessible.

### Step 4: Upload the Website

Upload the portfolio website to Amazon S3.

```bash
aws s3 cp index.html \
  s3://weintern-task3-s3-swapnaadhav/index.html \
  --content-type text/html
```

Verify the uploaded object:

```bash
aws s3api head-object \
  --bucket weintern-task3-s3-swapnaadhav \
  --key index.html
```

The verification confirmed:

- Content type: `text/html`
- Server-side encryption: `AES256`

### Step 5: Configure Origin Access Control

Origin Access Control (OAC) was configured to secure communication between CloudFront and the S3 origin.

Configuration used in `oac-config.json`:

```json
{
  "Name": "weintern-task3-oac-swapnaadhav",
  "Description": "OAC for WeIntern Internship Task 3",
  "SigningProtocol": "sigv4",
  "SigningBehavior": "always",
  "OriginAccessControlOriginType": "s3"
}
```

The OAC uses AWS Signature Version 4 (SigV4) to sign requests sent from CloudFront to S3.

### Step 6: Configure the S3 Bucket Policy

The bucket policy allows the CloudFront service principal to retrieve website objects.

The policy uses the CloudFront distribution ARN as a condition to restrict access.

Configuration stored in `bucket-policy.json`:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowCloudFrontServicePrincipalReadOnly",
      "Effect": "Allow",
      "Principal": {
        "Service": "cloudfront.amazonaws.com"
      },
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::weintern-task3-s3-swapnaadhav/*",
      "Condition": {
        "StringEquals": {
          "AWS:SourceArn": "arn:aws:cloudfront::230623977579:distribution/EAGMUDC8KCZVQ"
        }
      }
    }
  ]
}
```

**Security:** The policy grants read-only object access to the intended CloudFront distribution rather than allowing public access.

### Step 7: Configure Amazon CloudFront

The CloudFront distribution was configured with the following settings:

- S3 bucket REST endpoint as the origin.
- Origin Access Control (OAC) attached to the origin.
- Default root object set to `index.html`.
- Viewer protocol policy set to `redirect-to-https`.
- Allowed methods restricted to GET and HEAD.
- CloudFront default SSL certificate enabled.
- Price class set to `PriceClass_100`.

The distribution configuration is documented in:

`distribution-config.json`

### Step 8: Verify CloudFront Distribution

Check the distribution deployment status:

```bash
aws cloudfront get-distribution \
  --id EAGMUDC8KCZVQ \
  --query 'Distribution.Status' \
  --output text
```

Expected result:

```text
Deployed
```

Verify the default root object:

```bash
aws cloudfront get-distribution \
  --id EAGMUDC8KCZVQ \
  --query 'Distribution.DistributionConfig.DefaultRootObject' \
  --output text
```

Expected result:

```text
index.html
```

### Step 9: Test the Website

Open the deployed website:

https://dwpuiw40xj1jx.cloudfront.net/

Alternatively, test the website using:

```bash
curl -I https://dwpuiw40xj1jx.cloudfront.net/
```

Recorded response:

```text
HTTP/2 200
```

An HTTP 200 response confirms that the website request was successful during testing.

---

## 8. Updating Website Content

Whenever the website is modified, upload the updated HTML file.

```bash
aws s3 cp index.html \
  s3://weintern-task3-s3-swapnaadhav/index.html \
  --content-type text/html
```

To refresh cached content in CloudFront, create an invalidation.

```bash
aws cloudfront create-invalidation \
  --distribution-id EAGMUDC8KCZVQ \
  --paths "/*"
```

Check invalidation status:

```bash
aws cloudfront list-invalidations \
  --distribution-id EAGMUDC8KCZVQ
```

Wait until the invalidation status becomes `Completed`.

---

## 9. Security Best Practices

The following security practices were considered during deployment:

- Enabled all four Amazon S3 Block Public Access settings.
- Kept the S3 bucket private.
- Used Origin Access Control (OAC).
- Restricted S3 object access through the CloudFront distribution ARN.
- Enabled HTTPS redirection through CloudFront.
- Used least-privilege access principles.
- Avoided exposing AWS credentials in source code.
- Avoided publishing sensitive account information in public documentation.

---

## 10. Troubleshooting

| Issue | Possible Cause | Solution |
|---|---|---|
| 403 Forbidden | Incorrect bucket policy or OAC configuration | Verify the OAC association and bucket policy |
| 404 Not Found | Missing `index.html` | Check the uploaded S3 object |
| Old website content | CloudFront cache | Create a cache invalidation |
| Distribution not deployed | Configuration changes are processing | Check the distribution status later |
| Access Denied | Insufficient IAM permissions | Review IAM permissions |
| Direct S3 access denied | S3 bucket is private | Access the website through CloudFront |

---

## 11. Learning Outcomes

Through this project, I gained practical experience in:

- Deploying a static website using Amazon S3.
- Understanding Amazon CloudFront and CDN functionality.
- Configuring Origin Access Control.
- Securing private S3 bucket access.
- Working with AWS bucket policies.
- Using AWS CLI for cloud resource management.
- Understanding HTTPS-based content delivery.
- Managing CloudFront cache invalidations.
- Creating and maintaining AWS configuration files.
- Documenting cloud deployment projects using Markdown and GitHub.

---

## 12. Conclusion

This project successfully demonstrates the deployment of a responsive static portfolio website using Amazon S3 and Amazon CloudFront.

The website files are stored in a private S3 bucket, while CloudFront provides secure content delivery over HTTPS. Origin Access Control helps protect the S3 origin by allowing access through the configured CloudFront distribution.

The deployment reached the `Deployed` status, and the website returned an HTTP `200` response during verification.

This task provided practical knowledge of AWS storage, content delivery, access control, security configurations and static website deployment.

---

## 13. Author

**Swapna Adhav**

Cloud DevOps Intern  
WeIntern Cloud Internship – Week 1

**GitHub Repository:**

https://github.com/adhavswapna/Weintern-Internship.git

**Deployed Portfolio Website:**

https://dwpuiw40xj1jx.cloudfront.net/
