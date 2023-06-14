#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """initalize a new student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of the Student."""

        if (type(attrs) is list and
                all(type(elements) is str for elements in attrs)):
            return {m: getattr(self, m) for m in attrs if hasattr(self, m)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student."""
        for m, k in json.items():
            setattr(self, m, k)
