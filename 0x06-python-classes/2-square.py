#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """show the square"""

    def __init__(self, size=0):
        """initialise the size"""

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
