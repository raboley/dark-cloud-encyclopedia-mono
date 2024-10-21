import boto3
import os

# Let's use Amazon S3
s3 = boto3.resource('s3')

# Print out bucket names
#for bucket in s3.buckets.all():
#    print(bucket.name)



# Upload a new file
def uploadfile(bucket, upload_file_full_path, local_filepath):
    """Uploads a file to an s3 bucket from a local computer

    Parameters
    ----------
    bucket : str
            the string bucket name of the bucket to upload to

    print_cols : bool, optional
    A flag used to print the columns to the console (default is False)

    Returns
    -------
    list
    a list of strings representing the header columns
    """
    
    data = open(local_filepath, 'rb')
    s3.Bucket(bucket).put_object(Key=upload_file_full_path, Body=data)

def uploadfolder(bucket='dark-cloud-bucket2', folder_to_upload='./pictures', destination_folder_path=''):
    directory = os.fsencode(folder_to_upload)

    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        filepath = folder_to_upload + '/' + filename
        
        if destination_folder_path != '':
                upload_file_full_path = destination_folder_path + '/' + filename
        else:
                upload_file_full_path = filename
        print("Uploading " + filepath + '        TO: ' + upload_file_full_path)
        uploadfile( bucket=bucket, upload_file_full_path=upload_file_full_path, local_filepath=filepath)
 
if __name__ == "__main__":
        uploadfolder(destination_folder_path='new_images')