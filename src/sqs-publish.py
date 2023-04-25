import json
import boto3
import os
sqs = boto3.client('sqs')
SQS_QUEUE_URL = os.environ['SQS_QUEUE_URL']

def publish_sqs(message):
    try:
        results = sqs.send_message(
            QueueUrl=SQS_QUEUE_URL,
            MessageBody=message
        )
        print('Publish SQS Success')
        return results
    except Exception as e:
        print('Publish SQS Error: ', e)
        return {}

def handler(event, context):
    print(json.dumps(event))
    response = {}
    
    if event['httpMethod'] == 'POST':
        data = publish_sqs(json.dumps(event))
        response = {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'OPTIONS,POST',
                'Timing-Allow-Origin': '*'
            },
            'body': "Published SQS",
        }
    
    print('Response: ', json.dumps(response))
    return response
