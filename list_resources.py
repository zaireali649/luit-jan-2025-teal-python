from helpers import get_s3_client, get_ec2_client, list_buckets, describe_instances  # Import helper functions

from typing import List, Any  # For type hinting

def print_bucket_names(s3_client: Any) -> None:
    """
    Fetch and print the names of all S3 buckets.

    Args:
        s3_client (Any): An S3 client object used to interact with AWS S3.
    """
    bucket_names: List[str] = list_buckets(s3_client)  # Fetch bucket names using the helper function
    for bucket_name in bucket_names:  # Iterate over each bucket name
        print(bucket_name)  # Print the bucket name


def print_instance_ids(ec2_client: Any) -> None:
    """
    Fetch and print the instance IDs of all EC2 instances.

    Args:
        ec2_client (Any): An EC2 client object used to interact with AWS EC2.
    """
    instances: List[dict] = describe_instances(ec2_client)  # Fetch instance details using the helper function

    instance_ids: List[str] = []  # Initialize a list to store instance IDs
    for instance in instances:  # Iterate over each instance
        instance_ids.append(instance['InstanceId'])  # Append the instance ID to the list

    for instance_id in instance_ids:  # Iterate over the list of instance IDs
        print(instance_id)  # Print each instance ID


if __name__ == '__main__':
    # Initialize AWS clients
    ec2_client = get_ec2_client()  # Get the EC2 client
    s3_client = get_s3_client()  # Get the S3 client

    # Print bucket names
    print_bucket_names(s3_client)

    # Print EC2 instance IDs
    print_instance_ids(ec2_client)
