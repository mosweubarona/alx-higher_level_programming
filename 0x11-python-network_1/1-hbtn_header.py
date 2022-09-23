#!/usr/bin/python3
# displays the value of the X-Request-Idi


import sys
import urllib.request

if __name__ == "__main__":

    req = sys.argv[1]
    with urllib.request.urlopen(request) as response:
        print(response.headers.get("X-Request-Id"))
