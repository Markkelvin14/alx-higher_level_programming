#!/usr/bin/python3
"""Defines a function that adds attributes to objects."""


def add_atitribute(obj, atri, value):
    """Add a new attribute to an object if possible."""

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, atri, value)
