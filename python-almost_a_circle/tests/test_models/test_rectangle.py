#!/usr/bin/python3
"""Rectangle Unit test"""
from unittest import TestCase
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(TestCase):
    """Rectangle unit test"""

    def setup(self):
        """Grabs obj count"""
        Base._Base__nb_objects = 0
        self.assertEqual(Base._Base__nb_objects, 0)

    def test_area(self):
        t1 = Rectangle(1, 2)
        t2 = Rectangle(1, 2, 3, 4, 5)

        self.assertEqual(t1.area(), 2)
        self.assertEqual(t1.area(), 2)

if __name__ == "__main__":
    unittest.main()
