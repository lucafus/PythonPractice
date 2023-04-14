import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-2')

table = dynamodb.Table('Movies')

title = 'The New Movie'
year = 2015

response = table.get_item(
    Key={
        'year': year,
        'title': title
    }
    
)

print(response)

