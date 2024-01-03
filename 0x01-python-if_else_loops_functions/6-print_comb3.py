#!/usr/bin/python3

for no_1 in range(0, 10):
    for no_2 in range(no_1 + 1, 10):
        if no_1 == 8 and no_2 == 9:
            print("{}{}".format(no_1, no_2))
        else:
            print("{}{}".format(no_1, no_2), end=", ")
