#!/usr/bin/python3
"""defines a class Mylist"""


class MyList(list):
    """creates a class called mylist"""

    def print_sorted(self):
        """writes a class that inherits from list"""
        print(sorted(self))
