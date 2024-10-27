from PIL import Image
import boto3
from io import StringIO, BytesIO
import requests
from FileS3 import FileS3
from FileOs import FileOs
import os

class CropImage:

    def __init__(self, fileObject, output_folder):
        self.fileObject = fileObject
        self.output_folder = output_folder

    def crop_out_black_bars(self, image_bytes):
        topY = 0
        topX = 117
        bottomY = 675
        bottomX = 1085
        area = (topX, topY, bottomX, bottomY)
        cropped_img = image_bytes.crop(area)
        return cropped_img

    def crop_and_upload_image(self, source_key, upload_key):
        image = self.fileObject.read_image(source_key)
        img = self.crop_out_black_bars(image_bytes=image)
        self.fileObject.upload_image_to_s3(img, upload_key)
        return "Uploaded: " + source_key + "to: " + self.fileObject.bucket_name + ":" + upload_key

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
    ## generic params
    output_folder = 'weapons/images/'
    if not os.path.exists(output_folder):
        print("Creating output folder: " + output_folder)
        os.makedirs(output_folder)
    fileObject = FileOs("__test_source/")
    cropImage = CropImage(fileObject, output_folder=output_folder)

    ## local testing
    image = fileObject.read_image_file("DwJ6vxHUUAARYrH.jpg")
    cropped = cropImage.crop_out_black_bars(image)
    cropped.show()
    image.show()

    ## S3 testing
    # fileObject = FileS3("dark-cloud-bucket-dev")

    # source_key = 'weapons/images/Goro_Last_Judgment_Side1.jpg'
    # upload_key = cropImage.get_thumbnail_name(source_key=source_key)

    # cropImage.crop_and_upload_thumbnail(source_key=source_key, upload_key=upload_key)
