#!/usr/bin/python3

"""
takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8).
"""
import sys
import urllib.request
import urllib.error

if __name__ == "__main__":
    url = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.URLError as e:
        print("Error code: {}".format(e.code))
