from context import categorize
import unittest
import boto3
# from testfixtures import tempdir, compare, TempDirectory
# import os
# import json

FileS3 = categorize.FileS3

class test_FileS3(unittest.TestCase):
    """
    Ensure file object can get set and output paths to files
    """

    def setUp(self):
        self.bucket = 'dark-cloud-bucket'
        self.File_object = FileS3(bucket=self.bucket)
        self.output_folder = "__testing/"

    def tearDown(self):
        pass #self.delete_s3_objects(bucket_name=self.bucket,output_folder=self.output_folder)
        

    def delete_s3_objects(self, bucket_name, output_folder):
        s3 = boto3.resource('s3')
        objects_to_delete = s3.meta.client.list_objects(Bucket=bucket_name, Prefix=output_folder)

        delete_keys = {'Objects' : []}
        delete_keys['Objects'] = [{'Key' : k} for k in [obj['Key'] for obj in objects_to_delete.get('Contents', [])]]
        if delete_keys['Objects']:
            s3.meta.client.delete_objects(Bucket=bucket_name, Delete=delete_keys)

    def test_can_put_json_in_s3_bucket(self):
        # I think something about the way it makes requests to AWS was screwing this up
        # if I put these two calls in setup then the second test no longer works. 
        key = self.output_folder + 'test_json.json'
        data = [{"key":'12-11',"value":'choora'},{"key":'12-12',"value":'crystal_ring'},{"key":'12-13',"value":'omega'}]
        self.File_object.put_json_file(key=key, json_data=data)
        pushed_objects = categorize.get_matching_s3_keys(bucket=self.bucket, prefix=self.output_folder)
        self.assertTrue(pushed_objects)

    def test_can_read_back_json_correctly(self):
        test_data = [{"key":'12-11',"value":'choora'},{"key":'12-12',"value":'crystal_ring'},{"key":'12-13',"value":'omega'}]
        key = self.output_folder + 'test_json.json'
        json_data = self.File_object.read_json_file(key=key)
        self.assertEqual(json_data, test_data)

    def test_can_read_then_append_more_data(self):
        test_data = [{"key":'12-11',"value":'choora'},{"key":'12-12',"value":'crystal_ring'},{"key":'12-13',"value":'omega'},{"key":'12-14',"value":'Append_test'}]
        key = self.output_folder + 'test_json.json'
        json_to_append = {"key":'12-14',"value":'Append_test'}
        self.File_object.append_json_file(key=key,json_data=json_to_append)
        appended_json = self.File_object.read_json_file(key=key)
        self.assertEqual(appended_json, test_data)

    def test_can_return_parent_folder_name(self):
        full_path = 'archive/2019-01-18_13-53-00/Dvndh6DUYAAF1rM.jpg'
        parent_name = self.File_object.get_parent_folder_name(full_path)
        self.assertEqual(parent_name, '2019-01-18_13-53-00')
    
    def test_copy_file_will_copy_file_with_new_name(self):
        source_path = "archive/2019-01-27_18-20-31/DwJ6vY_VAAIexyj.jpg"
        dest_path = self.output_folder + 'weapons/Toan_Choora_Stats.jpg'
        self.File_object.copy_file(source_path=source_path, dest_path=dest_path)
        self.assertTrue(self.File_object.check_existence(dest_path))

    def test_copy_file_will_copy_file_with_new_name_to_another_bucket(self):
        source_path = "archive/2019-01-27_18-20-31/DwJ6vY_VAAIexyj.jpg"
        dest_path = 'dark-cloud-bucket2:'+ self.output_folder + 'weapons/Toan_Choora_Stats.jpg'
        other_bucket_dest = self.output_folder + 'weapons/Toan_Choora_Stats.jpg'
        self.File_object.copy_file(source_path=source_path, dest_path=dest_path)
        output_object = FileS3('dark-cloud-bucket2')
        self.assertTrue(output_object.check_existence(other_bucket_dest))

    def test_splits_bucket_and_path(self):
        full_path = 'dark-cloud-bucket2:'+ self.output_folder + 'weapons/Toan_Choora_Stats.jpg'
        bucket, output_path = self.File_object.split_bucket_path(full_path)
        self.assertEqual(bucket, 'dark-cloud-bucket2')
        self.assertEqual(output_path, '__testing/weapons/Toan_Choora_Stats.jpg')

    def test_z_teardown_does_remove_items(self):
        self.delete_s3_objects(bucket_name=self.bucket,output_folder=self.output_folder)
        pushed_objects = categorize.get_matching_s3_keys(bucket=self.bucket, prefix=self.output_folder)
        
        count = 0
        for obj in pushed_objects:
            count+= 1
        self.assertEqual(int(0), count)



if __name__ == "__main__":
    unittest.main()



# class test_integration_handler(unittest.TestCase):
#     """
#     Ensure that new tweets get downloaded to s3 when called with valid arguments
#     """

#     def setUp(self):
#         self.event_user = {
#             "config": "./config.cfg",
#             "username_or_hashtag": "cloud_images",
#             "hashtag": "",
#             "num": "3",
#             "retweets": "False",
#             "replies": "False",
#             "output_folder": "__testing/",
#             "bucket": "dark-cloud-bucket",
#             "download_lambda_name": "fetch-file-and-store-in-s3-dark-cloud-dev-save"
#         }
        
#         self.event_hashtag = {
#             "config": "./config.cfg",
#             "username_or_hashtag": "#dark_Clou2d_Images",
#             "hashtag": "",
#             "num": "3",
#             "retweets": "False",
#             "replies": "False",
#             "output_folder": "__testing/",
#             "bucket": "dark-cloud-bucket",
#             "download_lambda_name": "fetch-file-and-store-in-s3-dark-cloud-dev-save"
#         }

    



    
#     @unittest.skip('Cant really count the objects in a s3 bucket so easy like this I guess...')
#     def test_only_correct_num_of_images_get_downloaded(self):      
#         handler.search_for_new_tweets(self.event_user,'')
#         pushed_objects = get_matching_s3_objects.get_matching_s3_keys(bucket=self.bucket, prefix=self.output_folder)
        
#         count = 0
#         for obj in pushed_objects:
#             count+= 1
#         self.assertEqual(int(self.event_user['num']), count)
    
    
#     def test_new_twitter_images_from_hashtag_get_downloaded(self):
#         handler.search_for_new_tweets(self.event_hashtag,'')
#         pushed_objects = get_matching_s3_objects.get_matching_s3_keys(bucket=self.event_hashtag['bucket'], prefix=self.event_hashtag['output_folder'])
        
#         self.assertTrue(pushed_objects)


