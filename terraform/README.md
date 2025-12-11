# Terraform for SimpleTimeService

## Requirements
- terraform >= 1.6
- AWS credentials configured (e.g., AWS CLI or env vars)
- Docker image available in a registry (container_image variable)

## Deploy

1. Edit variables :

   Edit terraform/terraform.tfvars to set container_image and region

2. Initialize and apply:

   terraform init
   terraform plan
   terraform apply

3. On success the ALB DNS will be output. Visit http://<alb_dns>/ to see the service.

## Notes
- This example uses ECS Fargate and the terraform-aws-modules/vpc module.
- Do not commit AWS credentials or terraform.tfvars containing secrets.
