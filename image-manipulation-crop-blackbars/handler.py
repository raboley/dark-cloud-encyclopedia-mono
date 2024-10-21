import json
import os
from FileS3 import FileS3
from CropImage import CropImage

def create_thumbnail(event, context):
    
    output_folder = 'weapons/images/'
    args = {
        "bucket_name": event['Records'][0]['s3']['bucket']['name'],
        "image_key": event['Records'][0]['s3']['object']['key'],
    }

    fileObject = FileS3(args["bucket_name"])
    cropImage = CropImage(fileObject, output_folder=output_folder)

    file_name = fileObject.get_file_name(args["image_key"])
    upload_key = os.path.join(output_folder, file_name)
    output = cropImage.crop_and_upload_image(source_key=args["image_key"],upload_key=upload_key)

    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event,
        "output": output
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
    return response

if __name__ == '__main__':
    event = {
    "Records": [
        {
        "eventVersion": "2.0",
        "eventTime": "1970-01-01T00:00:00.000Z",
        "requestParameters": {
            "sourceIPAddress": "127.0.0.1"
        },
        "s3": {
            "configurationId": "testConfigRule",
            "object": {
            "eTag": "0123456789abcdef0123456789abcdef",
            "sequencer": "0A1B2C3D4E5F678901",
            "key": "staging/weapons/images/Goro_Last_Judgment_Side1.jpg",
            "size": 1024
            },
            "bucket": {
            "arn": "TEST",
            "name": "dark-cloud-bucket-dev",
            "ownerIdentity": {
                "principalId": "EXAMPLE"
            }
            },
            "s3SchemaVersion": "1.0"
        },
        "responseElements": {
            "x-amz-id-2": "EXAMPLE123/5678abcdefghijklambdaisawesome/mnopqrstuvwxyzABCDEFGH",
            "x-amz-request-id": "EXAMPLE123456789"
        },
        "awsRegion": "us-east-1",
        "eventName": "ObjectCreated:Put",
        "userIdentity": {
            "principalId": "EXAMPLE"
        },
        "eventSource": "aws:s3"
        }
    ]
    }
    create_thumbnail(event, '')