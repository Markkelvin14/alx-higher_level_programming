#!/usr/bin/python3
"""represent a class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square:
    """create a classs sttring"""

    def __init__(self, size):
        """initalise a new square"""

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
