import boto3

dynamodb = boto3.resource('dynamodb', region_name = 'us-east-2')

table = dynamodb.Table('Movies')

title = "The New Movie"
year = 2019

response = table.put_item(
    Item={
        'year': year,
        'title': title,
        'info': { 
            'plot': "Nothing Happens",
            'rating' : 10
        }
    }
    
)

print("Put Item succeded: ")