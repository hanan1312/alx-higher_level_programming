#!/usr/bin/python3
for str_c in range(ord('a'), ord('z') + 1):
    if chr(str_c) not in ["q", "e"]:
        print("{}".format(chr(str_c)), end='')
