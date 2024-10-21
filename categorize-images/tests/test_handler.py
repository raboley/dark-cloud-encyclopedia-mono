import unittest
from testfixtures import tempdir, compare, TempDirectory
import boto3
import os

from context import categorize
FileS3 = categorize.FileS3

class test_set_image_name(unittest.TestCase):
    """
    Ensure that we can set the image name correctly with weapon, character name and type
    """
    def setUp(self):
        self.bucket = 'dark-cloud-bucket'
        self.File_object = FileS3(bucket=self.bucket)
        self.output_folder = "__test/weapons"

    def tearDown(self):
        self.delete_s3_objects(bucket_name=self.bucket,output_folder=self.output_folder)
        

    def delete_s3_objects(self, bucket_name, output_folder):
        s3 = boto3.resource('s3')
        objects_to_delete = s3.meta.client.list_objects(Bucket=bucket_name, Prefix=output_folder)

        delete_keys = {'Objects' : []}
        delete_keys['Objects'] = [{'Key' : k} for k in [obj['Key'] for obj in objects_to_delete.get('Contents', [])]]
        if delete_keys['Objects']:
            s3.meta.client.delete_objects(Bucket=bucket_name, Delete=delete_keys)

    @unittest.skip("demonstrating skipping")
    def test_categorize_and_move_image_does_create_the_image(self):
        os.environ['stage'] = 'dev'
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
                "key": "archive/2019-01-27_18-20-31/DwJ6vY_VAAIexyj.jpg",
                "size": 1024
                },
                "bucket": {
                "arn": "TEST",
                "name": "dark-cloud-bucket",
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

        args = {
            "bucket_name": event['Records'][0]['s3']['bucket']['name'],
            "image_key": event['Records'][0]['s3']['object']['key'],
            "bucket_image_folder_path": "new_images/",
            "bucket_text_folder_path": "new_text/",
            "local_text_folder": "/temp/",
            "weapon_mapping_file": "mappings/all_weapons.json",
            "datefolder_character_weapon_mapping_file": "__test/mappings/datefolder_character_weapon_mapping_file.json",
            "output_folder_name": "__test/weapons",
            "output_bucket_name": "dark-cloud-bucket",
            "stage": "dev"
        }

        # file_object =  categorize.FileS3(event['Records'][0]['s3']['bucket']['name'])
        output_file_object = categorize.FileS3(event['Records'][0]['s3']['bucket']['name'])
        categorize.categorize_and_move_image(event, '')
        test_full_path = args["output_folder_name"] + '/Toan_Choora_Stat.jpg'
        self.assertTrue(output_file_object.check_existence(test_full_path))

    @unittest.skip("demonstrating skipping")
    def test_can_rekognize_osmund_star_breaker(self):
        os.environ['stage'] = 'dev'
        key = 'archive/1091843622935224320/DycB-4WU8AAgd28.jpg'
        bucket = 'dark-cloud-bucket-dev'
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
                "key": key,
                "size": 1024
                },
                "bucket": {
                "arn": "TEST",
                "name": bucket,
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

        args = {
            "bucket_name": event['Records'][0]['s3']['bucket']['name'],
            "image_key": event['Records'][0]['s3']['object']['key'],
            "bucket_image_folder_path": "new_images/",
            "bucket_text_folder_path": "new_text/",
            "local_text_folder": "/temp/",
            "weapon_mapping_file": "mappings/all_weapons.json",
            "datefolder_character_weapon_mapping_file": "__test/mappings/datefolder_character_weapon_mapping_file.json",
            "output_folder_name": "__test/weapons",
            "output_bucket_name": bucket,
            "stage": "dev"
        }

        # file_object =  categorize.FileS3(event['Records'][0]['s3']['bucket']['name'])
        output_file_object = categorize.FileS3(event['Records'][0]['s3']['bucket']['name'])
        categorize.categorize_and_move_image(event, '')
        test_full_path = args["output_folder_name"] + '/Osmund_Star_Breaker_Stats.jpg'
        self.assertTrue(output_file_object.check_existence(test_full_path))
        
    def test_can_recognize_g_crusher_osmond(self):
        key = 'archive/1092186392078110720/Dyg5uq1VsAIudez.jpg'
        os.environ['stage'] = 'dev'
                
        
        bucket = 'dark-cloud-bucket-dev'
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
                "key": key,
                "size": 1024
                },
                "bucket": {
                "arn": "TEST",
                "name": bucket,
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

        args = {
            "bucket_name": event['Records'][0]['s3']['bucket']['name'],
            "image_key": event['Records'][0]['s3']['object']['key'],
            "bucket_image_folder_path": "new_images/",
            "bucket_text_folder_path": "new_text/",
            "local_text_folder": "/temp/",
            "weapon_mapping_file": "mappings/all_weapons.json",
            "datefolder_character_weapon_mapping_file": "__test/mappings/datefolder_character_weapon_mapping_file.json",
            "output_folder_name": "__test/weapons",
            "output_bucket_name": bucket,
            "stage": "dev"
        }

        # file_object =  categorize.FileS3(event['Records'][0]['s3']['bucket']['name'])
        output_file_object = categorize.FileS3(event['Records'][0]['s3']['bucket']['name'])
        categorize.categorize_and_move_image(event, '')
        test_full_path = args["output_folder_name"] + '/Osmund_Star_Breaker_Stat.jpg'
        self.assertTrue(output_file_object.check_existence(test_full_path))

if __name__ == '__main__':
    unittest.main()