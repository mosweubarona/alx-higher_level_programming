#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status
"""


if __name__ == "__main__":
    import requests

    url = "https://intranet.hbtn.io/status"
    X = requests.get(url)

    print("Body response:")
    print("\t- type: {}".format(type(X.text)))
    print("\t- content: {}".format(X.text))
