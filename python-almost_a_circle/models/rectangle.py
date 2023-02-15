#!/usr/bin/python3
"""Rectangle class using Base"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialise class"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Return width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Return Height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """return x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Set x"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Return y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set y"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return area od rectangle"""
        return self.__width * self.__height

    def display(self):
        """Display rectangle"""
        for row in range(self.__height):
            print((self.__x * "") + (self.__width * '#'))

    def __str__(self):
        """Return string format"""
        return "[" + self.__class__.__name__ + "] " "(" + str(self.id) + ") " \
            + str(self.__x) + "/" + str(self.__y) + " - " \
            + str(self.__width) + "/" + str(self.__height)
