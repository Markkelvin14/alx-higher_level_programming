#!/bin/bash
# sends a request and displays only status code of response
curl -so /dev/null -w "%{http_code}" "$1"
