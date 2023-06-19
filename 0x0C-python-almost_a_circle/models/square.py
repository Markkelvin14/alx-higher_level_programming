#!/usr/bin/python3
"""defines a class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """create a class square"""
    def __init__(self, size, x=0, y=0, id=None):
        """initalise a new class"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """return width or height"""
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                  self.width))

    @property
    def size(self):
        """return the size of the width"""
        return self.width

    @size.setter
    def width(self, value):
        """set the size of the square"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assigns attributes"""
        order = ['id', 'size', 'x', 'y']
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
        """returns a dictionary with sttribites of the object
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
        """
        order = ['id', 'size', 'x', 'y']
        att = {}
        for key in order:
            att[key] = getattr(self, key)
        return att
