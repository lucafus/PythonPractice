import boto3

#Select the required resource

dynamodb = boto3.resource('dynamodb', region_name = 'us-east-2')

#Select the required table

table = dynamodb.Table('Video_Games')

#Add 10 items into the table

table.put_item(
    Item={
        'title': "Metal Gear Solid 3",
        'info': { 
            'year': 2004 ,
            'genre': "Stealth" ,
            'rating' : 10
        }
    }
    
)

table.put_item(
    Item={
        'title': "God of War 2",
        'info': { 
            'year': 2007 ,
            'genre': " Hack and slash" ,
            'rating' : 9
        }
    }
    
)

table.put_item(
    Item={
        'title': "Resident Evil 4",
        'info': { 
            'year': 2005 ,
            'genre': "Survival Horror" ,
            'rating' : 10
        }
    }
    
)

table.put_item(
    Item={
        'title': "Burnout 3: Takedown",
        'info': { 
            'year': 2004 ,
            'genre': "Racing" ,
            'rating' : 8
        }
    }
    
)

table.put_item(
    Item={
        'title': "Devil May Cry 3",
        'info': { 
            'year': 2005 ,
            'genre': "Hack and slash" ,
            'rating' : 8
        }
    }
    
)

table.put_item(
    Item={
        'title': "Tom Clancy's Splinter Cell",
        'info': { 
            'year': 2002 ,
            'genre': "Stealth" ,
            'rating' : 9
        }
    }
    
)

table.put_item(
    Item={
        'title': "Shadow of the Colossus",
        'info': { 
            'year': 2005 ,
            'genre': "Action-Adventure" ,
            'rating' : 10
        }
    }
    
)

table.put_item(
    Item={
        'title': "Prince of Persia",
        'info': { 
            'year': 2003 ,
            'genre': "Action-Adventure" ,
            'rating' : 9
        }
    }
    
)

table.put_item(
    Item={
        'title': "God of War 1",
        'info': { 
            'year': 2005 ,
            'genre': "Hack and slash" ,
            'rating' : 10
        }
    }
    
)

table.put_item(
    Item={
        'title': "Hitman: Blood Money",
        'info': { 
            'year': 2006 ,
            'genre': "Stealth" ,
            'rating' : 10
        }
    }
    
)

print("Put Items succeded")


#Scan all the items on our table

data1 = table.scan()

print(data1, sep='\n')



#Query an specific Item

from boto3.dynamodb.conditions import Key

data2 = table.query(
    KeyConditionExpression=Key('title').eq("Metal Gear Solid 3")
    )
    
for i in data2['Items']:
    print(i['title'])
    

# Delete an specific Item

deletion = table.delete_item(
        Key={
            'title': 'Metal Gear Solid 3'
        }
    )
    
print('Deletion completed: ' , deletion)    