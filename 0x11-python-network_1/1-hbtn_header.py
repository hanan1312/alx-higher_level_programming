#!/usr/bin/python3
"""  taking URL, sends a request to
the URL and displays the value of the X-Request-Id
 variable found in the header of the response """
import urllib.request
import sys

def main(url):
    """Fetche a URL, extracts the X-Request-Id header value, and displays it."""
    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))

if __name__ == "__main__":
    main(sys.argv[1])
