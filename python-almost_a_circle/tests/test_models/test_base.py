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
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base(None).id, 2)
        self.assertEqual(Base(20).id, 20)
        self.assertEqual(Base(-20).id, -20)

if __name__ == '__main__':
    unittest.main()
