#!/usr/bin/python3
"""Module 3-is_kind_of_class.py.
returns True if the object is an instance of, or if the object
is an instance of a class that inherited from, the specified class,
otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """returns True if the object is an instance of, or if the object
    is an instance of a class that inherited from a_class
    Args:
       obj: the object to find its instance.
       a_class: the class to look into.
    Return: True if the obj is a_class, or if the obj is an instance
            of a class that inherited from a_class, else False.
    """

    return isinstance(obj, a_class)
