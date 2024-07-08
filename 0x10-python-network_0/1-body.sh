#!/bin/bash

if [ $# -ne 1 ]; then
  echo "$0 <URL>"
  exit 1

fi

URL=$1

response=$(curl -s -o /dev/null -w "%{http_code}" "$URL")
if [ "$response" -ne 200 ]; then
  echo "Error: Unexpected HTTP status code $response"
  exit 1

fi

curl -s "$URL"
echo "" 
