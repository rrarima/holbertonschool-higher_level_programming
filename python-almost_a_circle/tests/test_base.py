#!/usr/bin/python3
"""Unit test for base class"""
import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """Base class unit test"""

    def test_id(self):
        """Test base id if it exist"""
        self.b1 = Base()
        self.asserEqual(self.b1.id, 1)
        self.b2 = Base()
        self.asserEqual(self.b2.id, 2)
        self.b3 = Base()
        self.asserEqual(self.b3.id, 3)
        self.b4 = Base(5)
        self.asserEqual(self.b4.id, 5)
