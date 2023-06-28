#!/usr/bin/python3
"""create a class called Square"""


class Square():
    """instantiate objects of the class"""
    def __init__(self, size=0):
        """instantiate the object of the callin function"""
        self.__size = size

    """retrive the instance of the main class"""
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        """check for conditions true and false"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            """instantiate a private instance attribute"""
            self.__size = value

    def area(self):
        return (self.__size)**2
