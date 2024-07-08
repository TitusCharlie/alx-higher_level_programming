#!/bin/bash

if [$# -ne 1]; then
	echo "Usage: $0 <URL>"
	exit 1
fi

#Capture the URL from the first argument
URL=$1

#Send a GET request using curl, suppress output,and get the size of the response

size=$(curl -sI "$URL" | grep -i Content-Length | awk '{print $2}')

#Display the size of the response body
echo "$size" 
