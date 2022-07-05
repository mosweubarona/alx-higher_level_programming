#!/usr/bin/python3
"""json to object"""
import json
"""get json"""


def load_from_json_file(filename):
    """get file from json"""
    with open(filename, encoding="utf-8") as sv:
        return json.loa(sv)
