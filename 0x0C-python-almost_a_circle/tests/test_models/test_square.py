#!/usr/bin/python3
"""Unittest for square.py file"""
import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle
from unittest.mock import patch
from io import StringIO


class Test_square(unittest.TestCase):
    """Defines a class to evaluate diferent test cases for square.py file"""

    def test_instance_class(self):
        """Checks for a instance of the class"""
        s1 = Square(10)
        self.assertIsInstance(s1, Square)
        self.assertTrue(issubclass(Square, Rectangle))
        self.assertTrue(issubclass(Square, Base))
        self.assertTrue(id(Square) != id(Rectangle))
        self.assertTrue(id(Square) != id(Base))
        self.assertTrue(type(Square) == type(Rectangle))
        self.assertTrue(type(Square) == type(Base))
        s2 = Square(2)
        self.assertTrue(type(s1) == type(s2))
        self.assertFalse(id(s1) == id(s2))

    def test_init_attributes(self):
        """Checks when id is none"""
        s1 = Square(10)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.size, 10)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)

    def test_raise_errors(self):
        """Check for raises errors"""
        with self.assertRaises(TypeError):
            s1 = Square()
        with self.assertRaises(NameError):
            s1 = Square_shape()
        with self.assertRaises(AttributeError):
            s1 = Square(10, 80)
            s1.to_json()
        with self.assertRaises(ValueError):
            s3 = Square(-4)
        with self.assertRaises(TypeError):
            s4 = Square("4")
        with self.assertRaises(TypeError):
            s6 = Square(10, 4, "9")
        with self.assertRaises(TypeError):
            s7 = Square(10, "4", 9)
        with self.assertRaises(ValueError):
            s8 = Square(10, 4, -5, 7)
        with self.assertRaises(ValueError):
            s9 = Square(10, -4, 5, 10)
        with self.assertRaises(TypeError):
            s10 = Square(10, 4, 5, 10, 100)
        with self.assertRaises(ValueError):
            s11 = Square(0)
        with self.assertRaises(ValueError):
            s1.x = -4
        with self.assertRaises(TypeError):
            s1.x = "4"
        with self.assertRaises(ValueError):
            s1.size = -10

    def test_area(self):
        """Check area method of square objects"""
        s1 = Square(3, 2)
        area = s1.area()
        self.assertEqual(area, 9)

        s2 = Square(3, 2)
        area = Square.area(s2)
        self.assertEqual(area, 9)

        s3 = Square(50, 20, 4, 10)
        area = s3.area()
        self.assertEqual(area, 25000)

        s4 = Rectangle(5, 5, 4)
        area = s4.area()
        self.assertEqual(area, 25)

        s5 = Square(10)
        area = s5.area()
        self.assertEqual(area, 100)

    def test_display(self):
        """Checks display method for square"""
        output_1 = "#\n"
        s1 = Square(1)
        with patch('sys.stdout', new=StringIO()) as out:
            s1.display()
            self.assertEqual(out.getvalue(), output_1)

    def test_update(self):
        """Check update method"""
        s1 = Square(5)
        self.assertEqual(s1.__str__(), "[Square] (1) 0/0 - 5")
        s1.update(10)
        self.assertEqual(s1.__str__(), "[Square] (10) 0/0 - 5")
        s1.update(1, 2)
        self.assertEqual(s1.__str__(), "[Square] (1) 0/0 - 2")
        s1.update(1, 2, 3)
        self.assertEqual(s1.__str__(), "[Square] (1) 3/0 - 2")
        s1.update(1, 2, 3, 4)
        self.assertEqual(s1.__str__(), "[Square] (1) 3/4 - 2")

    def test_dictionary_representation(self):
        """Check to_dictionary method"""
        s1 = Square(10, 2, 1)
        s1_dictionary = s1.to_dictionary()
        self.assertEqual(s1_dictionary, {'x': 2, 'y': 1, 'id': 1, 'size': 10})

        s2 = Square(1, 1)
        s2_dictionary = s2.to_dictionary()
        self.assertEqual(s2_dictionary, {'x': 1, 'y': 0, 'id': 2, 'size': 1})

        s3 = Square(10, 0, 2)
        s3_dictionary = s3.to_dictionary()
        self.assertEqual(s3_dictionary, {'x': 0, 'y': 2, 'id': 3, 'size': 10})

    def tearDown(self):
        """Tear down test method to reset class attribute"""
        Base._Base__nb_objects = 0
        try:
            os.remove("Rectangle.json")
        except Exception:
            pass
        try:
            os.remove("Square.json")
        except Exception:
            pass
        try:
            os.remove("Rectangle.csv")
        except Exception:
            pass
        try:
            os.remove("Square.csv")
        except Exception:
            pass


if __name__ == '__main__':
    unittest.main()
