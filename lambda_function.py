import json
from log import log

def lambda_handler(event, context):
    # TODO implement
    log(f'Log de execução após GitHub Actions. {json.dumps(event)}')
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }


