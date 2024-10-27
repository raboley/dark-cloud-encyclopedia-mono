from PIL import Image
import boto3
from io import StringIO, BytesIO
import requests
from FileS3 import FileS3
import os

class CropImage:
    
    def __init__(self, fileObject, output_folder):
        self.fileObject = fileObject
        self.output_folder = output_folder

    def crop_side_image_to_thumbnail(self, image_bytes):
        topY = 584
        topX = 156
        bottomY = topY + 55
        bottomX = topX + 60
        area = (topX, topY, bottomX, bottomY)
        cropped_img = image_bytes.crop(area)
        return cropped_img

    def crop_and_upload_thumbnail(self, source_key, upload_key):
        image = self.fileObject.read_image(source_key)
        img = self.crop_side_image_to_thumbnail(image_bytes=image)
        self.fileObject.upload_image_to_s3(img, upload_key)
        return "Uploaded: " + source_key + "to: " + self.fileObject.bucket_name + ":" + upload_key

    def get_thumbnail_name(self, source_key: str):
        file_name = self.fileObject.path_basename(source_key)
        output_key = os.path.join(self.output_folder, file_name)

        replace_string = 'Side1'
        thumbnail_string = 'Thumbnail.jpg'
        upload_key = output_key.replace(replace_string, thumbnail_string)
        return upload_key

if __name__ == '__main__':
    #image = read_image_file("__test_source/DwJ6vxHUUAARYrH.jpg")
    fileObject = FileS3("dark-cloud-bucket-dev")
    
    output_folder = 'weapons/images/'
    cropImage = CropImage(fileObject, output_folder=output_folder)
    
    source_key = 'weapons/images/Goro_Last_Judgment_Side1.jpg'
    upload_key = cropImage.get_thumbnail_name(source_key=source_key)
    
    cropImage.crop_and_upload_thumbnail(source_key=source_key, upload_key=upload_key)


    
    

