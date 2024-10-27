from PIL import Image
from io import StringIO, BytesIO
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
    input_folder = '../categorize-images/all_images/output'
    output_folder = 'output'
    ## generic params
    cropImage = CropImage(fileObject, output_folder=output_folder)

    ## local testing
    image = fileObject.read_image_file("Ungaga_5_Foot_Nail_Side1.jpeg")
    image.show()
    
    cropped = cropImage.crop_out_black_bars(image)
    cropped.show()
