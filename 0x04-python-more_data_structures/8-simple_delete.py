#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if key != "":
        new_dictionary = {}
        for k, v in a_dictionary.items():
            if k != key:
                new_dictionary[k] = v
        return new_dictionary
    else:
        return a_dictionary
