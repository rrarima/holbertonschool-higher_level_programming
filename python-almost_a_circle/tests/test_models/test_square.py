#!/usr/bin/python3
"""Square unittest module."""
from unittest import TestCase

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class Test_Square(TestCase):
    """Test class for square"""

    def setup(self):
        Base._Base__nb_objects = 0

    def test_empty(self):
        with self.assertRaises(TypeError):
            Square()

if __name__ == "__main__":
    unittest.main()
