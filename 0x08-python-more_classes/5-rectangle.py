#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """return the width of the Rec"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """return the height of the Rec"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the Rec"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the perimeter of the Rec"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Return the printable representation of the Rectangle.
        prints the rectangle with the # char"""
        if self.__width == 0 or self.__height == 0:
            return ("")

        rec = []
        for m in range(self.__height):
            [rec.append('#') for k in range(self.__width)]
            if m != self.__height - 1:
                rec.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """Print a message for deletion of a Rectangle."""
        print("Bye rectangle...")
