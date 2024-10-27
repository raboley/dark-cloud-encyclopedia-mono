from .rekognize_image  import create_json_fullpath, rekognize_image_json, write_image_json_to_file
import json
import boto3
from .get_matching_s3_objects import get_matching_s3_keys
from .upload_images_to_s3 import uploadfile
from .get_basename import path_basename
s3 = boto3.resource('s3')

bucket_name = 'dark-cloud-bucket2'
bucket_image_folder_path = 'new_images/'
bucket_text_folder_path = 'new_text/'
photo_extension = '.jpg'
local_text_folder = './picture_text'


files = get_matching_s3_keys(bucket=bucket_name, prefix=bucket_image_folder_path, suffix=photo_extension)

for photo in files: 
    print(photo)
    write_image_json_to_file(foldertosavein=local_text_folder, bucket=bucket_name, photo=photo)

    local_text_fullpath = create_json_fullpath(foldertosavein=local_text_folder, photo=photo)
    bucket_text_fullpath = bucket_text_folder_path + path_basename(photo) + '.json'
    uploadfile(bucket=bucket_name, upload_file_full_path=bucket_text_fullpath, local_filepath=local_text_fullpath)

    # Determine image type based on json

    # If it is a stat screen

        # get the weapon name

        # figure out the character name based on the weapon name

        # write the weapon name to the pair file

        # copy the file to the staging folder with the correct name

