#!/usr/bin/python3
"""Create Square class inheriting Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size):
        """Initialise square"""

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Return string representation of square"""
        return f"[{self.__class__.__name__}] {self.__size}/{self.__size}"
