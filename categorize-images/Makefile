init:
	#pip install -r requirements.txt
	bash setup.sh
	. env/bin/activate
	npm i serverless-plugin-aws-alerts
test:
	nosetests tests
deploy:
	serverless deploy --stage dev
	sls s3deploy --stage dev
	aws s3 cp all_weapons.json s3://dark-cloud-bucket-dev/mappings/
deploy-prod:
	serverless deploy --stage prod --alias prod
	sls s3deploy --stage prod
	aws s3 cp all_weapons.json s3://dark-cloud-bucket-prod/mappings/