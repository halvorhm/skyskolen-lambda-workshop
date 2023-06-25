import boto3
from botocore.exceptions import ClientError

def addData(event, context):

    s3 = boto3.client('s3')

    binaryData = b'binary data that was in my bucket'

    bucketString = 'testing-trigger-on-add-data-bucket'

    testKey = 'testKey'

    s3.put_object(Body=binaryData, Bucket = bucketString, Key=testKey)

    
    obj = s3.get_object(Bucket = bucketString, Key = testKey)

    result = obj['Body'].read().decode('utf-8')

    print(result)

def triggerOnAddData(ecent, context):
    print("Someone just added data to your bucket!")