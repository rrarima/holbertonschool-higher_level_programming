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

    def test_instance(self):
        "Test instantiation with valid arguments"
        o1 = Rectangle(2, 3)
        o2 = Rectangle(3, 4, 1, 1, 10)
        self.assertEqual(o1.width, 2)
        self.assertEqual(o1.height, 3)
        self.assertEqual(o1.x, 0)
        self.assertEqual(o1.y, 0)
        self.assertEqual(o1.id, 8)
        self.assertEqual(o2.width, 3)
        self.assertEqual(o2.height, 4)
        self.assertEqual(o2.x, 1)
        self.assertEqual(o2.y, 1)
        self.assertEqual(o2.id, 10)

        "Test instantiation with invalid arguments"
        self.assertRaises(TypeError, Rectangle, "string")
        self.assertRaises(TypeError, Rectangle, None)
        self.assertRaises(TypeError, Rectangle, float('inf'))
        self.assertRaises(TypeError, Rectangle, 9.5, 9.3)
        self.assertRaises(ValueError, Rectangle, -8, 9)
        self.assertRaises(TypeError, Rectangle)

    def test_str(self):
        """Test __str__() for Rectangle"""

        r1 = Rectangle(4, 5, 1, 2, 1)
        r2 = Rectangle(10, 15, 3, 4, 2)
        r3 = Rectangle(7, 8, 0, 0, 3)
        r4 = Rectangle(2, 6, 2, 2, "eps")

        assert str(r1) == "[Rectangle] (1) 1/2 - 4/5"
        assert str(r2) == "[Rectangle] (2) 3/4 - 10/15"
        assert str(r3) == "[Rectangle] (3) 0/0 - 7/8"
        assert str(r4) == "[Rectangle] (eps) 2/2 - 2/6"

if __name__ == "__main__":
    unittest.main()
