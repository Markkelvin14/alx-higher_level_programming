#!/usr/bin/python3
"""a function that reads a text"""


def read_file(filename=""):
    """read a text file"""
    with open(filename, 'r', encoding="UTF8") as f:
        print(f.read(), end="")
