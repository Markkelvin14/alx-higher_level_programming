#!/usr/bin/python3
"""define a class"""
from models.base import Base


class Rectangle(Base):
    """create a class rectangle that inherits from base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """intialise a new class"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """return the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the size of the width"""

        if type(value) is not int:
            raise TypeError("must be an integer")
        if value <= 0:
            raise ValueError("must be > 0")
        self.__width = value

    @property
    def height(self):
        """return the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the size of the height"""
        if type(value) is not int:
            raise TypeError("must be an integer")
        if value <= 0:
            raise ValueError("must be > 0")
        self.__height = value

    @property
    def x(self):
        """return the value of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """set the size of x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """return the value of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """set the value of y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area of the rectangle"""
        return self.width * self.height

    def display(self):
        """prints # to the stdout"""
        for m in range(self.y):
            print()
        for m in range(self.height):
            print(" " * self.x + self.width * '#')

    def __str__(self):
        """override the __str__"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
                                                        self.y, self.width
                                                        self.height))

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        order = ['id', 'width', 'height', 'x', 'y']
        if args is not None and bool(args) is True:
            m = 0
            for key in order:
                try:
                    setattr(self, key, args[m])
                except IndexError:
                    pass
                m += 1
        else:
            for key in order:
                try:
                    setattr(self, key, kwargs[key])
                except KeyError:
                    pass

    def to_dictionary(self):
        """returns a dictionary with atts of objects

        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
        """
        order = ['x', 'y', 'id', 'height', 'width']
        att = {}
        for key in order:
            att[key] = getattr(self, key)
        return att
