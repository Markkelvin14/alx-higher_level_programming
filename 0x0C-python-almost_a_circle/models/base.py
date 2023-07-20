#!/usr/bin/env bash
"""define a class"""
import json
import csv
import turtle


class Base:
    """create a class base"""

    def __init__(self, id=None):
        """inialise a new class"""
        __nb_objects = 0

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns a json representation of a string"""
        if list_dictionaries is None:
            return "[]"
        return json.dump(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """add a class method that writes a json atr represntation"""
        filename = "{}.json".format(cls.__name__)
        with open(filename, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dictionaries = [m.to_dictionary() for m in list_objs]
                f.write(Base.to_json_string(list_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the json string"""
        if json_string is None:
            return ("[]")
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ = "Rectangle":
            dum = cls(1, 1)
        else:
            dum = cls(1)
        dum.update(**dictionary)
        return dum

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, 'r') as f:
                list_dictionaries = Base.from_json_string(f.read())
                return [cls.create(**m) for m in list_dictionaries]
            ecept IOError:
                return []
