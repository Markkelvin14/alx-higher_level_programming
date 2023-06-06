#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    """prevent the user creating a new instance unless
    its a new instance called first_name
    """

    __slots__ = ["first_name"]
