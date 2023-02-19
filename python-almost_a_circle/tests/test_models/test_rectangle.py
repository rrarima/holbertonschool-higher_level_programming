#!/usr/bin/python3
"""Rectangle Unit test"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Rectangle unit test"""

    def test_create(self):
        """
        Test if creating a new Rectangle works.
        """
        r = Rectangle(1, 2)
        self.assertTrue(r)

    def test_create_args(self):
        """
        Test if creating a new Rectangle with various arguments works.
        """
        r1 = Rectangle(1, 2, 3)
        r2 = Rectangle(1, 2, 3, 4)
        r3 = Rectangle("1", 2)
        r4 = Rectangle(1, "2")
        r5 = Rectangle(1, 2, "3")
        r6 = Rectangle(1, 2, 3, "4")
        r7 = Rectangle(1, 2, 3, 4, 5)
        r8 = Rectangle(-1, 2)
        r9 = Rectangle(1, -2)
        r10 = Rectangle(0, 2)
        r11 = Rectangle(1, 0)
        r12 = Rectangle(1, 2, -3)
        r13 = Rectangle(1, 2, 3, -4)
        self.assertTrue(r1)
        self.assertTrue(r2)
        self.assertTrue(r3)
        self.assertTrue(r4)
        self.assertTrue(r5)
        self.assertTrue(r6)
        self.assertTrue(r7)
        self.assertTrue(r8)
        self.assertTrue(r9)
        self.assertTrue(r10)
        self.assertTrue(r11)
        self.assertTrue(r12)
        self.assertTrue(r13)

if __name__ == "__main__":
    unittest.main()
