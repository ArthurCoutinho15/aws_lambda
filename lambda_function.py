import json
from log import log
import os

def lambda_handler(event, context):
    # TODO implement
    log(f'Log de execução após GitHub Actions. {json.dumps(event)}')
    
    return {
        'statusCode': 200,
        'body': f'<html><body>Dados da requisição: {json.dumps(event)} </body></html>',
        'headers': {
            'content-type': 'text/html'
        } 
    }


