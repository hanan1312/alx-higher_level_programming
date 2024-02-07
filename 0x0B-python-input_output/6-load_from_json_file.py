#!/usr/bin/python3
""" function writes an Object to a text file, using a JSON representation:"""
import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    Args:
        filename (str): name of the JSON file to load.

    Returns:
        Python object represented by the JSON data in the file.
    """

    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
