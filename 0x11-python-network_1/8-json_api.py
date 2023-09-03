#!/usr/bin/python3
''' sends a post request with a given letter as a parameter  '''
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) < 2:
        q = ""
    else:
        q = argv[1]
    url = 'http://0.0.0.0:5000/search_user'
    data = {'q': q}
    try:
        req = requests.post(url, data=data).json()
        if 'id' in req and 'name' in req:
            print("[{}] {}".format(req['id'], req['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
