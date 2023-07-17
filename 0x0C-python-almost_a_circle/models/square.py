#!/usr/bin/python3
"""imoport module rectangle.py"""
from models.rectangle import Rectangle


"""
=====================
create a class square
=====================
"""



class Square(Rectangle):
    """class construct"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """return the size"""

        return self.height

    @size.setter
    def size(self, value):
        """set values for attributes"""

        self.width = value
        self.height = value

    def __str__(self):
        """return an override string"""

        return f"[{type(self).__name__}] ({self.id}) {self.x}/{self.y} - {self.height}"
