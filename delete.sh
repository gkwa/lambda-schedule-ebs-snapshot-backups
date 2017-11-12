#!/usr/bin/env bash

aws lambda delete-function \
  --function-name ebs-snapshot-backups \
  --region us-east-2
