#!/usr/bin/python3
"""defines a class Mylist"""


class Mylist(list):
    """creates a class called mylist"""

    def print_sorted(self):
        """writes a class that inherits from list"""
        print(sorted(self))
