#!/usr/bin/python3
"""represents a json file"""
import json


def load_from_json_file(filename):
    """creates an object"""
    with open(filename) as f:
        return json.load(f)
