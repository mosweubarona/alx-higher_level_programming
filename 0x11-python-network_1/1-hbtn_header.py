#!/usr/bin/python3
# displays the value of the X-Request-Idi


import urllib.request
import sys


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        req = response.info()
        print(req.get('X-Request-Id'))
