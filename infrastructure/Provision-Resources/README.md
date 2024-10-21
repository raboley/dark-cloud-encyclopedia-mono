# How to use terraform to spin up three ubuntu nodes using spot instances

This repo will spin up 3 instances of ec2s that will be ready to house a kubernetes cluster. For kubeadm and kubernetes to run it is required that they have at least 2 virtual processors, and 2 GB ram, so this demo is **outside the realm of the free tier** due to the base hardware requirements. You can request spot instances (commented out code) which are very cheap, but you can only have 10 spot requests active at time, so if you are spinning up and down these instances very quickly you will hit the limit since it takes a while for instances that are destroy to have their request removed.

## Download and Install Terraform

https://www.terraform.io/downloads.html

## Edit the k8s.tf file

1. Change "YOUR_KEY_NAME_HERE" to your ssh keyname (assumes it's already uploaded in the amazon ec2 key store)
2. Update the AWS region as desired (make sure your ssh key is in this region)
3. Add your AWS "access key" and "aws_secret_key" terraform.tfvars (NOT RECOMENDED).
Terraform will use ~/.aws/credentials if not specified in the .tf file. (RECOMENDED)
4. Add the path and name of the private key file to ssh into the machines (to run the provisioner for executing remote commands)

## Bootstrap terraform

1. Run `make init`
2. Run `make plan`
3. Run `make apply`

After that it will take a little time, but 3 instances in their own subnet and availabilty zones will be spun up!

### Basic troubleshooting

If you don't have make installed or supported, you can just run the raw commands in the make file. If your IP Address changes, and you lose access to ssh into your hosts, just run `make apply` again and the security group will be updated with your new IP Address.

If you don't know how to create and upload a key pair to aws, see here.
https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html

## To tear down all the created resources

1. Run `terraform destroy`

That will delete everything in aws. Make sure to do that so you don't get charged.

## CICD

The CICD Pipeline is run through azure devops and triggers whenever this repo commits to master.

The full pipeline uses a couple different repos to perform each step identified by the ().

1. Create 3 Ec2 instances in AWS (Provision-Resources)
1. Install kubernetes on the 3 nodes and setup networking (Create-k8-Cluster)
1. Deploy the dark-cloud-encyclopedia website pod to the cluster (Ansible-Pipeline)
