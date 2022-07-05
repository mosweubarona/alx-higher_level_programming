#!/usr/bin/python3
"""a json"""


class Student:
    """clas for student."""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of a Student instance."""
        if attrs is not None and all(isinstance(x, str) for x in attrs):
            a = {}
            for b, c in self.__dict__.items():
                if b in attrs:
                    a[b] = c
            return a
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """get data from json via reload"""
        for (key, value) in json.items():
            setattr(self, key, value)
