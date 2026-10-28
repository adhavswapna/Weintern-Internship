# WEINTERN CLOUD INTERNSHIP – TASK 3
## Deploying a Static Website Using Amazon S3 and CloudFront

### 📌 Project Overview

This project demonstrates how to deploy a static website using **Amazon S3 and Amazon CloudFront**. The website files are stored in an Amazon S3 bucket, and CloudFront distributes the website content to users through a CDN (Content Delivery Network).

The project was completed as part of the **WeIntern Cloud Internship – Task 3**.

### 🎯 Objectives

- Create an Amazon S3 bucket to store static website files.
- Upload the website's `index.html` file to S3.
- Configure Amazon CloudFront as a content delivery network.
- Use Origin Access Control (OAC) to help secure access to the S3 origin.
- Verify that the website is accessible through the CloudFront distribution.
- Document the deployment process and AWS CLI commands.

---

## 🏗️ Architecture

```text
                  User / Web Browser
                         |
                         v
                Amazon CloudFront
                 (CDN Distribution)
                         |
                         v
                Origin Access Control
                         |
                         v
                 Private Amazon S3
                  (index.html)
```

**How it works:**

1. The website's HTML file is uploaded to Amazon S3.
2. Amazon CloudFront receives requests from users.
3. CloudFront retrieves website content from the S3 origin.
4. CloudFront delivers the content to the user's browser.
5. Origin Access Control (OAC), when correctly configured with the S3 bucket policy, restricts direct origin access and allows CloudFront to access the private bucket.

---

## ☁️ AWS Resources

| Resource | Details |
|---|---|
| Cloud Provider | Amazon Web Services (AWS) |
| AWS Region | `ap-southeast-2` |
| S3 Bucket Name | `weintern-task3-s3-swapnaadhav` |
| CloudFront Distribution ID | `EAGMUDC8KCZVQ` |
| CloudFront Domain | `dwpuiw40xj1jx.cloudfront.net` |
| Origin Access Control ID | `E2M1DLNO7XA6O4` |
| Website File | `index.html` |
| Encryption | Amazon S3 managed encryption (AES256) |
| Source Code Repository | [Weintern-Internship](https://github.com/adhavswapna/Weintern-Internship) |

> **Note:** The AWS account ID and IAM username have been omitted from this public README for security and privacy. Avoid publishing credentials, access keys, secret keys, or other sensitive information.

---

## 🛠️ Technologies Used

- **Amazon S3:** Stores the website's static files.
- **Amazon CloudFront:** Distributes website content through AWS edge locations.
- **Origin Access Control (OAC):** Helps secure the connection between CloudFront and a private S3 bucket.
- **AWS CLI:** Used to create, configure, and verify AWS resources.
- **Git and GitHub:** Used for source control and project documentation.
- **HTML:** Used to create the static website.

---

## 🚀 Implementation Steps

### Step 1: Configure AWS CLI

Configure the AWS CLI with an IAM user or role that has the required permissions.

```bash
aws configure
```

Set the AWS region:

```bash
aws configure set region ap-southeast-2
```

Verify the active AWS identity:

```bash
aws sts get-caller-identity
```

**Security note:** Do not store AWS access keys or secret keys in this README or commit them to GitHub.

### Step 2: Create the S3 Bucket

Create the S3 bucket in the `ap-southeast-2` region.

```bash
aws s3api create-bucket \
  --bucket weintern-task3-s3-swapnaadhav \
  --region ap-southeast-2 \
  --create-bucket-configuration LocationConstraint=ap-southeast-2
```

> Run this command only if the bucket does not already exist and you have permission to create it. S3 bucket names must be globally unique.

### Step 3: Block Public Access

Keep all four S3 Block Public Access settings enabled.

```bash
aws s3api put-public-access-block \
  --bucket weintern-task3-s3-swapnaadhav \
  --public-access-block-configuration \
  "BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=true,RestrictPublicBuckets=true"
```

Verify the settings:

```bash
aws s3api get-public-access-block \
  --bucket weintern-task3-s3-swapnaadhav
```

### Step 4: Upload the Website

Upload the `index.html` file to the S3 bucket.

```bash
aws s3 cp index.html \
  s3://weintern-task3-s3-swapnaadhav/index.html \
  --content-type text/html
```

Check that the file exists:

```bash
aws s3api head-object \
  --bucket weintern-task3-s3-swapnaadhav \
  --key index.html
```

The object metadata should identify the content type as `text/html`. The recorded verification also showed AES256 server-side encryption.

### Step 5: Configure Amazon CloudFront

Create or configure a CloudFront distribution with the following settings:

- **Origin:** The S3 bucket's REST endpoint.
- **Origin access:** Origin Access Control (OAC).
- **Default root object:** `index.html`.
- **Viewer protocol policy:** Redirect HTTP to HTTPS.
- **Allowed methods:** GET and HEAD for a basic static website.
- **Origin security:** Keep the S3 bucket private and configure its bucket policy to allow the intended CloudFront distribution to read the required objects.

The distribution used in this project is:

- **Distribution ID:** `EAGMUDC8KCZVQ`
- **CloudFront domain:** `dwpuiw40xj1jx.cloudfront.net`
- **OAC ID:** `E2M1DLNO7XA6O4`

**Important:** Confirm these settings in the AWS Console before assuming the configuration is complete. The distribution and OAC IDs alone do not prove that the S3 origin, OAC association, and bucket policy are all correct.

### Step 6: Verify the CloudFront Distribution

Check the distribution status:

```bash
aws cloudfront get-distribution \
  --id EAGMUDC8KCZVQ \
  --query 'Distribution.Status' \
  --output text
```

A status of `Deployed` means that the distribution configuration has finished deploying.

Check the default root object:

```bash
aws cloudfront get-distribution \
  --id EAGMUDC8KCZVQ \
  --query 'Distribution.DistributionConfig.DefaultRootObject' \
  --output text
```

The expected value for this project is:

```text
index.html
```

### Step 7: Test the Website

Open the CloudFront domain in a web browser:

**Website URL:** https://dwpuiw40xj1jx.cloudfront.net/

Or test it from the terminal:

```bash
curl -I https://dwpuiw40xj1jx.cloudfront.net/
```

The recorded test returned:

```text
HTTP/2 200
```

An HTTP `200` response indicates that the request succeeded at the time of testing.

---

## 🔄 Updating Website Content

After changing `index.html`, upload the updated file:

```bash
aws s3 cp index.html \
  s3://weintern-task3-s3-swapnaadhav/index.html \
  --content-type text/html
```

To request a CloudFront cache refresh, create an invalidation:

```bash
aws cloudfront create-invalidation \
  --distribution-id EAGMUDC8KCZVQ \
  --paths "/*"
```

Check the invalidation status:

```bash
aws cloudfront list-invalidations \
  --distribution-id EAGMUDC8KCZVQ
```

Wait until the invalidation status is `Completed` before considering the cache refresh finished.

---

## 🔐 Security Best Practices

- Keep S3 Block Public Access enabled.
- Use Origin Access Control with the CloudFront S3 origin.
- Ensure the S3 bucket policy grants read access only to the intended CloudFront distribution.
- Use HTTPS for website visitors.
- Follow the principle of least privilege when assigning IAM permissions.
- Never commit AWS access keys, secret keys, passwords, or session tokens to GitHub.
- Avoid including AWS account identifiers or personal details in public documentation unless required.
- Review CloudFront access logs and AWS resource settings when necessary.

---

## 🧰 Troubleshooting

| Problem | Possible Cause | Suggested Solution |
|---|---|---|
| `403 Forbidden` | Incorrect S3 bucket policy or CloudFront origin configuration | Verify the OAC association and bucket policy. |
| `404 Not Found` | Missing `index.html` or incorrect default root object | Check the S3 object key and CloudFront default root object. |
| Old website content appears | CloudFront cached the previous version | Create an invalidation and wait for completion. |
| CloudFront status is not `Deployed` | Distribution changes are still being applied | Check the distribution status again later. |
| AWS CLI access denied | IAM permissions are insufficient | Review the IAM permissions for the required operation. |
| Direct S3 access is denied | The bucket is private | Access the website through CloudFront and verify OAC configuration. |

---

## 📂 Repository Structure

```text
Weintern-Internship/
├── README.md
└── index.html
```

The repository may contain additional files depending on the final project structure.

---

## 📈 Learning Outcomes

Through this project, I learned how to:

- Store and manage static website files using Amazon S3.
- Configure and verify S3 Block Public Access.
- Understand the role of CloudFront in content delivery.
- Understand Origin Access Control and private S3 origins.
- Use AWS CLI commands to inspect AWS resources.
- Test a website using HTTP response headers.
- Manage website updates and CloudFront cache invalidations.
- Document cloud deployment steps using Markdown and GitHub.

---

## 🏁 Conclusion

This project demonstrates the deployment of a static website using Amazon S3 and Amazon CloudFront. The website content is stored in S3, while CloudFront provides a distribution endpoint for accessing the content.

The recorded deployment reached the `Deployed` status, and the website endpoint returned an HTTP `200` response during testing. The S3 object metadata also showed the expected HTML content type and AES256 encryption.

For a secure final configuration, verify that the CloudFront distribution uses the intended S3 origin and OAC, and that the bucket policy restricts access appropriately.

---

## 👩‍💻 Author

**Swapna Adhav**

Cloud Internship Project – WeIntern

**GitHub Repository:**  
https://github.com/adhavswapna/Weintern-Internship.git
