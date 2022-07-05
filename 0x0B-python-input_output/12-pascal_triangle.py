#!/usr/bin/python3
"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n."""

    if n <= 0:
        return []

    pascal = [[1]]
    while len(pascal) != n:
        tri = pascal[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])
        tmp.append(1)
        pascal.append(tmp)
    return pascal
