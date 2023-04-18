import boto3

#Select the required resource

dynamodb = boto3.resource('dynamodb', region_name= 'us-east-2')

#Call the create_table method

table = dynamodb.create_table( 
    
    TableName= 'Video_Games',
    
    AttributeDefinitions=[ 
            
                {
            
            'AttributeName': 'title', # Specify the name of the title attribute
            'AttributeType' : 'S'     # Specify that the title attribute is a string
            
            
                    }
    ],
    
    
    KeySchema=[ 
            
                {   
            
            'AttributeName': 'title', # Specify that the title attribute will be used as the partition key
            'KeyType' : 'HASH'        # Specify that the title attribute will be used as the hash key
                        
                    }
    ],
    
    
    
                    
    ProvisionedThroughput={
        'ReadCapacityUnits': 1,
        'WriteCapacityUnits' : 1
        
        
    }        
)

print("The Video_Game table has been created")


