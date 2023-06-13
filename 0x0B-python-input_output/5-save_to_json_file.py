#!/usr/bin/python3
"""represents json"""
import json


def save_to_json_file(my_obj, filename):
    """writes an object to a textfile"""
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
