# SimpleTimeService

This repository contains a tiny FastAPI microservice that returns the current UTC timestamp and requester IP, a Dockerfile configured to run the app as a non-root user, Terraform configuration to deploy it to AWS ECS Fargate behind an Application Load Balancer, and a GitHub Actions workflow to build/push the image and apply the Terraform.

## Quick local run

1. Build:

```bash
cd app
docker build -t simple-time-service .

2. Run:

```bash
docker run -p 8000:8000 simple-time-service
# visit http://localhost:8000/


CI/CD

The GitHub Actions workflow builds and pushes the Docker image to DockerHub and runs Terraform to create/update the AWS infrastructure. Make sure you add the required GitHub repository secrets:

DOCKERHUB_USERNAME

DOCKERHUB_TOKEN

AWS_ACCESS_KEY_ID

AWS_SECRET_ACCESS_KEY

AWS_REGION (e.g., ap-northeast-2)

Terraform

Edit terraform/terraform.tfvars to set container_image if you want to use a pre-built image. The workflow will override container_image with the DockerHub image it pushes.

Security

Do not commit credentials or secrets into the repo.

The Dockerfile runs the app as a non-root user.
