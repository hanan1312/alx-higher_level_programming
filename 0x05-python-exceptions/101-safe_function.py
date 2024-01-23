#!/usr/bin/python3
import sys
def safe_function(fct, *args):
    try:
        tmp = fct(*args)
        return tmp
    except Exception as ex:
        print(f"Exception: {ex}", file=sys.stderr)
        return None
