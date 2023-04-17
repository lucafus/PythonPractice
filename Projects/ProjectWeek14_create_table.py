import boto3

#Select the required resource

dynamodb = boto3.resource('dynamodb', region_name= 'us-east-2')

#Create a DynamoDB table


table = dynamodb.create_table(
    TableName= 'Video_Games',
    KeySchema=[
            
                {   
            
            'AttributeName': 'title',
            'KeyType' : 'HASH'
                        
                    }
    ],
    
    
    AttributeDefinitions=[
            
                {
            
            'AttributeName': 'title',
            'AttributeType' : 'S'
            
            
                    }
    ],
                    
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits' : 10
        
        
    }        
)

print("The Video_Game table has been created")


