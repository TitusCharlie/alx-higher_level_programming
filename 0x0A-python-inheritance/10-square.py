#!/usr/bin/python3
"""
===================================
module with class BaseGeometry
===================================
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle that inherits BaseGeometry"""

    def __init__(self, size):
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """rectangle area"""

        return self.__size ** 2
    
    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
