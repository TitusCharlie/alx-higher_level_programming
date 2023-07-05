#!/usr/bin/python3
"""create a class"""


class Rectangle:
    """instantiate attributes"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    """create a property method for private instance"""
    @property
    def __width(self):
        return self.__width
    
    """retrieve the property instance"""
    @__width.setter
    def __width(self, value):
        """check if width is an integer"""
        if value != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    """create a property method for private instance"""
    @property
    def __height(self):
        return self.__height

    """retrieve the property instance"""
    @__height.setter
    def __height(self, value):
        """check if height is an integer"""
        if value != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__width = value
