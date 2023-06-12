#!/usr/bin/python3
"""define a function"""


def is_kind_of_class(obj, a_class):
    """Returns true if obj is an instance

    return:
        true if obj is an instance
        false if not
    """
    if isinstance(obj, a_class):
        return True
    return False
