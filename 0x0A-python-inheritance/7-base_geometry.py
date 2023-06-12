#!/usr/bin/python3
"""represent a class"""


class BaseGeometry:
    """create a class BaseGeometry"""

    def area(sel):
        """define area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate the parameter of an int"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
