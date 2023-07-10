#!/usr/bin/python3
"""create a class MyList that inherits from list

Public instance method that prints the list,
but sorted (ascending sort)

You can assume that all the elements of the list
will be of type int
"""

class MyList(list):
    """class with print_sorted method"""
    pass

    def print_sorted(self):
        """method to sort a list"""
        print(sorted(list(self)))
