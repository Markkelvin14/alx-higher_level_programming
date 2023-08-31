#!/bin/bash
# Script that takes in a URL and displays all HTTP methods the server will accpt
curl -sI "$1" | grep "Allow" | awk -F ": " '{ print $2 }'
