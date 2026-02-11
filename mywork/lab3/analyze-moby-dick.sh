#!/bin/bash

echo "$0 <-- invoking script"
echo "$1 <-- word to search"

export SEARCH_PATTERN=$1
OUTPUT="results.txt"
if [[ -z "$2" ]]; 
then
	OUTPUT="results.txt"
else
	OUTPUT=$2
fi

if [[ -f $OUTPUT ]];
then
	echo "Output File already exists: $OUTPUT"
	exit 1
fi

export OUTPUT
echo "$OUTPUT <-- output file"

export NUM_LINES=$(grep -oi "$SEARCH_PATTERN" ./mobydick.txt | wc -l)

echo "The search pattern \"$SEARCH_PATTERN\" was found $NUM_LINES time(s)." > "$OUTPUT"
