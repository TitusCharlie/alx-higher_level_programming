#!/usr/bin/python3
"""create a class"""


class Rectangle:
    """instantiate attributes"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    """create a property method for private instance"""
    @property
    def width(self):
        return self.__width
    """retrieve the property instance"""
    @width.setter
    def width(self, value):
        """check if width is an integer"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    """create a property method for private instance"""
    @property
    def height(self):
        return self.__height

    """retrieve the property instance"""
    @height.setter
    def height(self, value):
        """check if height is an integer"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    """public instace method"""
    def area(self):
        result = self.__width * self.__height
        return result

    """public instance method"""
    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        result = ""
        for i in range(self.__width):
            print("#")
            result = ""
            for j in range(self.__height):
                result.join("#")
                return result
