#!/usr/bin/python3
""" function writes an Object to a text file, using a JSON representation:"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using JSON representation.

    Args:
        my_obj: object to save as JSON.
        filename (str): name of the file to write to.
    """

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
