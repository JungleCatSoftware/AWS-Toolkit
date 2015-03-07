# AWS-Toolkit
Tools for generating and bootstrapping EC2 AMIs

## Use
Copy the contents of UserData.sh into the user data section of the AWS EC2 instance's Launch Configuration. This will cause the instance to reach out and pull the specified release archive from GitHub and execute the contained Configure.sh script when the instance is booted.
