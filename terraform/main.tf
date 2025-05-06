provider "aws" { region = "us-east-1"
}
resource "aws_instance" "app" { ami = 
  "ami-0c02fb55956c7d316" # Ubuntu 
  22.04 in us-east-1 instance_type = 
  "t3.micro" key_name = var.key_name 
  user_data = file("setup.sh") tags = {
    Name = "microservice"
  }
}
