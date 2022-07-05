#!/usr/bin/python3
"""save to file"""
import json
"""get json module"""


def save_to_json_file(my_obj, filename):
    """save to json file"""
    with open(filename, mode="w", encoding="utf-8") as sv:
        """save file to sv"""
        sv.write(json.dumps(my_obj))
