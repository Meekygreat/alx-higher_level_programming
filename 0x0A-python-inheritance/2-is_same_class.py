#!/usr/bin/python3
"""Module 2-is_same_class.py.
returns True if the object is exactly an instance of the specified class.
"""

def is_same_class(obj, a_class):
    """returns True if the obj is exactly an instance of a_class.
    Args:
       obj: the object to find its instance.
       a_class: the class to look into.
    Return: True if the obj is exactly an instance of a_class, otherwise False.
    """

    return True if type(obj) is a_class else False
