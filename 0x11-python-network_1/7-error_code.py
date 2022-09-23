#!/usr/bin/python3
"""takes in a URL, sends a request to the URL and
displays the body of the response.
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    X = requests.get(url)
    if X.status_code >= 400:
        print("Error code: {}".format(X.status_code))
    else:
        print(X.text
