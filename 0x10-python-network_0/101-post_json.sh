#!/bin/bash
# sends JSON POST request and displays body of response
curl -s -H "Content-Type: application/json" -d @"$2" "$1"
