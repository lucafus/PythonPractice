import json # Required to encode the response message.
import boto3 # It will allow us to access the SQS services. 
from datetime import datetime # It gets the current date time. 


sqs = boto3.resource('sqs', region_name='us-east-2') #This create an AWS resource using the boto3.resource method. 

def lambda_handler(event, content): #
    
    queue = sqs.get_queue_by_name(QueueName='My_Queue') #The SQS queue is retrieve using the sqs. method.
    
    time = datetime.now().strftime('%Y-%m-%d %H:%M:%S') #The current date and time is obtained in a string format. 
    
    message = ('The actual time and date when this SQS queue was created was: ' + time) #We will create a custom message variable with the actual time.
    
    response = queue.send_message( MessageBody=message) #A custom message is send to the queue by using the send_message method with the message variable previosuly created. 
    
    return {'statusCode': 200, 'body': json.dumps(message)} #The function will return a status code 200 in case of sucess.   

