import boto3;
if __name__=="__main__":
    s3 = boto3.resource("s3",endpoint_url="http://localhost:4572",aws_secret_access_key="abc",aws_access_key_id="abc")
    print("Creating bucket with name myBucket")
    s3.create_bucket(Bucket='myBucket')
    print("Fetching bucket resource")
    bucket = s3.Bucket('myBucket')
    print(bucket.name)
    print("Uploading sample file to bucket")
    bucket.upload_file('sample.txt','sample.txt')
    print("Uploading cloudformation template to bucket")
    bucket.upload_file('cloudformation_ec2.yaml','cloudformation_ec2.yaml')
    bucket.download_file('sample.txt','sample.txt')
    for bucket in s3.buckets.all():
        print("Name ",bucket.name)
        print("Creation Date",bucket.creation_date)

    