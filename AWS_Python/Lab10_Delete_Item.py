import boto3
from botocore.exceptions import ClientError
import decimal

dynamodb = boto3.resource('dynamodb', region_name='us-east-2')

table = dynamodb.Table('Movies')

title = 'The New Movie'
year = 2019

print("Attempting delete")

try:
    response = table.delete_item(
        
        Key = {
            'year': year,
            'title' : title
        },
        ConditionExpression="#info_rating > :val",
        ExpressionAttributeNames= { 
            "#info_rating" : "info.rating"
          
        },
        ExpressionAttributeValues = {
            ":val": decimal.Decimal(3)
        }    
    )
        
except ClientError as e:
    if e.response['Error']['Code'] == "ConditionalCheckFailedException":
        print(e.response['Error']['Message'])
    else:
        raise
else:
    print("DeleteItem succeeded:")
    print(json.dumps(response, indent=4, cls=DecimalEncoder))