#!/usr/bin/python3
"""Defines square class"""


class Square:
    """Implimentation"""

    def __init__(self, size=0):
        """initiazing"""
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
