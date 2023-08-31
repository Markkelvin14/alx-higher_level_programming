#!/usr/bin/python3
"""Module to find the hightest number(peak) in an list"""


def find_peak(list_of_integers):
    """Method to find hightest number"""
    if not list_of_integers:
        return None
    list_of_integers.sort()
    return list_of_integers[-1]
