import boto3

ec2_client = boto3.client("ec2")

x = ec2_client.describe_instances()

data = x["Reservations"]


li=[]

for instances in data:
    instance=instances["Instances"]
    for ids in instance:
        instance_id=ids ["InstanceId"]
        li.append(instance_id)
        
li.remove('i-0379c6fcb869301f5')

print(li)   

response = ec2_client.terminate_instances(InstanceIds=li)

print(response)