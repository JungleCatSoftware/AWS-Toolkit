# AWS-Toolkit
Tools for generating and bootstrapping EC2 AMIs

When used as below, the launched instance will download a release of
this repository and use it to load a base configuration and save it
as an AMI.

## IAM Role
When using these scripts to create AMIs, they must be granted a role
with access to the following actions:

- ec2:CreateImage

## How to Use
There are two methods for using this code to bootstrap your EC2 AMIs.

### Full User Data
The complete contents of the `UserData` script can be pasted into the
"User data" section under "Advanced Details" on the "Configure
Instance Details" step when launching a new EC2 instance.

### Curl
The following short script can be used in your instance's "User data"
instead of the full `UserData` script and will download and execute
the most recent version of the `UserData` script automatically and
will ensure that the most recent release archive from GitHub is used.

```bash
#!/bin/bash
curl -L https://raw.githubusercontent.com/JungleCatSoftware/AWS-Toolkit/master/UserData | /bin/bash
```
