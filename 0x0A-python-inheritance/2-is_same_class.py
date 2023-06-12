#!/usr/bin/python3
"""defines the object"""


def is_same_class(obj, a_class):
    """Returns true if object is an instance, false otherwise"""

    if not isinstance(obj, a_class):
        return False
    return True
