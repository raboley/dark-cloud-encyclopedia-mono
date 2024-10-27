variable "ssh_key_name" {default = "YOUR_KEY_NAME_HERE"}
variable "aws_region_name" { default = "us-west-2" }

variable "aws_access_key" {}
variable "aws_secret_key" {}
variable "private_key_path" {}

variable "output_facts" {
  default = "inventory"
}

provider "aws" {
  # Use keys in home dir.
  access_key = "${var.aws_access_key}"
  secret_key = "${var.aws_secret_key}"
  region = "${var.aws_region_name}"
}

terraform {
  backend "s3" {
    # Defined in the backend.config file since you can't use variable interpolation for backends.
  }
}

data "external" "myipaddr" {
  # Pick one or the other. The second one requires an external script but uses DNS instead of https.
  #program = ["bash", "-c", "curl -s 'https://api.ipify.org?format=json'"]
  program = ["bash", "${path.module}/myipaddr.sh"]
}

data "aws_ami" "ubuntu" {
  most_recent = true

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-xenial-16.04-amd64-server-*"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }

  owners = ["099720109477"] # Canonical
}

# Request a spot instance at $0.01
# Master Node
resource "aws_instance" "k8s-master" {
  count         = "1"
  ami           = "${data.aws_ami.ubuntu.id}"
  instance_type = "t2.medium"
  #wait_for_fulfillment = true
  #spot_type     = "one-time"
  #spot_price    = "0.015"

  vpc_security_group_ids = ["${aws_security_group.k8s_sg.id}"]

  key_name = "${var.ssh_key_name}"

  tags {
    Name   = "k8s-master"
    App    = "k8s"
    k8srole = "master"
  }
  
  connection {
    user        = "ubuntu"
    private_key = "${file(var.private_key_path)}"
  }
  provisioner "remote-exec" {
    script = "setup.sh"
  }
}

# Worker Nodes
#resource "aws_xzcv_spot_instance_request" "k8s-worker" {
resource "aws_instance" "k8s-worker" {
  count         = "2"
  ami           = "${data.aws_ami.ubuntu.id}"
  instance_type = "t2.medium"
  #wait_for_fulfillment = true
  #spot_type     = "one-time"
  #spot_price    = "0.015"

  vpc_security_group_ids = ["${aws_security_group.k8s_sg.id}"]

  key_name = "${var.ssh_key_name}"

  tags {
    Name   = "k8s-worker"
    App    = "k8s"
    k8srole = "worker"
  }
  
  connection {
    user        = "ubuntu"
    private_key = "${file(var.private_key_path)}"
  }

  provisioner "remote-exec" {
    script = "setup.sh"
  }
}

resource "aws_security_group" "k8s_sg" {

}
resource "aws_security_group_rule" "allow_ssh_from_anywhere" {
  type        = "ingress"  
  from_port   = 22
  to_port     = 22
  protocol    = "tcp"
  cidr_blocks = ["0.0.0.0/0"]
  description = "inbound SSH traffic from ANY"
  security_group_id = "${aws_security_group.k8s_sg.id}"
}
resource "aws_security_group_rule" "allow_all_egress" {
  type            = "egress"
  from_port       = 0
  to_port         = 0
  protocol        = "all"
  cidr_blocks     = ["0.0.0.0/0"]
  description     = "Outbound access to ANY"

  security_group_id = "${aws_security_group.k8s_sg.id}"
}


resource "aws_security_group_rule" "allow_all_myip" {
  type            = "ingress"
  from_port       = 0
  to_port         = 0
  protocol        = "all"
  cidr_blocks     = ["${data.external.myipaddr.result["ip"]}/32"]
  description     = "Management Ports for K8s Cluster"

  security_group_id = "${aws_security_group.k8s_sg.id}"
}

resource "aws_security_group_rule" "allow_all_ip" {
  type            = "ingress"
  from_port       = 0
  to_port         = 0
  protocol        = "all"
  cidr_blocks     = ["0.0.0.0/0"]
  description     = "Management Ports for K8s Cluster - all"

  security_group_id = "${aws_security_group.k8s_sg.id}"
}

resource "aws_security_group_rule" "allow_SG_any" {
  type            = "ingress"
  from_port       = 0
  to_port         = 0
  protocol        = "all"
  self            = true
  description     = "Any from SG for K8s Cluster"

  security_group_id = "${aws_security_group.k8s_sg.id}"
}

output "master_ip" {
  value = "${aws_instance.k8s-master.public_ip}"
}
output "worker_ips" {
  value = "${aws_instance.k8s-worker.*.public_ip}"
}

resource "aws_s3_bucket_object" "object" {
  bucket = "dark-cloud-bucket-terraform-prod"
  key    = "${var.output_facts}"
  content = <<EOF

[master]
master1 ansible_ssh_host=${aws_instance.k8s-master.public_ip}

[worker]
${aws_instance.k8s-worker.*.public_ip[0]}
${aws_instance.k8s-worker.*.public_ip[1]}


[master:vars]
ansible_ssh_common_args='-o StrictHostKeyChecking=no'

[worker:vars]
ansible_ssh_common_args='-o StrictHostKeyChecking=no'
EOF
}
