#!/bin/bash
# sends a POST request and displays body of response
curl -sX POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
