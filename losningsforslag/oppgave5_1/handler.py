import boto3
from botocore.exceptions import ClientError

def printBuckets(event, context):

    # Retrieve the list of existing buckets
    s3 = boto3.client('s3')
    response = s3.list_buckets()

    # Output the bucket names
    print('Existing buckets:')
    for bucket in response['Buckets']:
        print(f'  {bucket["Name"]}')


    binaryData = b'binary data that was in my bucket'

    bucketString = 'testingtasks-dev-serverlessdeploymentbucket-1w35tb9hjmwjl'

    testKey = 'testKey'

    # put data in a given bucket
    s3.put_object(Body=binaryData, Bucket = bucketString, Key=testKey)

    # get data by key from a bucket
    obj = s3.get_object(Bucket = bucketString, Key = testKey)

    result = obj['Body'].read().decode('utf-8')

    print(result)