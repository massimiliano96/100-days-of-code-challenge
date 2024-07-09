resource "aws_security_group" "example" {
  name        = "example"
  description = "Example security group"
  vpc_id      = "vpc-123456"

  tags = {
    name = "custom-tag-for-security-group"
  }
}