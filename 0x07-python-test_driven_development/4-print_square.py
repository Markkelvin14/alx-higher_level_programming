#!/usr/bin/python3
def print_square(size):
    """prints a square with the character #
    size is the argument provide
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")

    for m in range(size):
        [print("#", end="") for k in range(size)]
        print("")
