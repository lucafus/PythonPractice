import boto3

dynamodb = boto3.resource('dynamodb', region_name= 'us-east-2')

table = dynamodb.create_table(
    TableName= 'Movies',
    KeySchema=[
        {
            'AttributeName': 'year',
            'KeyType': 'HASH'
                    },
        {   'AttributeName': 'title',
            'KeyType' : 'RANGE'
                        
                    }
    ],
    AttributeDefinitions=[
        {    
            'AttributeName': 'year',
            'AttributeType': 'N'
                        },
            
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

print("Table Status: ", table.table_status  )

