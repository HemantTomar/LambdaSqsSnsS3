import json
import boto3


def lambda_handler(event, context):
    s3=boto3.client("s3")
    data=json.loads(event["Records"][0]["body"])
    s3.put_object(Bucket="targetbucket-01",Key="data.json",Body=json.dumps(data))
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
