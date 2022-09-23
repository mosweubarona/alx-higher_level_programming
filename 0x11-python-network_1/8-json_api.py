#!/usr/bin/python3
"""Python script that takes in a letter and
sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter
"""


import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) > 1:
        arg = sys.argv[1]
    else:
        arg = ""
        payload = {'q': arg}
        r = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        r.raise_for_status()
        json = r.json()
        if len(json) == 0:
            print("No result")
        else:
            print("[{:d}] {}".format(json['id'], json['name']))
    except Exception:
        print("Not a valid JSON")
