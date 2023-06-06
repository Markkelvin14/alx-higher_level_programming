#!/usr/bin/python3
"""addition of two ints"""


def add_integer(a, b=98):
    """this function adds two integers
    converts them to ints incase they are floats
    and if the arguments are not int or floats it raises a Type error

    raises a typeerror excetion message

    float args are changed to int
    """

    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
