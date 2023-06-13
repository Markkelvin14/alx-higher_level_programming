#!/usr/bin/python3
"""retruns the dictionary description"""


def class_to_json(obj):
    """return the dictionary description with simple data struct"""
    return obj.__dict__
