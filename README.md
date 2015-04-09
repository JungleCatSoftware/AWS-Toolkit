# AWS-Toolkit
Tools for generating and bootstrapping EC2 AMIs

When used as described below, the launched instance will download a
release or branch of this repository and use it to load a base
configuration and save it as an AMI in your AWS account.

This allows for automation of installing core tools and dependencies
needed in order to spin up application VMs in your EC2 environment. By
default, the scripts in this repository are made to update a stock
Ubuntu image, install Python 3.0 and pip, Puppet, and AWS command-line
tools.

## IAM Role
When using these scripts to create AMIs, the instance must be granted
a role with access to the following actions:

- ec2:CreateImage
- ec2:DescribeImages

## How to Use
Below are two methods for using this repo to bootstrap your EC2 AMIs.
For both methods, the instance must be given access to create an image
(see the "IAM Role" section above), and it is recommended to set the
instance's shutdown behavior to "Terminate" to allow the instance to
terminate itself and prevent additonal EC2 charges once the script
has finished configuring itself and kicked off the AMI generation.

### Full User Data
The complete contents of the `UserData` script can be pasted into the
"User data" section under "Advanced Details" on the "Configure
Instance Details" step when launching a new EC2 instance. This also
offers the greatest amount of control, allowing the script to be
modified to tweek tarball download settings.

### Curl
The following short script can be used in your instance's "User data"
instead of the full `UserData` script and will download and execute
the most recent version of the `UserData` script automatically and
will ensure that the most recent release archive from GitHub is used.
The URL can be modified to point to branches or tags other than
"master".

```bash
#!/bin/bash
curl -L https://raw.githubusercontent.com/JungleCatSoftware/AWS-Toolkit/master/UserData | /bin/bash
```
