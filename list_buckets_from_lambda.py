import json
import boto3  # Import the AWS SDK for Python (Boto3)

def lambda_handler(event, context):
    # Create an S3 client to interact with the AWS S3 service
    s3 = boto3.client('s3')

    # List all the buckets in the AWS account using the S3 client
    response = s3.list_buckets()

    # Extract the list of buckets from the response
    buckets = response["Buckets"]

    bucket_names = []  # Initialize an empty list to store bucket names

    # Iterate over each bucket in the list of buckets
    for bucket in buckets:
        # Print the name of the bucket
        print(bucket["Name"])
        bucket_names.append(bucket["Name"])  # Add the bucket name to the list

    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps(bucket_names)
    }
