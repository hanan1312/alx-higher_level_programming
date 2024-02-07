#!/usr/bin/python3
"""append to UTF8 file"""


def append_write(filename="", text=""):
    """
    Appends a string to the end of a text file (UTF8) and returns the number of characters added.
    Creates the file if it doesn't exist.

    Args:
        filename (str): name of the file to append to "".
        text (str): text to append to the file "".

    Returns:
        int: number of characters appended to the file.
    """

    with open(filename, "a", encoding="utf-8") as file:  # Open in append mode ("a")
        num_chars = file.write(text)
    return num_chars
