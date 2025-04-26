Flask Web Calculator on AWS
A simple, lightweight Flask-based calculator application deployed on AWS EC2 using Docker and Terraform.
This project demonstrates containerization, Infrastructure as Code (IaC), and basic CI/CD automation via GitHub Actions.

📁 Project Structure

.
├── .github/
│   └── workflows/
│       └── ci-cd.yml
├── app/
│   ├── app.py
│   └── templates/
│       └── index.html
├── terraform/
│   ├── main.tf
│   ├── outputs.tf
│   └── variables.tf
├── Dockerfile
├── requirements.txt
└── README.md


🚀 Getting Started
These instructions will help you run the project locally and in production.

📦 Prerequisites
Python 3.x

Docker

Terraform

AWS CLI

⚙️ Local Setup
Clone the repository


git clone https://github.com/iam-vinod/Flask-Web-Calculator-on-AWS.git

cd Flask-Web-Calculator-on-AWS

Install dependencies


pip install -r requirements.txt

Run the application locally

python app/app.py

Open the app in your browser

Visit: http://localhost:5000

🐳 Docker Usage
Build the Docker image

docker build -t my-python-app .

Run the container

docker run -p 8080:5000 my-python-app

Access the application

Visit: http://localhost:8080

☁️ Deploy on AWS with Terraform
Navigate to the Terraform directory

cd terraform

Initialize Terraform

terraform init

Plan the infrastructure

terraform plan

Apply the configuration

terraform apply

Access the deployed applications:

API Calculator (port 5000): http://your-ec2-public-ip:5000

Web GUI Calculator (port 8080): http://your-ec2-public-ip:8080

🔄 CI/CD Pipeline
A GitHub Actions workflow is configured at:

.github/workflows/ci-cd.yml
On every push to the main branch:

Build Docker images

Push to Docker Hub (or your private registry)

Deploy updated containers to AWS EC2

✅ Fully automated deployment pipeline!

🎯 Summary:
API runs on port 5000

Web GUI runs on port 8080

Fully Dockerized + Terraform Automated + GitHub Actions CI/CD ✅
