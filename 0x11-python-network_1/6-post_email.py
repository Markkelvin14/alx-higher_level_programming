#!/usr/bin/python3
''' sends a POST request to passed URL with given email address '''
import requests
from sys import argv


if __name__ == "__main__":
    val = {'email': argv[2]}
    url = argv[1]
    req = requests.post(url, data=val)
    print(req.text)
