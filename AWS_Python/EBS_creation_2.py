import boto3

ec2_client = boto3.client('ec2')

response = ec2_client.create_volume(AvailabilityZone= 'us-east-2c',
Encrypted=True,
Size=12,
SnapshotId= 'snap-07d2561d49f3aea09',
VolumeType= 'gp2')

print(response)