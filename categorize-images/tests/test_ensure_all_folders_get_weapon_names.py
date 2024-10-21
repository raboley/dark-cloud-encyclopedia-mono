from context import categorize
import unittest
import boto3
# from testfixtures import tempdir, compare, TempDirectory
# import os
# import json

FileS3 = categorize.FileS3

def get_all_unique_parent_folders(file_object, prefix):
    keys = categorize.get_matching_s3_objects(bucket=file_object.bucket_name, prefix=prefix)
    tweet_ids = set([])
    for key_dict in keys:
        key = key_dict["Key"]
        tweet_ids.add(file_object.get_parent_folder_name(key))
    return tweet_ids

class test_ensure_all_folders_get_weapon_names(unittest.TestCase):
    """
    All archve/id folders should get a matching entry in the weapon mapping file
    and if they don't there should be an alert
    """

    def setUp(self):
        self.bucket = 'dark-cloud-bucket-dev'
        self.file_object = FileS3(bucket=self.bucket)
        self.output_folder = "__testing/"
        self.prefix = 'archive/'
        self.mapping_file_key = 'mappings/datefolder_character_weapon_mapping_file.json'
    
    def test_get_all_folder_names(self):
        tweet_ids = get_all_unique_parent_folders(file_object=self.file_object, prefix=self.prefix)
        self.assertGreater(len(tweet_ids),0)
        

    def test_get_all_the_weapon_mappings(self):
        mapping_json = self.file_object.read_json_file(self.mapping_file_key)
        self.assertTrue(mapping_json)

    def test_find_folders_with_no_match(self):
        tweet_ids = get_all_unique_parent_folders(file_object=self.file_object, prefix=self.prefix)
        weapon_map_json = self.file_object.read_json_file(self.mapping_file_key)
        unmapped_ids = []
        weapon_mapping = []
        for tweet_id in tweet_ids:
            weapon_object = next((item for item in weapon_map_json if item["key"] == tweet_id), 'unknown')
            if weapon_object != 'unknown':
                weapon = weapon_object["weapon name"]
            mapping = {
                "key": tweet_id,
                "weapon": weapon
            }
            if weapon == 'unknown':
                unmapped_ids.append(mapping)
            else:
                weapon_mapping.append(mapping)
        self.assertEqual(len(weapon_mapping), len(tweet_ids))
        self.assertEqual(len(unmapped_ids), 0)

    def test_make_sure_staging_gets_all_pictures(self):
        raw_keys = categorize.get_matching_s3_objects(bucket=self.file_object, prefix=self.prefix)
        self.assertEqual(raw_keys,'')


if __name__ == '__main__':
    unittest.main()