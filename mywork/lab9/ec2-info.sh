#!/bin/bash

module load miniforge
source activate ds2002

aws ec2 describe-instances | jq '.Reservations[].Instances[] | {
  ImageId,
  InstanceId,
  InstanceType,
  InstanceName: (.Tags[]? | select(.Key=="Name") | .Value),
  PublicIpAddress: (.PublicIpAddress),
  State
}'