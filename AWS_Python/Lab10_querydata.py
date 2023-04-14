import boto3
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb', region_name='us-east-2')

table = dynamodb.Table('Movies')

print('Movies from 1985')

response = table.query(
    KeyConditionExpression=Key('year').eq(1985)
    )
    
for i in response['Items']:
    print(i['year'], ":", i['title'])