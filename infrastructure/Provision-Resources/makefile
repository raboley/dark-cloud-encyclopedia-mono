init:
	terraform init -backend-config=backend.config
plan:
	terraform plan -var-file='terraform.tfvars'
apply:
	terraform apply -var-file='terraform.tfvars' -auto-approve
destroy:
	terraform destroy -force