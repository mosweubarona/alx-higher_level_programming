#!/usr/bin/python3
"""
This module implements a Rectangle object
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        """initialisation of rectangle class

        Args:
            width (int): width
            height (int): height
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """method that returns area

        Returns:
            int: response
        """
        return self.__width * self.__height

    def __str__(self):
        """method that returns string

        Returns:
            str: string representation
        """
        string = "[" + str(self.__class__.__name__) + "]"
        string += str(self.__width) + "/" + str(self.__height)
        return string
