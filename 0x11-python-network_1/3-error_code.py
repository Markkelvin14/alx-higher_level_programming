#!/usr/bin/python3
'''  takes in a url, sends a request, and displays the response '''


import urllib.request
from sys import argv
import urllib.error as error


if __name__ == "__main__":
    url = argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as erre:
        print("Error code: {}".format(erre.code))
