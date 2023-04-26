# Import the Boto3 library
import boto3

# Connect to the SQS
sqs = boto3.resource('sqs')

# Create the queue with its name
queue = sqs.create_queue(QueueName='My_Queue')

# Print the URL of the queue
print(queue)