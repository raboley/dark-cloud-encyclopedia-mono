setup:
	bash setup.sh
	. env/bin/activate
	npm install
	serverless plugin install --name serverless-python-requirements
	npm install serverless-plugin-existing-s3
deploy:
	serverless deploy --stage dev
	sls s3deploy --stage dev