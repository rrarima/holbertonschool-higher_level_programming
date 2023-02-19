#!/usr/bin/python3
"""Rectangle Unit test"""
import unittest
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base


class TestRectangle(unittest.TestCase):
    """Rectangle unit test"""

    def update(self):
        """Tears down obj count"""
        Base._Base__nb_objects = 0
        self.assertEqual(Base._Base__nb_objects, 0)

    def test_area(self):
        """Testing area()"""
        o1 = Rectangle(1, 2)
        o2 = Rectangle(1, 3, 0, 0, 12)
        o3 = Rectangle(123, 123)

        self.assertEqual(o1.area(), 2)
        self.assertEqual(o2.area(), 3)
        self.assertEqual(o3.area(), 15129)

if __name__ == "__main__":
    unittest.main()
