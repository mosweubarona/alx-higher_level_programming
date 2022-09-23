#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status
"""
import requests

if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    X = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(X.text)))
    print("\t- content: {}".format(X.text))
