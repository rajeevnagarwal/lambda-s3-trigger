import boto3;
if __name__=="__main__":
    ec2 = boto3.resource("ec2",endpoint_url="http://localhost:4597",aws_secret_access_key="abc",aws_access_key_id="abc",region_name="us-east-1")
    instances = ec2.instances.all()
    for instance in instances:
        print("CPU Options ",instance.cpu_options)
        print("IAM profile attached ",instance.iam_instance_profile)
        print("AMI ",instance.image)
        print("Rebooting instance")
        instance.reboot()
    
