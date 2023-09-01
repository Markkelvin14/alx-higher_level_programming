#!/usr/bin/python3
''' displays value of X-Request_Id in response header  '''
import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    req = requests.get(url)
    print(req.headers.get('X-Request-Id'))
