import boto3

from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb', region_name = 'us-east-2')

table = dynamodb.Table('Movies')

fe = Key('year').between(1950, 1959)
pe = "#yr, title, info.rating"
ean = { "#yr": "year", }
esk = None

response = table.scan(
    FilterExpression = fe,
    ProjectionExpression = pe,
    ExpressionAttributeNames = ean
    )
    
print(response)