import boto3

client = boto3.client("ec2")

response = client.delete_vpc(
    VpcId= 'vpc-0322d34b6cebcd32b')
    
