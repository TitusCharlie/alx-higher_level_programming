#!/usr/bin/python3
def add_integer(a, b=98):
    """function that adds 2 integers"""
    if (type(a) == int or type(a) == float) and (type(b) == int or type(b) == float):
        a, b = int(a), int(b)
        return a + b
    else:
        if type(a) != int:
            raise TypeError("a must be an integer")
        raise TypeError("b must be an integer")
