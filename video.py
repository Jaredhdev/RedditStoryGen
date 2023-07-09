import os
import boto3
from dotenv import load_dotenv


def download_video():
    session = boto3.session.Session()
    load_dotenv()
    aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
    aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
    s3 = session.client('s3',
                        region_name='us-west-2',
                        endpoint_url='https://s3.us-west-2.amazonaws.com',
                        aws_access_key_id=aws_access_key_id,
                        aws_secret_access_key=aws_secret_access_key)

    filename = 'minecraft15.mp4'
    bucket_name = 'reddit-story-gen'

    path = os.path.join('/tmp', filename)

    if not os.path.exists(path):
        s3.download_file(bucket_name, filename, path)
        print('File Downloaded')
    else:
        print('File already downloaded')

