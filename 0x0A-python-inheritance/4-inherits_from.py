#!/usr/bin/python3
"""defines a function"""


def inherits_from(obj, a_class):
    """returns true if the object is an instance

    return:
        true if obj is instance
        false otherwise
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
