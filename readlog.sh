#!/usr/bin/env bash

cat awsstdout.json | jq --raw-output .LogResult | base64 --decode
