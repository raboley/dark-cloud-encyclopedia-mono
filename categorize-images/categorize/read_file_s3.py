import boto3

def read_file_s3(bucket_name, key):
    client = boto3.client('s3')
    s3_object = client.get_object(Bucket=bucket_name, Key=key)
    body = s3_object['Body']
    return body.read()