from aws_cdk import (
    aws_lambda as _lambda,
    aws_s3 as s3,
    aws_s3_notifications,
    aws_sqs as sqs,
    core
)


class LambdaS3TriggerStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        function = _lambda.Function(self, "lambda_function", runtime=_lambda.Runtime.PYTHON_3_7,
                                    handler="lambda-handler.main", code=_lambda.Code.asset("./lambda"))

        s3_bucket = s3.Bucket(self, "s3Bucket")
        notification = aws_s3_notifications.LambdaDestination(function)

        s3_bucket.add_event_notification(s3.EventType.OBJECT_CREATED, notification)

        queue = sqs.Queue(self, "test_queue")

        queue.grant_send_messages(function)
        # The code that defines your stack goes here
