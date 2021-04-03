#!/bin/bash

set -euo pipefail

echo "[...] Deploying cloud formation stack: $1 from $2";


if [ -z "$1" ] && [ -z $2"" ]; then
    echo "No template or stack name passed"
    exit 1
fi

cfn-lint $2

aws cloudformation deploy --stack-name $1 --template-file $2