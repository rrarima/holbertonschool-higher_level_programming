#!/usr/bin/python3
"""Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Inherit rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        """Set size to value"""
        self.width = value
        self.height = value

    def __str__(self):
        """Return string format"""
        return "[{}] ({}) {}/{} - {}".format(
                self.__class__.__name__, self.id, self.x, self.y,
                self.width)

    def update(self, *args, **kwargs):
        """Return variable number of keywords and non-keywords"""
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                setattr(self, k, v)
        elif len(args) != 0:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass
