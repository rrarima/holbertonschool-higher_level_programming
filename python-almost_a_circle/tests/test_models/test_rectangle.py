#!/usr/bin/python3
"""Rectangle Unit test"""
import unittest
import os
from io import StringIO
from unittest.mock import patch
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
        self.assertEqual(o1.id, 9)
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

    def test_display(self):
        """Testing display()"""

        o1 = Rectangle(3, 2)
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            o1.display()
            self.assertEqual(fakeOutput.getvalue(), '###\n###\n')

        o2 = Rectangle(4, 5, 0, 1, 12)
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            o2.display()
            self.assertEqual(fakeOutput.getvalue(),
                             '\n####\n####\n####\n####\n####\n')
    def test_rectangle_update(self):
        r1 = Rectangle(4, 3, 1, 2, 5)
        r2 = Rectangle(2, 4)
        r3 = Rectangle(1, 1, 1, 1, 10)
        r4 = Rectangle(1, 1, 1)
        r5 = Rectangle(2, 2, id="hello")

        r1.update(3, 5, 1, 1, 7)
        self.assertEqual(r1.__str__(), '[Rectangle] (3) 1/7 - 5/1')
        with self.assertRaises(ValueError):
            r2.update(x=2, y=-1, width=-2)
            r3.update(3, "string", 1)
        r4.update(5)
        self.assertEqual(r4.__str__(), '[Rectangle] (5) 1/0 - 1/1')
        r5.update(id=8, x=1, width=3)
        self.assertEqual(r5.__str__(), '[Rectangle] (8) 1/0 - 3/2')

    def test_rectangle_to_dict(self):
        """Testing to_dictionary()"""
        r1 = Rectangle(5, 7)
        r2 = Rectangle(8, 10, 3, 4, 5)
        r3 = Rectangle(3, 2, 1, 1)
        r4 = Rectangle(3, 2, 0, 0, 10)

        expected_dict_r1 = {'id': r1.id, 'width': 5, 'height': 7, 'x': 0, 'y': 0}
        expected_dict_r2 = {'id': 5, 'width': 8, 'height': 10, 'x': 3, 'y': 4}
        expected_dict_r3 = {'id': r3.id, 'width': 3, 'height': 2, 'x': 1, 'y': 1}
        expected_dict_r4 = {'id': 10, 'width': 3, 'height': 2, 'x': 0, 'y': 0}

        self.assertDictEqual(r1.to_dictionary(), expected_dict_r1)
        self.assertDictEqual(r2.to_dictionary(), expected_dict_r2)
        self.assertDictEqual(r3.to_dictionary(), expected_dict_r3)
        self.assertDictEqual(r4.to_dictionary(), expected_dict_r4)

if __name__ == "__main__":
    unittest.main()
