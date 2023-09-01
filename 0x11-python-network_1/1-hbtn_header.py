#!/usr/bin/python3
"""a Python script that takes in a URL, sends a request"""
import urllib.request
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    with urllib.request.urlopen(url) as response:
        print(response.headers.get('X-Request-id'))
