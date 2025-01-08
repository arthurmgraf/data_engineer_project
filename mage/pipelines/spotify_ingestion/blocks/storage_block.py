import boto3
import os
import json

def storage_block(data):
    s3_client = boto3.client(
        's3',
        endpoint_url=os.getenv('MINIO_ENDPOINT'),
        aws_access_key_id=os.getenv('MINIO_ACCESS_KEY'),
        aws_secret_access_key=os.getenv('MINIO_SECRET_KEY')
    )
    
    bucket = 'landing'
    key = 'spotify_recommendations.json'
    s3_client.put_object(
        Bucket=bucket,
        Key=key,
        Body=json.dumps(data)
    )
