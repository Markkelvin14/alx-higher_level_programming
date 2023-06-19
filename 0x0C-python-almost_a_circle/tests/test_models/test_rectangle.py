#!/usr/bin/python3
"""Unittest for rectangle.py file"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from unittest.mock import patch
from io import StringIO


class Test_rectangle(unittest.TestCase):
    """Defines a class to evaluate diferent test cases for rectangle.py file"""

    def test_instance_class(self):
        """Checks for a instance of the class
        """
        r1 = Rectangle(10, 2)
        self.assertIsInstance(r1, Rectangle)
        self.assertTrue(issubclass(Rectangle, Base))
        self.assertTrue(id(Rectangle) != id(Base))
        self.assertTrue(type(Rectangle) == type(Base))
        r2 = Rectangle(2, 5)
        self.assertTrue(type(r1) == type(r2))
        self.assertFalse(id(r1) == id(r2))

    def test_init_attributes(self):
        """Checks when id is none
        """
        r1 = Rectangle(10, 60)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 60)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

    def test_raise_errors(self):
        """Check for raises errors"""
        with self.assertRaises(TypeError):
            r1 = Rectangle()
        with self.assertRaises(NameError):
            r1 = Rectangle_shape()
        with self.assertRaises(AttributeError):
            r1 = Rectangle(10, 80)
            r1.to_json()
        with self.assertRaises(TypeError):
            r2 = Rectangle(10)
        with self.assertRaises(ValueError):
            r3 = Rectangle(10, -4)
        with self.assertRaises(ValueError):
            r4 = Rectangle(-10, 4)
        with self.assertRaises(TypeError):
            r5 = Rectangle(10, "4")
        with self.assertRaises(TypeError):
            r6 = Rectangle("10", 4)
        with self.assertRaises(TypeError):
            r7 = Rectangle(10, 4, "9")
        with self.assertRaises(TypeError):
            r8 = Rectangle(10, 4, 9, "20")
        with self.assertRaises(ValueError):
            r9 = Rectangle(10, 4, -5, 7)
        with self.assertRaises(ValueError):
            r10 = Rectangle(10, 4, 5, -10)
        with self.assertRaises(TypeError):
            r11 = Rectangle(10, 4, 5, 10, 30, 60)
        with self.assertRaises(ValueError):
            r12 = Rectangle(0, 10)
        with self.assertRaises(ValueError):
            r13 = Rectangle(15, 0)

    def test_area(self):
        """Check area method of rectangle objects"""
        r1 = Rectangle(3, 3)
        area = r1.area()
        self.assertEqual(area, 9)

        r2 = Rectangle(3, 2)
        area = Rectangle.area(r2)
        self.assertEqual(area, 6)

        r3 = Rectangle(30, 20, 4, 5, 10)
        area = r3.area()
        self.assertEqual(area, 600)

        r4 = Rectangle(5, 5, 4)
        area = r4.area()
        self.assertEqual(area, 25)

    def test_display(self):
        """Checks display method
        """
        output_1 = "#\n"
        r1 = Rectangle(1, 1)
        with patch('sys.stdout', new=StringIO()) as out:
            r1.display()
            self.assertEqual(out.getvalue(), output_1)

    def test_update(self):
        """Checks update method
        """
        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 10/10 - 10/10")
        r1.update(height=1)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 10/10 - 10/1")
        r1.update(width=1, x=2)

    def test_dictionary_representation(self):
        """Checks to_dictionary method"""
        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        self.assertEqual(r1_dictionary, {'x': 1, 'y': 9, 'id': 1, 'height': 2,
                                         'width': 10})

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
