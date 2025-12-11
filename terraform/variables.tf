variable "region" {
  description = "AWS region"
  type        = string
  default     = "ap-northeast-2" # Seoul
}

variable "container_image" {
  description = "Container image (repo:tag) to run in ECS"
  type        = string
}
