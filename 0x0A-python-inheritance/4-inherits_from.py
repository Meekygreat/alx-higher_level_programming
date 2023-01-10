#!/usr/bin/python3
"""Module 4-inherits_from.py.
returns True if the object is an instance of a class that inherited
(directly or indirectly) from the specified class ; otherwise False.
"""


def inherits_from(obj, a_class):
    """returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class ; otherwise False.
    Args:
       obj: object to find its instance.
       a_class: class to look into.
    Return: True if the object is an instance of a class that inherited
           (directly or indirectly) from a_class, otherwise False.
    """

    return isinstance(obj, a_class) and type(obj) != a_class
