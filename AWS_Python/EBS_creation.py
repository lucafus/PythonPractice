import boto3

ec2_client = boto3.client('ec2')

ec2_client.create_snapshot (Description='Snapshot',
VolumeId='vol-03e5087679e54f4b4')