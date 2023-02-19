#!/usr/bin/python3
"""Unit test for base class"""
from unittest import TestCase

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase(TestCase):
    """Base class unit test"""

    def setup(self):
        Base._Base__nb_objects = 0

    def test_id(self):
        """Test base id if it exist"""
        self.b1 = Base()
        self.b2 = Base()
        self.b3 = Base()
        self.b4 = Base(5)
        self.b5 = Base(-1)

        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 2)
        self.assertEqual(self.b3.id, 3)
        self.assertEqual(self.b4.id, 5)
        self.assertEqual(self.b5.id, -1)

if __name__ == '__main__':
    unittest.main()
