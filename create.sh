#!/usr/bin/env bash

aws lambda create-function \
  --handler lambda_function.lambda_handler \
  --role arn:aws:iam::${ACCOUNT_ID}:role/ebs-backup-worker \
  --runtime python3.6 \
  --region us-east-2 \
  --zip-file fileb://lambda_function.zip \
  --function-name ebs-snapshot-backups \
  --timeout $((2*60)) \
  --memory-size 128
