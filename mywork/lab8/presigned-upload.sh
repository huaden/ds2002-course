#!/bin/bash

LOCAL_FILE=$1
BUCKET_NAME=$2
EXPIRATION=$3

if [ -z "$LOCAL_FILE" ] || [ -z "$BUCKET_NAME" ] || [ -z "$EXPIRATION" ]; then
    echo "Usage: $0 <local-file> <bucket-name> <expiration-seconds>"
    exit 1
fi

aws s3 cp "$LOCAL_FILE" "s3://$BUCKET_NAME/$LOCAL_FILE"
aws s3 presign "s3://$BUCKET_NAME/$LOCAL_FILE" --expires-in "$EXPIRATION"