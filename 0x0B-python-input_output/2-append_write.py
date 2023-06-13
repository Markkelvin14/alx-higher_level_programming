#!/usr/bin/python3
"""function that appends a string"""


def append_write(filename="", text=""):
    """append a string at the end of a textfile"""
    with open(filename, 'a', encoding="UTF8") as f:
        return f.write(text)
