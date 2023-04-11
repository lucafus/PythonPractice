import boto3

s3 = boto3.client('s3')

response = client.delete_bucket(
    Bucket='cf-templates-na5to0vok5g9-us-east-1',
    )