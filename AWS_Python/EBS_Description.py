import boto3

ec2_boto3 = boto3.client('ec2')

results = ec2_boto3.describe_snapshots(SnapshotIds = ['snap-04c1d481e3da310af'])

print(results)