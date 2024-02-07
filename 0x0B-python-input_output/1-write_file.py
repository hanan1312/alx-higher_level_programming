#!/usr/bin/python3
"""write UTF8 file"""


def write_file(filename="", text=""):
    """
    Writes to a file (UTF8) and returns the number of characters written.

    Args:
        filename (str): name of the file to write to "".
        text (str): The text to write to the file"".

    Returns:
        int: number of characters written to the file.
    """

    with open(filename, "w", encoding="utf-8") as file:
        num_chars = file.write(text)
    return num_chars
