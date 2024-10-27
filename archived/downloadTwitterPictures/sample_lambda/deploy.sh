sam package --s3-bucket aslkfjaslekfje --template-file template.yaml --output-template-file package.yaml
sam package --s3-bucket aslkfjaslekfje --template-file template.yaml --output-template-file packaged.yaml
sam deploy --template-file packaged.yaml --stack-name mySafeDeployStack --capabilities CAPABILITY_IAM