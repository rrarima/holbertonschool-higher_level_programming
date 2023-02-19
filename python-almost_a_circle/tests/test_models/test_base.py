import unittest
import sys
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle
import json


class TestBase(unittest.TestCase):
    """Test Base class functionality"""

    def setUp(self):
        """Redirect stdout to buffer for checking output of print functions."""
        sys.stdout = StringIO()

    def tearDown(self):
        """Reset stdout."""
        sys.stdout = sys.__stdout__

    def test_docstrings(self):
        """Test for existence of docstrings"""
        self.assertIsNotNone(Base.__doc__)
        self.assertIsNotNone(Base.__init__.__doc__)
        self.assertIsNotNone(Base.create.__doc__)
        self.assertIsNotNone(Base.to_json_string.__doc__)
        self.assertIsNotNone(Base.from_json_string.__doc__)
        self.assertIsNotNone(Base.save_to_file.__doc__)
        self.assertIsNotNone(Base.load_from_file.__doc__)

    def test_id(self):
        """Test id property"""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, 4)

    def test_to_from_json_string(self):
        """Test conversion of Base subclasses to JSON representation."""
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        if not Rectangle:
            return
        r1 = Rectangle(10, 7, 2, 8, 1)
        r1_dict = r1.to_dictionary()
        json_dict = Base.to_json_string([r1_dict])
        self.assertEqual(r1_dict, {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8})
        self.assertIsInstance(r1_dict, dict)
        self.assertIsInstance(json_dict, str)
        self.assertEqual(json.loads(json_dict), json.loads('[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]'))
        list_input = [{'id': 89, 'width': 10, 'height': 4}, {'id': 7, 'width': 1, 'height': 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertIsInstance(json_list_input, str)
        self.assertIsInstance(list_output, list)
        self.assertEqual(list_output, list_input)
        self.assertEqual(json.loads(json_list_input),
                         json.loads('[{"height": 4, "width": 10, "id": 89}, {"height": 7, "width": 1, "id": 7}]'))
