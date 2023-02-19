#!/usr/bin/python3
"""Rectangle Unit test"""
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """Rectangle unit test"""

    def objCount(self):
        """Grabs obj count"""
        Base._Base__nb_objects = 0
        self.assertEqual(Base._Base__nb_objects, 0)

if __name__ == '__main__':
    unittest.main()
