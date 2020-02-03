import boto3
if __name__=="__main__":
    cloudformation = boto3.resource("cloudformation",endpoint_url="http://localhost:4581",aws_secret_access_key="abc",aws_access_key_id="abc",region_name="us-east-1")
    result = ""
    with open("cloudformation_ec2.yaml",'r') as file:
        for line in file:
            result = result + line
    print(result)
    print("Creates a stack single ec2 instance with a security group")
    cloudformation.create_stack(StackName="stack0",TemplateBody=result)
