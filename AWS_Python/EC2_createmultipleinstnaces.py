import boto3

ec2_resource=boto3.resource("ec2")
ec2_resource.create_instances(ImageId='ami-0103f211a154d64a6',
InstanceType='t2.micro',
MaxCount=5,
MinCount=3)

