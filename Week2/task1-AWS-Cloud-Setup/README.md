# WeIntern Cloud Computing Internship – Task 1

## AWS EC2 Instance Setup, Nginx Deployment, and AMI Creation

## 1. Objective

The objective of this task is to gain hands-on experience with Amazon Web Services (AWS) EC2 by launching and configuring a virtual machine.

This project demonstrates how to:
- Launch an EC2 instance.
- Configure security groups.
- Connect to an EC2 instance using SSH.
- Install and configure an Nginx web server.
- Deploy a basic web application.
- Verify web server accessibility using a public IP address.
- Create an Amazon Machine Image (AMI) as a backup of the configured instance.

## 2. Technologies Used

| Component | Technology |
|---|---|
| Cloud Provider | Amazon Web Services (AWS) |
| Cloud Service | Amazon EC2 |
| Operating System | Amazon Linux |
| Web Server | Nginx |
| Remote Connection | SSH |
| Client Operating System | Ubuntu 22.04 |
| Backup | Amazon Machine Image (AMI) |

## 3. AWS EC2 Instance Configuration

An EC2 instance was launched using the AWS Management Console.

**Configuration:**
- Instance type: t2.micro (if used)
- Operating system: Amazon Linux
- Key pair: weintern-key-swapna.pem
- Web server: Nginx

The instance was launched successfully and its status was verified in the EC2 console.

## 4. Security Group Configuration

A security group was configured to allow the required inbound traffic.

| Type | Protocol | Port | Source |
|---|---|---|---|
| SSH | TCP | 22 | My IP |
| HTTP | TCP | 80 | 0.0.0.0/0 |

**Purpose:**
- SSH (Port 22): Allows secure remote access to the EC2 instance.
- HTTP (Port 80): Allows users to access the hosted website through a browser.

SSH access was restricted to the administrator's IP address.

## 5. Connect to EC2 Using SSH

The EC2 instance was accessed from an Ubuntu terminal using the downloaded private key.

First, navigate to the directory containing the key:

```bash
cd ~/Downloads
```

Set secure permissions for the private key:

```bash
chmod 400 weintern-key-swapna.pem
```

Connect to the EC2 instance:

```bash
ssh -i "weintern-key-swapna.pem" ec2-user@YOUR_PUBLIC_IP
```

Replace `YOUR_PUBLIC_IP` with the actual public IPv4 address of the EC2 instance.

The SSH connection was established successfully.

**Note:** The `ec2-user` account is commonly used for Amazon Linux instances.

## 6. Update Amazon Linux Packages

The operating system package manager was used to update the system.

For Amazon Linux 2023:

``bash
sudo dnf update -y
```



To identify the Amazon Linux version:

```bash
cat /etc/os-release
```

**Note:** Ubuntu uses `apt`, whereas Amazon Linux uses `dnf` or `yum`.

## 7. Install Nginx Web Server

Nginx was installed on the EC2 instance.

For Amazon Linux 2023:

```bash
sudo dnf install nginx -y
```


Start the Nginx service:

```bash
sudo systemctl start nginx
```

Enable Nginx to start automatically after reboot:

```bash
sudo systemctl enable nginx
```

Check the Nginx service status:

```bash
sudo systemctl status nginx
```

Expected status:

```text
Active: active (running)
```

## 8. Deploy a Custom Webpage

The default Nginx webpage was modified to display a custom welcome message.

Open the default HTML file:

```bash
sudo nano /usr/share/nginx/html/index.html
```

Replace the existing content with:

```html
<!DOCTYPE html>
<html>
<head>
    <title>My AWS EC2 Website</title>
</head>
<body>
    <h1>Welcome to My AWS EC2 Web Server!</h1>

    <h2>WeIntern Cloud Computing Internship</h2>

    <p>Successfully deployed using Amazon Linux and Nginx.</p>

    <p>EC2 Instance is running successfully.</p>
</body>
</html>
```

Save the file and restart Nginx:

```bash
sudo systemctl restart nginx
```

## 9. Verify Web Server Using Public IP

The EC2 instance's Public IPv4 address was obtained from:

**AWS Console → EC2 → Instances → Select Instance → Details**

Open the following address in a web browser:

```text
http://YOUR_PUBLIC_IP
```

The custom Nginx webpage should appear in the browser.

This confirms that:
- The EC2 instance is accessible.
- Nginx is running successfully.
- HTTP traffic is allowed through the security group.
- The website is publicly accessible.

## 10. Create an Amazon Machine Image (AMI)

An Amazon Machine Image (AMI) was created from the configured EC2 instance.

An AMI contains the information required to launch another EC2 instance with the captured configuration.

**Steps:**

1. Open AWS EC2 Console.
2. Navigate to Instances.
3. Select the configured EC2 instance.
4. Click Actions.
5. Select Image and templates.
6. Click Create image.
7. Enter the following details:

| Field | Value |
|---|---|
| Image Name | WeIntern-Task1-Nginx-AMI |
| Description | AMI backup of EC2 with Nginx configured |
| No Reboot | Unchecked |

8. Click Create image.
9. Navigate to EC2 → Images → AMIs.
10. Wait until the AMI status changes to `Available`.

**Result:** The AMI was created to preserve the configured EC2 environment for future use.

AWS automatically creates backing EBS snapshots for the volumes included in the AMI.

## 11. Screenshots and Evidence

The following screenshots should be included as proof of implementation.

| Screenshot | Description |
|---|---|
| 1 | EC2 instance running in AWS Console |
| 2 | Security group inbound rules |
| 3 | Successful SSH connection |
| 4 | Nginx installation and service status |
| 5 | Custom webpage displayed in browser |
| 6 | AMI creation confirmation |
| 7 | AMI status showing Available |

Create a folder named `screenshots` in the project directory and save the screenshots there.

## 12. AWS Resource Cleanup

After completing the task and saving all required screenshots, AWS resources can be cleaned up if they are no longer needed.

Important considerations:

- Terminating an EC2 instance stops its compute charges.
- EBS volumes may remain if configured not to delete on termination.
- AMIs and their associated EBS snapshots may continue to incur storage charges.
- Public IPv4 addresses may also incur charges.

If the AMI is no longer required, deregister it and delete its associated snapshots after verifying that they are not needed elsewhere.

## 13. Project Structure

```text
WeIntern-Task1/
│
├── README.md
│
├── screenshots/
│   ├── 01-ec2-instance.png
│   ├── 02-security-group.png
│   ├── 03-ssh-connection.png
│   ├── 04-nginx-status.png
│   ├── 05-custom-webpage.png
│   ├── 06-ami-creation.png
│   └── 07-ami-available.png
│
└── Documentation/
    └── Task1-Documentation.docx
```

## 14. Conclusion

Successfully completed the basic AWS EC2 deployment workflow.

The task provided practical experience in launching cloud infrastructure, configuring network security, connecting to a Linux server using SSH, installing and configuring Nginx, deploying a custom webpage, verifying public accessibility, and creating an AMI.

This project demonstrates the fundamentals of cloud computing and AWS EC2 instance management.

---

**Internship:** WeIntern Pvt. Ltd.  
**Domain:** Cloud Computing / DevOps  
**Task:** Week 2 – Task 1  
**Cloud Platform:** Amazon Web Services (AWS)
