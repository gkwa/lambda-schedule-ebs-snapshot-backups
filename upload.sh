#!/usr/bin/env bash

aws lambda update-function-code \
  --region us-east-2 \
  --function-name ebs-snapshot-backups \
  --zip-file fileb://lambda_function.zip
