#!/usr/bin/python3
"""Module to access to the GitHub API and uses the information"""
import requests
from requests.auth import HTTPBasicAuth
from sys import argv


if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    response = requests.get('https://api.github.com/username',
                            auth=HTTPBasicAuth(user, password))
    profile = response.jsoin()
    print(profile['id'])
