# WeIntern Internship — Task 3
## Deploy a Static Website Using Amazon S3 and Amazon CloudFront

**Author:** Swapna Adhav  
**Project:** WeIntern Internship  
**Task:** Task 3 — Deploy a Static Site via S3 / GCS  
**Cloud Provider:** Amazon Web Services (AWS)  
**Region:** Asia Pacific (Sydney) — `ap-southeast-2`  
**Status:** Successfully deployed and verified

---

## 1. Project Overview

The objective of this project is to deploy a static website using Amazon Simple Storage Service (Amazon S3) and Amazon CloudFront.

The HTML website is stored in an S3 bucket. CloudFront distributes the website to visitors over HTTPS. The S3 bucket remains private, and CloudFront uses Origin Access Control (OAC) to access the website files.

### Live Website

**Website URL:** https://dwpuiw40xj1jx.cloudfront.net/

**GitHub Repository:** https://github.com/adhavswapna/Weintern-Internship

## 2. Objectives

- Create an Amazon S3 bucket.
- Configure the AWS region and resource tags.
- Keep the S3 bucket private by blocking public access.
- Upload the static website's `index.html` file.
- Configure CloudFront to distribute the website.
- Use Origin Access Control (OAC) to protect the S3 origin.
- Configure a bucket policy to allow CloudFront to read website files.
- Redirect HTTP requests to HTTPS.
- Verify the deployment and document the results.

## 3. Technologies Used

- **Amazon S3:** Stores the static website files.
- **Amazon CloudFront:** Distributes the website to visitors.
- **Origin Access Control (OAC):** Allows CloudFront to access the private S3 origin.
- **AWS CLI:** Creates and manages AWS resources from the terminal.
- **HTML and CSS:** Build and style the website.
- **Git and GitHub:** Version control and project documentation.
- **Python 3:** Basic HTML and JSON validation.

## 4. AWS Resource Details

| Resource | Configuration |
|---|---|
| AWS Region | `ap-southeast-2` |
| S3 Bucket | `weintern-task3-s3-swapnaadhav` |
| CloudFront Distribution ID | `EAGMUDC8KCZVQ` |
| CloudFront Domain | `dwpuiw40xj1jx.cloudfront.net` |
| Origin Access Control ID | `E2M1DLNO7XA6O4` |
| Default Root Object | `index.html` |
| Viewer Protocol Policy | Redirect HTTP to HTTPS |
| Allowed HTTP Methods | GET, HEAD |
| CloudFront Price Class | `PriceClass_100` |
| Object Encryption Observed | AES256 |

## 5. Architecture

```text
                 Website Visitor
                        |
                        | HTTPS
                        v
                Amazon CloudFront
                Distribution
                EAGMUDC8KCZVQ
                        |
                        | Secure origin access
                        | through OAC
                        v
                 Amazon S3 Bucket
       weintern-task3-s3-swapnaadhav
                        |
                        v
                    index.html
```

### How It Works

1. A visitor opens the CloudFront website URL.
2. CloudFront receives the HTTPS request.
3. CloudFront retrieves the requested file from the S3 bucket using OAC.
4. The S3 bucket policy authorizes read access for the specified CloudFront distribution.
5. CloudFront returns the website content to the visitor.

The S3 bucket is not configured for public access.

## 6. Prerequisites

Before starting, ensure you have:

- An AWS account.
- AWS CLI installed.
- AWS CLI configured with suitable permissions.
- Python 3 installed.
- A GitHub account.
- A local project directory containing `index.html`.

Verify your AWS CLI installation:

```bash
aws --version
```

Check the active AWS identity:

```bash
aws sts get-caller-identity
```

Check the configured AWS region:

```bash
aws configure get region
```

The configured region for this project is:

```text
ap-southeast-2
```

## 7. Step-by-Step Implementation

### Step 1: Configure Environment Variables

Set the variables used by the AWS CLI commands.

```bash
export AWS_REGION="ap-southeast-2"
export BUCKET_NAME="weintern-task3-s3-swapnaadhav"
export PROJECT="WeIntern-Internship"
export TASK="Task3"
export ENVIRONMENT="Learning"
export OWNER="SwapnaAdhav"
```

Verify the variables:

```bash
echo "$AWS_REGION"
echo "$BUCKET_NAME"
```

### Step 2: Create the S3 Bucket

Create the S3 bucket in the Sydney region.

```bash
aws s3api create-bucket \
  --bucket "$BUCKET_NAME" \
  --region "$AWS_REGION" \
  --create-bucket-configuration LocationConstraint="$AWS_REGION"
```

**Result:** The bucket `weintern-task3-s3-swapnaadhav` was created.

### Step 3: Block Public Access

Configure all four S3 Block Public Access settings.

```bash
aws s3api put-public-access-block \
  --bucket "$BUCKET_NAME" \
  --region "$AWS_REGION" \
  --public-access-block-configuration \
  'BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=true,RestrictPublicBuckets=true'
```

Verify the settings:

```bash
aws s3api get-public-access-block \
  --bucket "$BUCKET_NAME" \
  --region "$AWS_REGION"
```

**Verified result:** All four settings returned `true`.

This configuration helps prevent accidental public access to the bucket.

### Step 4: Add Bucket Tags

Apply tags to identify the project and its owner.

```bash
aws s3api put-bucket-tagging \
  --bucket "$BUCKET_NAME" \
  --region "$AWS_REGION" \
  --tagging 'TagSet=[
    {Key=Project,Value=WeIntern-Internship},
    {Key=Task,Value=Task3},
    {Key=Environment,Value=Learning},
    {Key=Owner,Value=SwapnaAdhav}
  ]'
```

Verify the tags:

```bash
aws s3api get-bucket-tagging \
  --bucket "$BUCKET_NAME" \
  --region "$AWS_REGION"
```

### Step 5: Upload the Website

Navigate to the project directory.

```bash
cd ~/weintern-cloud-internship/task3-static-website
```

Upload `index.html` to S3.

```bash
aws s3 cp index.html \
  "s3://$BUCKET_NAME/index.html" \
  --region "$AWS_REGION" \
  --content-type "text/html"
```

Verify the uploaded object:

```bash
aws s3api head-object \
  --bucket "$BUCKET_NAME" \
  --key index.html \
  --region "$AWS_REGION"
```

**Verified results:**

- Content type: `text/html`
- Server-side encryption: `AES256`
- Object key: `index.html`

### Step 6: Configure CloudFront Origin Access Control

An Origin Access Control was created to let CloudFront access the private S3 origin.

**OAC ID:** `E2M1DLNO7XA6O4`

The S3 origin used by the distribution is:

```text
weintern-task3-s3-swapnaadhav.s3.ap-southeast-2.amazonaws.com
```

OAC provides authenticated origin access without making the bucket public.

### Step 7: Create the CloudFront Distribution

The CloudFront distribution was configured with the following settings:

- Default root object: `index.html`
- Viewer protocol policy: `redirect-to-https`
- Allowed methods: `GET` and `HEAD`
- Compression: enabled
- Price class: `PriceClass_100`
- CloudFront default certificate: enabled
- HTTP/2: enabled
- IPv6: enabled
- Origin: the S3 bucket's REST endpoint
- Origin access: OAC

The distribution was created successfully.

**Distribution ID:**

```text
EAGMUDC8KCZVQ
```

**Distribution ARN:**

```text
arn:aws:cloudfront::230623977579:distribution/EAGMUDC8KCZVQ
```

**CloudFront Domain:**

```text
dwpuiw40xj1jx.cloudfront.net
```

### Step 8: Configure the S3 Bucket Policy

The bucket policy allows CloudFront to read objects from the bucket.

The policy uses the CloudFront service principal and restricts access to the specific distribution ARN.

The key permissions are:

- Principal: `cloudfront.amazonaws.com`
- Action: `s3:GetObject`
- Resource: `arn:aws:s3:::weintern-task3-s3-swapnaadhav/*`
- Condition: the request must originate from the specified CloudFront distribution.

Validate the JSON file:

```bash
python3 -m json.tool bucket-policy.json
```

**Security note:** Keep all four S3 Block Public Access settings enabled. Do not make the bucket public as a workaround for access errors.

### Step 9: Verify CloudFront Deployment

Check the distribution status:

```bash
aws cloudfront get-distribution \
  --id EAGMUDC8KCZVQ \
  --query 'Distribution.Status' \
  --output text
```

**Verified result:**

```text
Deployed
```

### Step 10: Upload Website Updates

Whenever you modify `index.html`, upload it again:

```bash
aws s3 cp index.html \
  s3://weintern-task3-s3-swapnaadhav/index.html \
  --region ap-southeast-2 \
  --content-type "text/html"
```

### Step 11: Invalidate the CloudFront Cache

Request an invalidation so CloudFront refreshes cached website content.

```bash
aws cloudfront create-invalidation \
  --distribution-id EAGMUDC8KCZVQ \
  --paths "/*"
```

The recorded invalidation requests initially returned `InProgress`.

To check the final status, use the invalidation ID returned by the command:

```bash
aws cloudfront get-invalidation \
  --distribution-id EAGMUDC8KCZVQ \
  --id YOUR_INVALIDATION_ID \
  --query 'Invalidation.Status' \
  --output text
```

Replace `YOUR_INVALIDATION_ID` with the actual ID.

### Step 12: Verify the Website URL

Retrieve the CloudFront domain:

```bash
aws cloudfront get-distribution \
  --id EAGMUDC8KCZVQ \
  --query 'Distribution.DomainName' \
  --output text
```

Check the website response:

```bash
curl -I https://dwpuiw40xj1jx.cloudfront.net/
```

**Verified result:** The endpoint returned `HTTP/2 200`.

Open the website:

https://dwpuiw40xj1jx.cloudfront.net/

### Step 13: Validate the HTML File

A basic HTML parser check can be performed using Python:

```bash
python3 - <<'PY'
from html.parser import HTMLParser
from pathlib import Path

class Validator(HTMLParser):
    pass

html = Path("index.html").read_text(encoding="utf-8")
Validator().feed(html)
print("HTML parser completed without a syntax error.")
PY
```

This checks whether Python's HTML parser can process the file. It is not a complete accessibility or browser-compatibility test.

## 8. Validation Results

| Validation | Result |
|---|---|
| AWS identity | Verified |
| AWS region | `ap-southeast-2` |
| S3 public access block | All four settings enabled |
| S3 bucket tags | Verified |
| Website uploaded | Verified |
| Content type | `text/html` |
| Server-side encryption | `AES256` |
| CloudFront status | `Deployed` |
| HTTPS response | `HTTP/2 200` observed |
| CloudFront invalidation | Requested; initially `InProgress` |

## 9. GitHub Repository Setup

The project repository is:

https://github.com/adhavswapna/Weintern-Internship

Navigate to the project directory:

```bash
cd ~/weintern-cloud-internship/task3-static-website
```

Check Git status:

```bash
git status
```

Check the configured remote:

```bash
git remote -v
```

If `origin` already exists but points to the wrong repository, update it:

```bash
git remote set-url origin \
  https://github.com/adhavswapna/Weintern-Internship.git
```

If no `origin` remote exists, add it:

```bash
git remote add origin \
  https://github.com/adhavswapna/Weintern-Internship.git
```

Create a `.gitignore` file:

```bash
cat > .gitignore <<'EOF'
.env
.env.*
*.pem
.DS_Store
EOF
```

Review the files before committing:

```bash
git status
```

Stage the website and documentation:

```bash
git add index.html README.md .gitignore
```

Commit:

```bash
git commit -m "Document AWS static website deployment"
```

Push to GitHub:

```bash
git push -u origin main
```

### GitHub Authentication

GitHub does not accept a normal account password for HTTPS Git operations.

Use one of these methods:

- Git Credential Manager or browser authentication.
- A fine-grained Personal Access Token with access to the correct repository and `Contents: Read and write`.
- SSH authentication using an SSH key registered with GitHub.

Never share your token or commit it to the repository.

If GitHub rejects the push because the remote already contains commits, inspect the repository history and reconcile it before pushing. Do not force-push automatically.

## 10. Security Considerations

- S3 Block Public Access remains enabled.
- CloudFront accesses the origin through OAC.
- The bucket policy restricts object reads to the intended distribution.
- Viewer requests are redirected to HTTPS.
- The uploaded object was observed to use AES256 server-side encryption.
- AWS credentials and GitHub tokens must never be committed.
- Consider enabling S3 versioning if recovery of older files is required.
- Review AWS costs before leaving cloud resources running.

## 11. Troubleshooting

### Error: 403 Forbidden

Check that:

- CloudFront is deployed.
- OAC is attached to the correct S3 origin.
- The bucket policy contains the correct distribution ARN.
- `index.html` exists in S3.
- The CloudFront distribution is configured for the correct origin.

Do not make the bucket public to resolve this error.

### Error: 404 Not Found

Check that:

- The uploaded object key is `index.html`.
- The default root object is `index.html`.
- The CloudFront origin points to the correct bucket.

### Website Updates Are Not Visible

Upload the updated file, create a CloudFront invalidation, and wait for it to complete.

### GitHub Authentication Failed

Do not use the normal GitHub account password. Check the token's expiration, repository access, and `Contents: Read and write` permission.

## 12. Optional Cleanup

**Warning:** The following commands delete the S3 website files and bucket. Only run them if you no longer need the deployment.

```bash
aws s3 rm s3://weintern-task3-s3-swapnaadhav \
  --recursive \
  --region ap-southeast-2
```

Then delete the bucket:

```bash
aws s3api delete-bucket \
  --bucket weintern-task3-s3-swapnaadhav \
  --region ap-southeast-2
```

CloudFront must be disabled and the configuration update fully deployed before the distribution can be deleted. Follow the current AWS CLI procedure for CloudFront deletion.

## 13. Conclusion

The static website was uploaded to Amazon S3 and distributed through Amazon CloudFront over HTTPS.

S3 public access blocking remained enabled, and CloudFront OAC together with a scoped bucket policy provided controlled access to the private S3 origin.

The CloudFront distribution reached `Deployed` status, and the live HTTPS endpoint returned `HTTP/2 200`.

**Live Website:** https://dwpuiw40xj1jx.cloudfront.net/

**GitHub Repository:** https://github.com/adhavswapna/Weintern-Internship
