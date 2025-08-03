import json
from log import log

import os
import boto3

boto3.setup_default_session(region_name='us-east-1')
s3 =  boto3.client('s3')

def lambda_handler(event, context):
    record = event['Records'][0]
    bucket = record['s3']['bucket']['name']
    key = record['s3']['bucket']['key']
    
    response = s3.head_object(Bucket=bucket, Key=key)  
    content_length = response['ContentLength']   
    
    mega_byte = 1024 * 1024
    
    if content_length > mega_byte:
        log('Objeto muito grande')
        return 'Objeto muito grande'
    
    
    return log('Objeto de tamanho OK')


