from helpers import *  # Importing all helper functions (should ideally import only what's needed for clarity and maintainability)

def create_instances(ec2_client: object, ami_type: str = "ubuntu", instance_amount: int = 1) -> None:
    """
    Creates EC2 instances based on the specified AMI type and instance amount.

    Args:
        ec2_client (object): The EC2 client object used to interact with AWS EC2.
        ami_type (str): The type of AMI to use for the instance. Defaults to "ubuntu".
                        Supported values are "ubuntu", "linux 2023", and "linux 2".
        instance_amount (int): The number of instances to create. Defaults to 1.

    Returns:
        None: This function does not return a value.
    """
    for i in range(instance_amount):
        # Normalize and validate AMI type input
        if ami_type.lower().strip() == "ubuntu":
            create_ubuntu_instance(ec2_client)  # Helper function to create an Ubuntu instance
            print("Ubuntu Created")
        elif ami_type.lower().strip() == "linux 2023":
            create_amazon_linux_2023_instance(ec2_client)  # Helper function to create Amazon Linux 2023 instance
            print("Linux 2023 Created")
        elif ami_type.lower().strip() == "linux 2":
            create_amazon_linux_2_instance(ec2_client)  # Helper function to create Amazon Linux 2 instance
            print("Linux 2 Created")
        else:
            print("Unsupported AMI")  # Handle unsupported AMI types

if __name__ == '__main__':
    ec2_client = get_ec2_client()  # Obtain the EC2 client object
    create_instances(ec2_client, "linux 2", 3)  # Create 3 instances with Linux 2 AMI
    create_instances(ec2_client, ami_type="liNux 2023 ")  # Create 1 instance with Linux 2023 AMI (default instance_amount)
    create_instances(ec2_client, instance_amount=2)  # Create 2 instances with the default Ubuntu AMI
