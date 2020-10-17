# Base Infrastructure
## Overview

Creates base infrastructure. 

## Environment

To create the environment, run the following command:

```
aws cloudformation create-stack \
--template-body file://base_infrastructure.yaml \
--stack-name OzNetNerd-demo-environment
```