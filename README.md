# aws-3-tier-webapp
Hands-on project to deploy a scalable 3-tier web app architecture on AWS with EC2, Load Balancer, and RDS

# AWS 3-Tier Web Application Deployment

## 🚀 Project Overview
This project demonstrates the deployment of a scalable 3-tier web application on AWS using core cloud services. The architecture includes:

- **Presentation Layer**: Web server hosted on EC2
- **Application Layer**: Backend logic on EC2 behind an Application Load Balancer (ALB)
- **Database Layer**: Amazon RDS (MySQL)

## 🧰 Tech Stack
- Frontend: HTML/CSS (static website)
- Backend: Python (Flask)
- Database: MySQL (AWS RDS)

## 🛠 AWS Services Used
- EC2
- ALB
- Auto Scaling Group (ASG)
- RDS
- S3 (optional for static assets)
- IAM
- VPC/Subnets/Security Groups

## 🎯 Goals
- Hands-on experience with AWS architecture
- Demonstrate full-stack deployment with high availability
- Learn networking and security setup in AWS

## 📁 Project Structure
To be updated as development progresses.

## 📝 Status
🟢 Deployment successfull
 - AWS 3-Tier Web App - Terminal Operations Log
Date: 2025-05-13
EC2 Setup
---------
- Launched Amazon Linux EC2
- Installed Python3, Flask, mysql-connector-python
- Transferred backend.py and index.html
- Flask bound to 0.0.0.0, ran on port 5000
Security Groups
---------------
- Allowed inbound on port 5000 (HTTP) and 22 (SSH)
- Verified frontend fetch using EC2 public IP
RDS MySQL Setup
---------------
- Created MySQL 8.0 instance in RDS
- Allowed inbound traffic from EC2 SG
- Created database `webapp` and table `messages`
- Inserted data successfully
Error Fixes
-----------
- Access Denied: Fixed credentials
- Column not found: Fixed table schema
- Null data: Fixed insert
- HTTP 500/Timeouts: Fixed Flask binding and SG rules
Final Check
-----------
- Backend returns correct JSON
- Frontend fetches and shows message
- End-to-end flow working
