#!/usr/bin/python3
"""function returns list of all attributes and methods of object"""


def lookup(obj):
    """
      Returns list of all attributes and methods of an object.

      Args:
          obj: object.

      Returns:
          A list of strings.
      """
    return (dir(obj))
