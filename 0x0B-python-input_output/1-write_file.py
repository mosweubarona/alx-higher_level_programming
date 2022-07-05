#!/usr/bin/python3
"""to write a file"""


def write_file(filename="", text=""):
    """write strring to text fle"""
    with open(filename, mode="w", encoding="utf-8") as fw:
        fw.write(text)
    return len(text)
