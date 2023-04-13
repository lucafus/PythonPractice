import boto3

client= boto3.client("ec2")

response = client.describe_vpcs()


number_ofVPCS = response["Vpcs"]


lenght = len(number_ofVPCS)

for vpc in number_ofVPCS:
    print(vpc["VpcId"])