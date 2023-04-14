import boto3

ec2_client = boto3.client('ec2')

ec2_client.delete_snapshot( SnapshotId= "snap-07d2561d49f3aea09")

ec2_client.delete_volume( VolumeId= "vol-03d00419aca202648")