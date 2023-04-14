import boto3


dynamodb = boto3.resource("dynamodb", region_name='us-east-2' )

table = dynamodb.Table('Movies')

title = "The New Movie"
year = 2019

response = table.update_item(
    Key={
        'year': year,
        'title':title 
    },
    UpdateExpression = "set #info_rating=:r, #info_plot=:p, #info_actors=:a",
    ExpressionAttributeNames ={
        '#info_rating': 'info.rating',
        '#info_plot': 'info.plot',
        '#info_actors': 'info.actors'
        },
    ExpressionAttributeValues = {
        
        ':p': "Everything happens all at once.",
        ':a': ["Larry", "Moe", "Curly"],
        ':r': '5.5'
    },
    ReturnValues = "UPDATED_NEW"
    
    )
    
print("Update item succeded")