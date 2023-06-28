#!/usr/bin/python3
"""Create a class called Square"""


class Square():
    """instantiate the object of the class"""
    def __init__(self, size=0):
        """check if the instance is integer"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            """instantiate private instance attribute"""
            self.__size = size

    """define a public instance method that returns the area"""
    def area(self):
        returns self.__size**2
