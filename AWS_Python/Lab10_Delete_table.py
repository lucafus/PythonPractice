import boto3

dynamodb = boto3.resource('dynamodb', region_name = 'us-east-2')

table = dynamodb.Table('Movies')

result = table.delete()

print(result)