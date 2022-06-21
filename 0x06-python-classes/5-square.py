#!/usr/bin/python3
"""Defines square class"""


class Square:
    """Implimentation"""

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        return (self.__size ** 2)

    def my_print(self):
        if (self.__size == 0):
            print('')

            for l in range(self.__size):
                print('#' * self.__size)
