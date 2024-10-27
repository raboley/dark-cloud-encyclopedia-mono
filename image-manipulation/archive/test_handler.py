import unittest
import boto3
from FileS3 import FileS3
from CropImage import CropImage
# def get_all_unique_parent_folders(file_object, prefix):
#     keys = get_matching_s3_objects(bucket=file_object.bucket_name, prefix=prefix)
#     tweet_ids = set([])
#     for key_dict in keys:
#         key = key_dict["Key"]
#         tweet_ids.add(file_object.get_parent_folder_name(key))
#     return tweet_ids

class test_ensure_images_get_cropped(unittest.TestCase):
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

    def test_can_crop_images_with_single_quotes_in_the_name(self):
        fileObject = FileS3("dark-cloud-bucket-dev")
        cropImage = CropImage(fileObject, '__test/')
        source_key = "staging/weapons/images/Ruby_Satan's_Ring_Side1.jpg"
        upload_key = cropImage.get_thumbnail_name(source_key=source_key)
        
        image = fileObject.read_image(source_key)
        img = cropImage.crop_side_image_to_thumbnail(image_bytes=image)
        img.show()
        fileObject.upload_image_to_s3(img, upload_key)
        self.assertTrue(img)
    
if __name__ == '__main__':
    unittest.main()