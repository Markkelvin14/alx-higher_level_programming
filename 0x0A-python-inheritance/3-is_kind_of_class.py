#!/usr/bin/python3
"""define a function"""


def is_kind_of_class(obj, a_class):
    """Returns true if obj is an instance"""
    if type(obj) is a_class:
        return True
    return False
