#!/usr/bin/python3
def safe_print_division(a, b):
    tmp = None
    try:
        tmp = a/b
    except:
        pass
    finally:
        print("Inside result: {}".format(tmp))
    return tmp
