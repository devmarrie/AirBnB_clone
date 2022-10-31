#!/usr/bin/python3

"""
Handles file storage
serialisation and Deserialization
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage():
    """
    This class defines the following methods,
    all(), new(), save() and reload()
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        makes the _objects public
        """
        return self.__objects

    def new(self, obj):
        """
        Populates the _objects
        The key now includes <class name.id>
        """
        nm = obj.__class__.__name__
        key = "{}.{}".format(nm, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Json serialization
        We shall use our python dictonary dct
        so that we can easily convert to json object
        """
        dct = {}

        for key, value in self.__objects.items():
            dct[key] = value.to_dict()
            with open(self.__file_path, "w") as f:
                json.dump(dct, f)

    def reload(self):
        """
        deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists
        load() converts to a pyton object
        The split method splits the key containing id and class
        """
        try:
            with open(self.__file_path, "r") as f:
                dct_obj = json.load(f)
            for key, value in dct_obj.items():
                self.__objects[key] = eval(key.split(".")[0])(**value)

        except FileNotFoundError:
            pass
