#!/usr/bin/python3
"""function that writes a string"""


def write_file(filename="", text=""):
    """write a string to a text file

    filename is name of file
    text is the text to be written in file
    """
    with open(filename, 'w', encoding="UTF8") as f:
        return f.write(text)
