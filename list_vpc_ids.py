import boto3  # Import Boto3 to interact with AWS services

# Create an EC2 client to interact with VPCs
vpc_client = boto3.client('ec2')

# Fetch details of all VPCs in the account
response = vpc_client.describe_vpcs()

# Extract the list of VPCs from the response
vpcs = response['Vpcs']

# Print the VPC ID of each VPC
for vpc in vpcs:
    print(vpc['VpcId'])
