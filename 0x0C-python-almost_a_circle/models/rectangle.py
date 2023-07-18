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
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """return value of width"""

        return self.__width

    @width.setter
    def width(self, value):
        """set the value of width"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("Width must be > 0")

        else:
            self.__width = value

    @property
    def height(self):
        """return value of height"""

        return self.__height

    @height.setter
    def height(self, value):
        """set the value of height"""

        if not isinstance(value, int):
            raise TypeError("heigh must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """return value of x"""

        return self.__x

    @x.setter
    def x(self, value):
        """set the value of x"""

        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")

        else:
            self.__x = value

    @property
    def y(self):
        """return value of y"""

        return self.__y

    @y.setter
    def y(self, value):
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

        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def update(self, *args, **kwargs):
        """update argument input"""

        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.__width = args[1]
        if len(args) >= 3:
            self.__height = args[2]
        if len(args) >= 4:
            self.__x = args[3]
        if len(args) >= 5:
            self.__y = args[4]

        for key, value in kwargs.items():
            if 'id' == key:
                self.id = value
            if 'width' == key:
                self.__width = value
            if 'height' == key:
                self.__height = value
            if 'x' == key:
                self.__x = value
            if 'y' == key:
                self.__y = value

        """instance_attr = ['id', '__width', '__height','__x', '__y']

        for i, value in enumerate(args):
            if i < len(instance_attr):
                setattr(self, instance_attr[i], value)
            else:
                break"""

    def __str__(self):
        """return an override string"""

        width = self.width
        height = self.height
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {width}/{height}"
