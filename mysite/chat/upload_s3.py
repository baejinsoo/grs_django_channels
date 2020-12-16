import boto3
from botocore.client import Config

ACCESS_KEY_ID = ''
ACCESS_SECRET_KEY = ''
BUCKET_NAME = 'grs-img'

def handle_upload_file(f):
    data = open('static/images/'+f,'rb')
    s3 = boto3.resource(
        's3',
        aws_access_key_id=ACCESS_KEY_ID,
        aws_secret_access_key=ACCESS_SECRET_KEY,
        config=Config(signature_version='s3v4')
        )
    s3.Bucket(BUCKET_NAME).put_object(Key=f,Body=data,ContentType='image/jpg')

# img_1 = "jinsoo.jpg"
# print(img_1, type(img_1))
# handle_upload_file(img_1)