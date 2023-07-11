#!/usr/bin/python3
"""
================================
module with method is_same_class
================================
"""


def is_same_class(obj, a_class):
    """check if obj is an instance of a_class"""
    if type(obj) is not a_class:
        return False
    else:
        return True
