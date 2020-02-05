#!/usr/bin/env python3

from aws_cdk import core

from lambda_s3_trigger.lambda_s3_trigger_stack import LambdaS3TriggerStack


app = core.App()
LambdaS3TriggerStack(app, "lambda-s3-trigger")

app.synth()
