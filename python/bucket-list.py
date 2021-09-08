import boto3

s3 = boto3.client("s3")

for bucket in s3.list_buckets()["Buckets"]:
    if s3.head_bucket(Bucket=bucket['Name'])['ResponseMetadata']['HTTPHeaders']['x-amz-bucket-region'] == 'us-east-1':
        print(bucket["Name"])
