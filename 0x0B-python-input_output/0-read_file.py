#!/usr/bin/python3
"""to read a fill"""


def read_file(filename=""):
    """function to read file"""
    with open (filename, encoding="utf-8") as r:
            print(r.read(), end="")
