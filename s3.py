import boto3
import logging
from botocore.exceptions import ClientError
from botocore.config import Config
#import requests


logging.basicConfig(level=logging.INFO)

def adds3(file_to_upload, object_name):

    try:
        s3_resource = boto3.resource(
            's3',
            endpoint_url = 'https://s3.ir-thr-at1.arvanstorage.ir',
            aws_access_key_id = '79ad1d7d-9e71-4d87-861b-63983db0e6a5',
            aws_secret_access_key = '028c7d144574f887a03cf795418f9c1e36fb0204' 
        )
    except Exception as exc:
        logging.error(exc)
    else:
        try:
            bucket = s3_resource.Bucket('project-javad')
            bucket.put_object(
                ACL='private',
                Body=file_to_upload,
                Key=object_name
            )
        except ClientError as e:
            logging.error(e)
            




def generate_presigned_url(bucketname ,objectname):

    try:
        s3_client = boto3.client(
            's3',
            endpoint_url='https://s3.ir-thr-at1.arvanstorage.ir',
            aws_access_key_id = '79ad1d7d-9e71-4d87-861b-63983db0e6a5',
            aws_secret_access_key = '028c7d144574f887a03cf795418f9c1e36fb0204'
        )

    except Exception as exc:
        logging.error(exc)
    else:
        try:
            bucket = bucketname
            object_name = objectname

            response = s3_client.generate_presigned_url(
                'get_object',
                Params={
                    'Bucket': bucket,
                    'Key': object_name
                },
                ExpiresIn=3600
            )
        except ClientError as e:
            logging.error(e)
    return response  
#if __name__ =='__main__':
    
    #print(generate_presigned_url('project-javad','217a9fe56b8111edb9bd5c879c9b432fcar1.jpg'))
    
    
    
    


