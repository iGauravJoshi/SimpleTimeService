output "alb_dns" {
  description = "Public DNS name of the ALB"
  value       = aws_lb.app_lb.dns_name
}
