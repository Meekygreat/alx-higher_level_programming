#!/usr/bin/python3
"""Module 0-lookup.
Returns a list of available attributes and methods of an obj.
"""


def lookup(obj):
    """returns the list of available attributes and methods of an object
    Args:
        - obj: object to look into
    """

    return dir(obj)
