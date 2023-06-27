from secret import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY

import time
import boto3
import os
import time
import shutil
from datetime import datetime

date = datetime.now().strftime("%Y-%m-%d")
dir_name = "C:/Users/mzahn/Documents/"
zip_path= "C:/Users/mzahn/"
filename = "laptop-"
extension = ".zip"
output_filename = filename + date

print ('Starting back-up to S3 bucket.... ')

os.chdir("C:/Users/mzahn/")
shutil.make_archive(output_filename, 'zip', dir_name)

client = boto3.client('s3',
                        aws_access_key_id = AWS_ACCESS_KEY_ID,
                        aws_secret_access_key = AWS_SECRET_ACCESS_KEY)

for file in os.listdir():
    if file.endswith('.zip'):
        upload_file_bucket = 'laptop-bkp'
        upload_file_key = str(file)
        client.upload_file(file, upload_file_bucket, upload_file_key)

# Cleanup
os.remove(output_filename + extension)
print('Backup completed')
time.sleep(1)