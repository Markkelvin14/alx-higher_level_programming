#!/usr/bin/python3
"""defines a student"""


class Student:
    """define a class"""

    def __init__(self, first_name, last_name, age):
        """initalise a new student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns a dictionary rep of a student"""
        if (type(attrs) is list and
                all(type(elements) is str for elements in attrs)):
            return {m: getattr(self, m) for m in attrs if hasattr(self, m)}
        return self.__dict__
