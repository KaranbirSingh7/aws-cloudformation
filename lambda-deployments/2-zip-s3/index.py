import boto3
from datetime import datetime

# Create an S3 client
s3 = boto3.client('s3')

def handler(event, context):
    # Call S3 to list current buckets
    response = s3.list_buckets()

    # Get a list of all bucket names from the response
    buckets = [bucket['Name'] for bucket in response['Buckets']]

    # Print out the bucket list
    print("This is another change I made")
    print(datetime.now())
    print("Bucket List: %s" % buckets)

    return buckets