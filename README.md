# AWS-Toolkit
Tools for generating and bootstrapping EC2 AMIs

## Use
Copy the contents of the `UserData` file into the User Data section
of an AWS EC2 instance's Launch Configuration. This will cause the
instance to reach out and pull the specified release archive from
GitHub and execute the contained `scripts/run` script when the
instance is booted.

Alternatively, the following can be used instead to automatically
pull the latest version:
```bash
#!/bin/bash
curl -L https://raw.githubusercontent.com/JungleCatSoftware/AWS-Toolkit/master/UserData | /bin/bash
```
