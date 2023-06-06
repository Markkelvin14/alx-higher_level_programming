#!/usr/bin/python3
"""Unittests for max_integer([..])."""

import unittest
max_integer = __import__('6-max_integer').max_integer

class Test_MaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..])."""

    def test_ordered(self):
        """Test an ordered list of integers."""
        self.assertEqual(max_integer(1, 2, 3, 4), 4)

    def test_no_order(self):
         """Test an unordered list of integers."""
        self.assertEqual(max_integer(2, 1, 4, 3), 4)

    def test_max_at_begin(self):
        """Test a list with a beginning max value."""
        self.assertEqual(max_integer(4, 3, 2, 1), 4)

    def test_empty(self):
        """Test an empty list."""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_one_element(self):
        """Test a list with a single element."""
        self.assertEqual(max_integer(14), 14)

    def test_ints_and_floats(self):
        """Test a list of ints and floats."""
        self.assertEqual(max_integer(2.53, 18.5, -9, 17, 20), 20)

    def test_floats(self):
        """Test a list of floats."""
        self.assertEqual(max_integer(6.44, 2.32, -8.321, 14.5, 6.0), 14.5)

    def test_string(self):
        """Test a string."""
        string = "Brennan"
        self.assertEqual(max_integer(string), 'r')

    def test_empty_str(self):
         """Test an empty string."""
         self.assertEqual(max_integer(""), None)

    def test_l_of_str(self):
        """Test a list of strings."""
        strings = ["Mark", "is", "my", "name"]
        self.assertEqual(max_integer(strings), "name")

if __name__ == '__main__':
    unittest.main()
