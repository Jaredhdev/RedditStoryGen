import os
import boto3


def download_video():
    session = boto3.session.Session()
    s3 = session.client('s3',
                        region_name='us-west-2',
                        endpoint_url='https://s3.us-west-2.amazonaws.com',
                        aws_access_key_id='AKIAW5L5XMDNKVMXOPPA',
                        aws_secret_access_key='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')

    filename = 'minecraft15.mp4'
    bucket_name = 'reddit-story-gen'

    path = os.path.join('/tmp', filename)

    if not os.path.exists(path):
        s3.download_file(bucket_name, filename, path)
        print('File Downloaded')
    else:
        print('File already downloaded')

