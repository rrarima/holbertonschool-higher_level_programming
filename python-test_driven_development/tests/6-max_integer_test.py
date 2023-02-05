#!/usr/bin/python3
"""Unittest max_integer"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test for max_integer"""


    def test_max_int(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_int_beginning(self):
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_max_int_middle(self):
        self.assertEqual(max_integer([1, 2, 5, 4, 3]), 5)

    def test_max_int_one_neg_number(self):
        self.assertEqual(max_integer([-1, 2, 3, 4]), 4)

    def test_max_int_only_neg(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_max_int_one_element_exist(self):
        self.assertEqual(max_integer([1]), 1)

    def test_max_int_empty_list(self):
        self.assertEqual(max_integer([]), None)


if __name__ == '__main__':
    unittest.main()
