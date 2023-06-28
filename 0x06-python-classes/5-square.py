#!/usr/bin/python3
"""define a class"""


class Square:
    def __init__(self, size=0):
        self.size = size
   
   """create a property instance for the object"""
    @property
    def size(self):
        return self.__size

    """set the property of the object"""
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
    """Public instance method to return the current square area"""
    def area(self):
        return (self.__size)**2

    """
    Public instance method to print
    in stdout the square with the character #
    """
    def my_print(self):
        if self.__size == 0:
            pass
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print("")
