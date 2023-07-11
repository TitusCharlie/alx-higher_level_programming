#!/usr/bin/python3
"""
===================================
module with method is_kind_of_class
===================================
"""


def is_kind_of_class(obj, a_class):
    """check if obj is an instance of a class
       if obj is an instance of an inherited class"""
    return isinstance(obj, a_class)
