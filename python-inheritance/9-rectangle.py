#!/usr/bin/python3
"""Inherit BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle inherits BaseGeometry"""

    def __init__(self, width, height):
        """Initialise rectangle"""

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Return string representation of square"""
        return f"[{self.__class__.__name__}] {self.__size}/{self.__size}"
