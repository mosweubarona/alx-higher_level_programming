#!/usr/bin/python3
# displays the value of the X-Request-Id
import urllib.request
import sys
# prevent code to be executed
if __name__ == "__main__":
    with request.urlopen(sys.argv[1]) as reply:
        print(reply.info()['X-Request-Id'])
