#!/usr/bin/env bash

rm -f lambda_function.zip
mkdir -p stage
# cp pingtest.py stage/lambda_function.py
cp ebs-snapshot-backups.py stage/lambda_function.py

cd stage
zip -X -r ../lambda_function.zip *
cd ..
