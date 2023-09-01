#!/usr/bin/python3
'''  sends a POST request to passed URL and displays response  '''
import urllib.request as request
from sys import argv
import urllib.parse as parse


if __name__ == "__main__":
    url = argv[1]
    data = {'email': argv[2]}
    data = parse.urlencode(data)
    data = data.encode('utf8')
    req = request.Request(url, data)
    with utllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
