import boto3
import json
client = boto3.client("sqs")
test_queue_url = "https://sqs.us-east-1.amazonaws.com/844205617614/lambda-s3-trigger-testqueue6060C692-1XKN9XW50CNJT"
def main(event,context):
    client.send_message(QueueUrl=test_queue_url,MessageBody=json.dumps(event))
    return {
        'statusCode':200,
        'body':event
        }