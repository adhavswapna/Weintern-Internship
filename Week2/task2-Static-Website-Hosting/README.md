# WeIntern Cloud Computing Internship – Week 2

# Task 2: Static Website Hosting Using AWS S3

## 1. Objective

Deploy a static website to the cloud using AWS S3 Static Website Hosting. Configure bucket policies, enable public access, and set up an optional CloudFront CDN distribution for improved website delivery.

## 2. Key Requirements

The following requirements were covered in this task:

- Create an S3 bucket configured for static website hosting.
- Upload website files (HTML, CSS, JavaScript, and other assets).
- Configure the bucket policy for public read access.
- Set the index and error document settings.
- Verify website accessibility through the S3 website endpoint.
- Configure an optional CloudFront distribution for CDN delivery.

## 3. Recommended Tech Stack

| Component | Technology |
|---|---|
| Cloud Provider | AWS |
| Storage Service | Amazon S3 |
| CDN (Optional) | AWS CloudFront |
| DNS (Optional) | AWS Route 53 |
| Website | Static HTML/CSS/JavaScript |
| Deployment Method | AWS Management Console |

## 4. AWS Configuration

| Configuration | Details |
|---|---|
| AWS Region | Asia Pacific (Sydney) |
| Region Code | `ap-southeast-2` |
| S3 Bucket Name | `swapna-weintern-static-website-task2` |
| Index Document | `index.html` |
| Error Document | `error.html` |
| Static Website Hosting | Enabled |
| Public Read Access | Configured through bucket policy |
| CloudFront | Configured (Optional) |
| Default Root Object | `index.html` |
| Viewer Protocol Policy | Redirect HTTP to HTTPS |
| Allowed HTTP Methods | GET, HEAD |
| Price Class | PriceClass_100 |
| Route 53 | Not configured (Optional) |

## 5. Project Structure

```text
task2-Static-Website-Hosting/
│
├── index.html
├── error.html
└── README.md
```

## 6. Implementation Steps Using AWS Management Console

### Step 1: Create an S3 Bucket

1. Sign in to the AWS Management Console.
2. Search for and open Amazon S3.
3. Select the Asia Pacific (Sydney) region.
4. Click **Create bucket**.
5. Enter a globally unique bucket name:

   `swapna-weintern-static-website-task2`

6. Under Block Public Access settings, uncheck **Block all public access** for this practice website.
7. Acknowledge the public access warning.
8. Keep the remaining settings at their defaults.
9. Click **Create bucket**.

### Step 2: Enable Static Website Hosting

1. Open the newly created S3 bucket.
2. Navigate to the **Properties** tab.
3. Scroll down to **Static website hosting**.
4. Click **Edit**.
5. Select **Enable**.
6. Choose **Host a static website**.
7. Configure the following documents:

   - Index document: `index.html`
   - Error document: `error.html`

8. Click **Save changes**.

### Step 3: Upload Website Files

1. Open the bucket's **Objects** tab.
2. Click **Upload**.
3. Select the website files:
   - `index.html`
   - `error.html`
4. Upload any additional CSS, JavaScript, or image files if used.
5. Click **Upload** to complete the process.

### Step 4: Configure Bucket Policy

1. Open the S3 bucket.
2. Navigate to the **Permissions** tab.
3. Scroll down to **Bucket policy**.
4. Click **Edit**.
5. Add the following policy:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "PublicReadGetObject",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::swapna-weintern-static-website-task2/*"
    }
  ]
}
```

6. Click **Save changes**.

This policy grants public read access to the objects stored in the bucket.

### Step 5: Copy the S3 Website Endpoint

1. Open the bucket's **Properties** tab.
2. Scroll down to **Static website hosting**.
3. Copy the **Bucket website endpoint**.

The website endpoint follows this format:

```text
http://bucket-name.s3-website-region.amazonaws.com
```

For this task:

```text
http://swapna-weintern-static-website-task2.s3-website-ap-southeast-2.amazonaws.com
```

### Step 6: Verify the Website

1. Open the S3 website endpoint in a browser.
2. Check whether the main website loads correctly.
3. Verify that the website content and design are displayed.
4. Test the error document if applicable.

The website should be publicly accessible through the S3 website endpoint.

## 7. Optional: Configure CloudFront CDN

CloudFront was also configured to distribute the static website content through AWS edge locations.

### Step 1: Open CloudFront

1. Search for **CloudFront** in the AWS Management Console.
2. Open the CloudFront service.
3. Select **Create distribution**.

### Step 2: Configure the Origin

1. Enter the S3 static website endpoint as the origin domain.
2. Use the website endpoint as a custom origin.
3. Configure the origin protocol policy as **HTTP only**.

### Step 3: Configure Distribution Settings

Configure the following settings:

| Setting | Value |
|---|---|
| Viewer Protocol Policy | Redirect HTTP to HTTPS |
| Allowed HTTP Methods | GET, HEAD |
| Default Root Object | `index.html` |
| Price Class | PriceClass_100 |
| Compression | Enabled |

Keep other settings at their defaults unless required.

### Step 4: Create the Distribution

1. Review the distribution settings.
2. Click **Create distribution**.
3. Wait until the distribution status changes to **Deployed**.

### Step 5: Verify CloudFront

1. Open the CloudFront distribution.
2. Copy its distribution domain name.
3. Open the domain using HTTPS in a browser.
4. Verify that the website loads successfully.

CloudFront provides HTTPS access and distributes website content through its global edge network.

## 8. Optional: Route 53 DNS Configuration

Route 53 can be used to connect a custom domain name to the website.

For this task, Route 53 was not configured because it was optional.

## 9. Verification

The following activities were completed:

- Created an S3 bucket in the Sydney region.
- Enabled public access for the practice website.
- Enabled S3 Static Website Hosting.
- Configured `index.html` as the index document.
- Configured `error.html` as the error document.
- Uploaded website files.
- Configured a bucket policy for public `GetObject` access.
- Tested the website through the S3 website endpoint.
- Created a CloudFront distribution.
- Configured CloudFront to redirect HTTP requests to HTTPS.
- Verified the website through the CloudFront domain.

## 10. Deliverables

| Deliverable | Description |
|---|---|
| Live Website URL | S3 website endpoint |
| S3 Configuration | Screenshot of bucket configuration |
| Bucket Policy | Screenshot of public read policy |
| Live Website | Screenshot of website running in browser |
| CloudFront | Screenshot of distribution configuration |
| Documentation | README.md containing implementation steps |

**Note:** The AWS resources were deleted after capturing the practical screenshots. Therefore, the website is no longer live.

## 11. Screenshots

Add the following screenshots as evidence of task completion:

1. S3 bucket created successfully.
2. Website files uploaded to the bucket.
3. Static Website Hosting enabled.
4. Index and error document configuration.
5. Bucket policy configured for public read access.
6. S3 website running successfully in the browser.
7. CloudFront distribution configuration.
8. CloudFront distribution status as Deployed.
9. Website running through the CloudFront domain.

## 12. Resource Cleanup

After completing the task and capturing screenshots, AWS resources were deleted to avoid ongoing charges.

### S3 Cleanup

1. Open Amazon S3.
2. Select the website bucket.
3. Delete all objects inside the bucket.
4. Select the bucket and click **Delete**.
5. Confirm the bucket deletion.

### CloudFront Cleanup

1. Open Amazon CloudFront.
2. Select the distribution.
3. Disable the distribution.
4. Wait until its status becomes **Disabled**.
5. Select the distribution and click **Delete**.
6. Confirm deletion.

**Note:** CloudFront distributions must be disabled before deletion. Charges incurred before resource deletion may still appear on the AWS bill.

## 13. Evaluation Criteria

| Evaluation Criteria | Implementation |
|---|---|
| Successful static site deployment | Website hosted using Amazon S3 |
| Website accessibility | Verified using S3 website endpoint |
| Correct bucket policy | Public `s3:GetObject` policy configured |
| Index and error documents | `index.html` and `error.html` configured |
| CloudFront configuration | Distribution created and tested |
| Documentation quality | Implementation steps and screenshots documented |

## 14. Conclusion

In this task, I successfully deployed a static website using Amazon S3 Static Website Hosting and configured a bucket policy to allow public read access.

I also created an optional Amazon CloudFront distribution to deliver website content through AWS edge locations and provide HTTPS access.

Through this practical, I gained hands-on experience with S3 bucket creation, static website hosting, website file uploads, bucket policies, CloudFront configuration, website verification, and AWS resource cleanup.

This task helped me understand the fundamentals of hosting and delivering static websites using AWS cloud services.
