#!/usr/bin/env bash

aws lambda invoke \
  --function-name ebs-snapshot-backups \
  --invocation-type RequestResponse \
  --region us-east-2 \
  --log-type Tail \
  --payload '{"key1":"value1", "key2":"value2", "key3":"value3"}' \
  --profile general \
  outputfile.txt >awsstdout.json
