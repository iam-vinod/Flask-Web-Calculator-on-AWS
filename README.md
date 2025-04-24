# Flask-Web-Calculator-on-AWS

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
These instructions will get your project up and running locally and in production using Docker and Terraform.

📦 Prerequisites
Python 3.x
Docker
Terraform
AWS CLI

⚙️ Installation & Local Setup

1.Clone the repository

git clone <your-repo-url>

cd <your-repo-folder>

2.Install dependencies

pip install -r requirements.txt

3. Run the application locally

  python app/app.py

4. Open in browser Visit http://localhost:5000 (or the port your app is set to use).

🐳 Docker Usage

1. Build the Docker image

docker build -t my-python-app .

2. Run the container with port forwarding (host: 8080 → container: 5000)

docker run -p 8080:5000 my-python-app

3. Access the app in your browser

http://localhost:8080

☁️ Deploy with Terraform

1. Navigate to the Terraform directory

cd terraform

2. Initialize Terraform

terraform init

3.Plan the infrastructure

terraform plan

4. Apply the configuration

terraform apply

🔄 CI/CD Pipeline

A GitHub Actions workflow is configured at .github/workflows/ci-cd.yml

Automatically triggers builds, tests, and deployments on push to main.



