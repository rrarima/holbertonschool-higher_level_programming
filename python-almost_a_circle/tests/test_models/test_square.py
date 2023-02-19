#!/usr/bin/python3
"""
Unit tests for the Square class
"""
import unittest
from io import StringIO
from unittest.mock import patch
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test cases for the Square class"""

    def setUp(self):
        """Resets the number of objects"""
        Base._Base__nb_objects = 0
        self.assertEqual(Base._Base__nb_objects, 0)

    def test_size_value(self):
        """Test that the size value is set correctly"""
        s1 = Square(5)
        self.assertEqual(s1.size, 5)

    def test_size_type(self):
        """Test that an invalid type for size raises a TypeError"""
        with self.assertRaises(TypeError):
            s1 = Square("hello")

    def test_size_value_negative(self):
        """Test that a negative size value raises a ValueError"""
        with self.assertRaises(ValueError):
            s1 = Square(-5)

    def test_x_value(self):
        """Test that the x value is set correctly"""
        s1 = Square(5, 2)
        self.assertEqual(s1.x, 2)

    def test_x_value_negative(self):
        """Test that a negative x value raises a ValueError"""
        with self.assertRaises(ValueError):
            s1 = Square(5, -2)

    def test_y_value(self):
        """Test that the y value is set correctly"""
        s1 = Square(5, 2, 3)
        self.assertEqual(s1.y, 3)

    def test_y_value_negative(self):
        """Test that a negative y value raises a ValueError"""
        with self.assertRaises(ValueError):
            s1 = Square(5, 2, -3)

    def test_area(self):
        """Test that the area is calculated correctly"""
        s1 = Square(5)
        self.assertEqual(s1.area(), 25)

        s1 = Square(5, 2, 3, 7)
        s1.update(1, 2, 3, 4)
        self.assertEqual(str(s1), "[Square] (1) 3/4 - 2")
    
    def test_to_dictionary(self):
        """Test that the to_dictionary method works correctly"""
        s1 = Square(5, 2, 3, 7)
        s1_dict = s1.to_dictionary()
        expected_dict = {'id': 7, 'size': 5, 'x': 2, 'y': 3}
        self.assertEqual(s1_dict, expected_dict)    

    def test_square_creation_zero(self):
        """0 test case"""
        with self.assertRaises(ValueError):
            s = Square(0)

    def test_square_instantiation(self):
        """Test instantiation of Square objects"""

        s1 = Square(7)
        s2 = Square(3, 2, 1, "hello")

        with self.assertRaises(ValueError):
            s3 = Square(-5, 3, 4)
            s4 = Square(9.5)
            s5 = Square(float('inf'))
            s6 = Square("string")
            s9 = Square(None)

        with self.assertRaises(TypeError):
            s7 = Square(5, "hi")
            s8 = Square(5, None)
            s10 = Square(5, float('inf'))
            s11 = Square(5, 9.5)
            s12 = Square()

        self.assertEqual(s1.id, 1)
        self.assertEqual(s1._Base__nb_objects, 3)
        self.assertEqual(s2.id, 'hello')
        self.assertEqual(s2._Base__nb_objects, 3)    

    def test_create_methods(self):
        """Test create method with different arguments"""
        
        self.assertTrue(hasattr(Square, 'create'))
        
        s1 = Square.create(**{ 'id': 89 })
        self.assertEqual(s1.id, 89)
        
        s2 = Square.create(**{ 'id': 89, 'size': 1 })
        self.assertEqual(s2.id, 89)
        self.assertEqual(s2.size, 1)
        
        s3 = Square.create(**{ 'id': 89, 'size': 1, 'x': 2 })
        self.assertEqual(s3.id, 89)
        self.assertEqual(s3.size, 1)
        self.assertEqual(s3.x, 2)
        
        s4 = Square.create(**{ 'id': 89, 'size': 1, 'x': 2, 'y': 3 })
        self.assertEqual(s4.id, 89)
        self.assertEqual(s4.size, 1)
        self.assertEqual(s4.x, 2)
        self.assertEqual(s4.y, 3)    

    def test_save_and_load_methods(self):
        """Test save_to_file and load_from_file methods"""
        
        self.assertTrue(hasattr(Square, 'save_to_file'))
        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")
        
        self.assertTrue(hasattr(Square, 'save_to_file'))
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")
        
        self.assertTrue(hasattr(Square, 'save_to_file'))
        s1 = Square(1)
        Square.save_to_file([s1])
        with open("Square.json", "r") as file:
            self.assertEqual(json.dumps([s1.to_dictionary()]), file.read())
        
        self.assertTrue(hasattr(Square, 'load_from_file'))
        if os.path.exists("Square.json"):
            os.remove("Square.json")
        self.assertEqual(Square.load_from_file(), [])
        
        self.assertTrue(hasattr(Square, 'load_from_file'))
        s2 = Square(2)
        Square.save_to_file([s2])
        squares = Square.load_from_file()
        self.assertEqual(len(squares), 1)
        self.assertIsInstance(squares[0], Square)
        self.assertEqual(squares[0].id, s2.id)
        self.assertEqual(squares[0].size, s2.size)
        self.assertEqual(squares[0].x, s2.x)
        self.assertEqual(squares[0].y, s2.y)

if __name__ == '__main__':
    unittest.main()
