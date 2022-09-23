#!/usr/bin/python3
# displays the value of the X-Request-Idi


if __name__ == "__main__":
    import sys
    import urllib.request

    req = sys.argv[1]
    with urllib.request.urlopen(req) as response:
        print(response.info()['X-Request-Id'])
