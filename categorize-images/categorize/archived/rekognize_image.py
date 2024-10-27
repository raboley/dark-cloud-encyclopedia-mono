# Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# PDX-License-Identifier: MIT-0 (For details,
# see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)

import boto3
import json
from .get_basename import path_basename

s3 = boto3.resource('s3')


def create_json_fullpath(foldertosavein='./picture_text', photo='Ruby_Crystal_Ring_Stats.jpg'):
    filebasename = path_basename(photo)
    final_path = foldertosavein + '/' + filebasename + '.json'
    return final_path


# if __name__ == "__main__":
def rekognize_image_json(bucket='dark-cloud-bucket2', photo='Ruby_Crystal_Ring_Stats.jpg'):
    client = boto3.client('rekognition')
    response = client.detect_text(Image={'S3Object': {'Bucket': bucket, 'Name': photo}})
    textDetections = response['TextDetections']
    return textDetections


def write_image_json_to_file(foldertosavein='./categorize/picture_text', bucket='dark-cloud-bucket',
                             photo='Ruby_Crystal_Ring_Stats.jpg'):
    final_path = create_json_fullpath(foldertosavein=foldertosavein, photo=photo)
    data = rekognize_image_json(bucket=bucket, photo=photo)
    with open(final_path, 'w') as outfile:
        json.dump(data, outfile, ensure_ascii=False, indent=4)
    return final_path

# write_image_json_to_file(photo='archive/2019-01-18_13-53-00/DwJ6v8fUcAAa-Ov.jpg')
