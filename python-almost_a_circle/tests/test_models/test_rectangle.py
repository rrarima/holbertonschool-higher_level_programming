#!/usr/bin/python3
"""Rectangle Unit test"""
import unittest
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base


class TestRectangle(unittest.TestCase):
    """Rectangle unit test"""

    def test_create(self):
        """
        Test if creating a new Rectangle works.
        """
        r = Rectangle(1, 2)
        self.assertTrue(r)

if __name__ == "__main__":
    unittest.main()
