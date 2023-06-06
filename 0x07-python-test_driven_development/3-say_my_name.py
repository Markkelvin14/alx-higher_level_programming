#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """prints my name is <first name> <last name>"""
    if type(first_name) is int:
        raise TypeError("first_name must be a string")
    if type(last_name) is int:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
