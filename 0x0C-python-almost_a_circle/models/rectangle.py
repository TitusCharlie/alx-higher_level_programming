#!/usr/bin/python3
"""import module base"""
from models.base import Base


"""
===========================================
create Rectangle class to inherit from Base
===========================================
"""


class Rectangle(Base):
    """construct class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def get_width(self):
        """return value of width"""

        return self.__width

    def set_width(self, value):
        """set the value of width"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("Width must be > 0")

        else:
            self.__width = value

    def get_height(self):
        """return value of height"""

        return self.__height

    def set_height(self, value):
        """set the value of height"""

        if not isinstance(value, int):
            raise TypeError("heigh must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")        

        else:
            self.__height = value

    def get_x(self):
        """return value of x"""

        return self.__x

    def set_x(self, value):
        """set the value of x"""

        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")

        else:
            self.__x = value

    def get_y(self):
        """return value of y"""

        return self.__y

    def set_y(self, value):
        """set the value of y"""

        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")

        else:
            self.__y = value

    def area(self):
        """return the area of the rectangle"""

        return self.__width * self.__height

    def display(self):
        """loop through to print rectangle in #"""

        result = []
        for i in range(self.get_height()):
            adding = ""
            for j in range(self.get_width()):
                adding += "#"
            result.append(adding)
        output = "\n".join(result)
        print(output)

