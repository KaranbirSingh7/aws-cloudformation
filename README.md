# aws-cloudformation

Repo to contain commonly used AWS CloudFormation templates

### Installation

```bash
#deploy script uses cfn-lint to lint template

pip3 install cfn-lint

```

### Provisioning

```bash
# SAMPLE USAGE: ./deploy.sh codecommit-stack ./codecommit/cloudformation.yml

./deploy.sh $STACK_NAME $TEMPLATE_FILE_PATH
```
