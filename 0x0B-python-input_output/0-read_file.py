#!/usr/bin/python3
"""read UTF8 file"""


def read_file(filename=""):
    """
    Reads file (UTF8), prints the contents to stdout.

    Args:
        filename (str): name of the file to read "".
    """

    with open(filename, "r", encoding="utf-8") as file:
        contents = file.read()
        print(contents)
