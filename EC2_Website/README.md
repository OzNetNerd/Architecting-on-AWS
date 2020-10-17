# EC2 Website
## Overview

Hosts a file uploading website on an EC2 instance. 

## Environment

The environment has two optional parameters:
* AdminIp: Lets you to lock down access to your IP address (Default: 0.0.0.0/0)
* KeyName: Lets you to SSH into the webserver (Default: None) 

To create the environment with its default settings, run the following command:

```
aws cloudformation create-stack \
--template-body file://ec2_website.yaml \
--stack-name OzNetNerd-demo-environment
```

To modify the default parameters, use the following command:

```
aws cloudformation create-stack \
--template-body file://ec2_website.yaml \
--stack-name OzNetNerd-demo-environment \
--parameters \
ParameterKey=AdminIp,ParameterValue=<YOUR_IP_ADDRESS> \
ParameterKey=KeyName,ParameterValue=<YOUR_EC2_KEY_NAME>
```