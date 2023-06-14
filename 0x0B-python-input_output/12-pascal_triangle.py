#!/usr/bin/python3
"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """creates a Pascal Triangle of size n.
    Returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    triang = [[1]]
    while len(triang) != n:
        tri = triang[-1]
        tmp_ang = [1]
        for m in range(len(tri) - 1):
            tmp_ang.append(tri[m] + tri[m + 1])
        tmp_ang.append(1)
        triang.append(tmp_ang)
    return triang
