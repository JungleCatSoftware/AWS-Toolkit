# AWS-Toolkit
Tools for generating and bootstrapping EC2 AMIs

When used as described below, the launched instance will download a
release or branch of this repository and use it to load a base
configuration and save it as an AMI in your AWS account. It will also
install a FirstBoot cronjob to execute `scripts/global/doFirstBoot`
on boot of any Instances created from the AMI. Currently FirstBoot
only removes itself so it does not run on subsequent reboots.

This allows for automation of installing core tools and dependencies
needed in order to spin up application VMs in your EC2 environment. By
default, the scripts in this repository are made to update a stock
Ubuntu image, install Python 3.0 and pip, Puppet, and AWS command-line
tools. It also prepares the AMI for auto-configuration of Images
built from it.

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

## Booting From Generated AMI
After generating the AMI using the above methods, it can now be launched
with Instance User Data to define how configuration should be started. At
present, configuration information must be passed in as a JSON document
at instance launch.

For example, the following User Data can be passed in at launch to install
a basic Apache web server:

```json
{
    "options": {
        "tool": "puppet",
        "script": "include ::apache",
        "dependancies": {
            "concat": {
                "type": "puppet-forge",
                "source": "puppetlabs-concat"
            },
            "puppetlabs-apache-2.0.0": {
                "type": "puppet-tarball",
                "source": "https://github.com/puppetlabs/puppetlabs-apache/archive/2.0.x.tar.gz",
                "ignore-dependencies": "True"
            }
        }
    }
}
````

### Configuration Options
This section will cover the values that can be passed to the instance when
launched

#### tool
Supported values: puppet, shell

- shell: run the contents of `script` with `/bin/bash`. It is not recommended
  to use this tool other than for testing.
- puppet: treat the contents of `script` as a Puppet manifest and will run
  using `/usr/bin/puppet apply`. This is the recommended tool.

#### script
These are the commands to run on boot. This script should be as minimal as
possible, ideally a single line, such as an import for a single Puppet
class (such as a specific role if using the profiles and roles pattern).

#### dependencies
This is a hash of dependencies to retrieve prior to script execution. It
consists of the dependency name, followed by a hash of it's configuration
information.

##### type
Supported values: puppet-forge, puppet-tarball

- puppet-forge: download and install the module named in "source" from
  https://forge.puppet.com/
- puppet-tarball: download and install the tarballed module from the URL
  "source". The tarball will be named as the dependency name, so be aware
  that earlier versions of Puppet will expect the username and version to
  be present in this name. (later Puppet versions use the metadata.json to
  get this information)

##### source
The source of the dependency. For puppet-forge this is the module's name/id,
for puppet-tarball this is the URL to download the tarball from.

##### ignore-dependencies
Only applies to "puppet-" types. Valid values are the strings "True" and
"False" (assumes "False" otherwise). This controls whether the Puppet module
install should automatically retrieve dependencies from the Puppet Forge. This
should be left as the default when downloading modules from the Forge, but
should be set to True if downloading module tarballs for modules not present
on the Forge (such as custom modules on GitHub)
