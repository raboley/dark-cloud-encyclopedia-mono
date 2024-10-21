run:
	ansible-playbook -i inventory site.yml --private-key terraform.pem
build:
	docker build -t raboley/ansible .
	#docker run --rm raboley/ansible
	./exectue.sh play site.yml -i inventory
	#-e 'some_var=some_value'