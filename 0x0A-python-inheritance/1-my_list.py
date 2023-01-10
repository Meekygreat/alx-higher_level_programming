#!/usr/bin/python3
"""Module 1-my_list.py.
a class MyList that inherits from list.
"""


class MyList(list):
    """a class MyList that inherits from list"""

    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""

        newlist = self[:]
        newlist.sort()
        print("{}".format(newlist))
