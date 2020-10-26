# EC2 Website
## Overview

Hosts a file uploading website on two EC2 instances, fronted by an Application Load Balancer. Uploads are stored in S3 to ensure data is not lost if a server(s) fail.

## Environment

The environment has two optional parameters:
* AdminIp: Lets you to lock down access to your IP address (Default: 0.0.0.0/0)
* KeyName: Lets you to SSH into the webserver (Default: None) 

To create the environment with its default settings, run the following command:

```
aws cloudformation create-stack \
--template-body file://ec2_website_s3.yaml \
--stack-name OzNetNerd-demo-environment \
--capabilities CAPABILITY_IAM
```

To modify the default parameters, use the following command:

```
aws cloudformation create-stack \
--template-body file://ec2_website_s3.yaml \
--stack-name OzNetNerd-demo-environment \
--parameters \
ParameterKey=AdminIp,ParameterValue=<YOUR_IP_ADDRESS> \
ParameterKey=KeyName,ParameterValue=<YOUR_EC2_KEY_NAME> \
--capabilities CAPABILITY_IAM
```