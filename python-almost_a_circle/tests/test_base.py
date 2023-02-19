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
