#!/usr/bin/python3
"""script that takes 2 arguments in order to
solve this challenge.
"""
import sys
import requests

def main(url):
    response = requests.get(url)
    commits = response.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

