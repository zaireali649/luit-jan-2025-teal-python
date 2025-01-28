import boto3  # Import the AWS SDK for Python (Boto3)

# Create an S3 client to interact with the AWS S3 service
s3 = boto3.client('s3')

# List all the buckets in the AWS account using the S3 client
response = s3.list_buckets()

# Extract the list of buckets from the response
buckets = response["Buckets"]

# Iterate over each bucket in the list of buckets
for bucket in buckets:
    # Print the name of the bucket
    print(bucket["Name"])
