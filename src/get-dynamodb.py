import json
import boto3
import os
dynamodb = boto3.resource('dynamodb')
DDB_WIN_TABLE_NAME = os.environ['DDB_WIN_TABLE_NAME']
table = dynamodb.Table(DDB_WIN_TABLE_NAME)

def handler(event, context):
    win_name = 'coffee'
    try: 
        response = table.get_item(
            Key={
                'win_name': win_name
            }
        )
        item = response['Item']
    except Exception as e:
        print(e)
        item = {
            'win_name': win_name,
            'win_count': 0
        }
        table.put_item(Item=item)
        print("Item create: ", item)

    if 'Item' in response:
        count = response['Item'].get('win_count', 0)
        if count < 21:
            response = table.update_item(
                Key={
                    'win_name': 'coffee'
                },
                UpdateExpression='SET #win_count = #win_count + :incr',
                ExpressionAttributeValues={
                    ':incr': 1
                },
                ExpressionAttributeNames={
                    '#win_count': 'win_count'
                },
                ReturnValues='ALL_NEW'
            )
            response = {
                    'statusCode': 200,
                    'headers': {
                        'Access-Control-Allow-Headers': 'Content-Type',
                        'Access-Control-Allow-Origin': '*',
                        'Access-Control-Allow-Methods': 'OPTIONS,GET',
                        'Timing-Allow-Origin': '*'
                    },
                    'body': True
            }
            return response
        else:
            response = {
                    'statusCode': 200,
                    'headers': {
                        'Access-Control-Allow-Headers': 'Content-Type',
                        'Access-Control-Allow-Origin': '*',
                        'Access-Control-Allow-Methods': 'OPTIONS,GET',
                        'Timing-Allow-Origin': '*'
                    },
                    'body': False
            }
            return response