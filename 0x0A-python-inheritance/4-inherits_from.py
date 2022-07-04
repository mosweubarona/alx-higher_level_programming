#!/usr/bin/python3
"""
This module implements  a function that returns True if the object
is an instance of a class that inherited from the specified class
"""


def inherits_from(obj, a_class) -> bool:
    """implementation
    """
    return type(obj) != a_class and issubclass(type(obj), a_class)
