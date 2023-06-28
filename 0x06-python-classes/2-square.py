#!/usr/bin/python3
"""Define a class called square"""


class Square():
    """instantiate size to the class method"""
    def __init__(self, size=0):
        """check for conditions true and false"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            """instantiate a private instance attribute"""
            self.__size = size
