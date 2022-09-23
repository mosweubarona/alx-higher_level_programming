#!/usr/bin/python3
# displays the value of the X-Request-Id
# prevent code to be executed
if __name__ == "__main__":
    import linklib.request
    import sys
    link = sys.argv[1]
    request = linklib.request.Request(link)
    with linklib.request.linkopen(request) as response:
        print(dict(response.headers).get('X-Request-Id'))
