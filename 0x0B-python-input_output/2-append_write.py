#!/usr/bin/python3
"""append a string"""


def append_write(filename="", text=""):
    """lappend string and return its length"""
    with open(filename, mode="a", encoding="utf-8") as fa:
        fa.write(text)
    return len(text)
