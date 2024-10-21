import boto3

# if __name__ == "__main__":

#     imageFile='/Users/russellboley/Downloads/Git/categorize-images/tests/_testArtifacts/test_controller/abcdefg_ruby_crystalring_bdc.jpg'
#     client=boto3.client('rekognition')
   
#     with open(imageFile, 'rb') as image:
#         response = client.detect_labels(Image={'Bytes': image.read()})
        
#     print('Detected labels in ' + imageFile)    
#     for label in response['Labels']:
#         print (label['Name'] + ' : ' + str(label['Confidence']))

#     print('Done...')


class rekognize():

    def rekognize_image(self):
        pass

    def __init__(self, file_object):
        self.file_object = file_object
        self.client = boto3.client('rekognition')

class rekognize_local(rekognize):

    def rekognize_image(self):
        image_bytes = self.file_object.get_photo()
        response = self.client.detect_labels(Image={'Bytes': image_bytes})
        return response

import unittest
import FileOs

class controller(unittest.TestCase):

    def test_rekognize_image(self):
        pass

    def test_rekognize_image_local(self):
        file_object = FileOs.FileOs('/categorize/pictures/')
        file_object
        response = rekognize_local(file_object)
