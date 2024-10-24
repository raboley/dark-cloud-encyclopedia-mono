deploy:
	kubectl create -f deploy.yml
	kubectl create -f service.yml
update:
	kubectl apply -f deploy.yml --record
	kubectl delete svc hello-svc
	kubectl delete svc flask-handler
	kubectl delete svc flask-books
	kubectl create -f service.yml