#!/usr/bin/python3
# displays the value of the X-Request-Id
# prevent code to be executed
if __name__ == "__main__":
    import urllib.request
    import sys
    with urllib.request.urlopen(sys.argv[1]) as reply:
        response = reply.headers.get('X-Request-Id')
        print(response)
