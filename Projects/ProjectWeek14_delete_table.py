import boto3

#Select the required resource

dynamodb = boto3.resource('dynamodb', region_name = 'us-east-2')

#Select the required table

table = dynamodb.Table('Video_Games')

result = table.delete()

print(result) 