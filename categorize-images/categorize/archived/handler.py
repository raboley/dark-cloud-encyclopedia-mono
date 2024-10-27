import json
from .set_image_name import copy_image_to_folder_with_categorized_name
from .FileS3 import FileS3
import os

def categorize_and_move_image(event, context):
    STAGE = os.environ['stage']  
    if STAGE == "dev":
        output_bucket_name = event['Records'][0]['s3']['bucket']['name']
        output_folder_name = output_bucket_name + ":staging/weapons/images"
    elif STAGE == "prod":
        output_bucket_name = "dark-cloud-bucket2"
        output_folder_name = "dark-cloud-bucket2:staging/weapons/images"

    args = {
        "bucket_name": event['Records'][0]['s3']['bucket']['name'],
        "image_key": event['Records'][0]['s3']['object']['key'],
        "bucket_image_folder_path": "new_images/",
        "bucket_text_folder_path": "new_text/",
        "local_text_folder": "/temp/",
        "weapon_mapping_file": "mappings/all_weapons.json",
        "datefolder_character_weapon_mapping_file": "mappings/datefolder_character_weapon_mapping_file.json",
        "output_folder_name": output_folder_name,
        "output_bucket_name": output_bucket_name
    }

    file_object =  FileS3(args['bucket_name'])
    output_file_object = FileS3(args["output_bucket_name"])

    output = copy_image_to_folder_with_categorized_name(args, file_object, output_file_object)
    
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

# Use this code if you don't use the http event with the LAMBDA-PROXY
# integration
"""
return {
    "message": "Go Serverless v1.0! Your function executed successfully!",
    "event": event
}
"""

# def get_arguments(username='cloud_images', destination_bucket='dark-cloud-bucket', num=5, output_folder='archive/', download_lambda_name='fetch-file-and-store-in-s3-dark-cloud-dev-save'):
#   args = { 
#     'config': './config.cfg',
#     'username': username,
#     'hashtag': '',
#     'num': num,
#     'retweets': False,
#     'replies': False,
#     'output_folder': output_folder,
#     'bucket': destination_bucket,
#     'download_lambda_name': download_lambda_name
#   }
#   print(args)
#   return args

def parse_event(default_event,event):    
    return_event = default_event
    
    return_event.update(event)
    # for key, value in default_event.items():
    #     if key in event:
    #         return_event.update(key = value)
    return return_event


if __name__ == '__main__':
    #get_arguments()
    event = {
        "config": "./config.cfg",
        "username_or_hashtag": "cloud_images",
        "hashtag": "",
        "num": "5",
        "retweets": "False",
        "replies": "False",
        "output_folder": "archive/",
        "bucket": "dark-cloud-bucket",
        "download_lambda_name": "fetch-file-and-store-in-s3-dark-cloud-dev-save"
    }
    search_for_new_tweets(event,'')
