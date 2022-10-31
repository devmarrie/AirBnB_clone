#!/usr/bin/python3
import unittest
import json
import models
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.engine.file_storage import FileStorage

"""Testing the file storage file.
"""


class TestFileStorageType(unittest.TestCase):
    """
    Checks the type of FileStorage
    """
    def test_FileStorage_type(self):
        self.assertTrue(FileStorage,type(FileStorage))


class TestFileStorageInstance(unittest.TestCase):
    """Checks for FileStorage instantiation"""
    def test_FileStorageInstance(self):
        file = FileStorage()
        self.assertIsInstance(file, FileStorage)

class TestFileStorageStorageType(unittest.TestCase):
    """Checks if type of all is a dict"""
    def test_FileStorage_all(self):
        self.assertEqual(dict,type(models.storage.all()))
    def test_FileStorage_new(self):
        us = User()
        st = State()
        pl = Place()
        cy = City()
        am = Amenity()
        rv = Review()
        self.assertIn("User.{}".format(us.id),models.storage.all().keys())
        self.assertIn("State.{}".format(st.id),models.storage.all().keys())
        self.assertIn("Place.{}".format(pl.id),models.storage.all().keys())
        self.assertIn("City.{}".format(cy.id),models.storage.all().keys())
        self.assertIn("Amenity.{}".format(am.id),models.storage.all().keys())
        self.assertIn("Review.{}".format(rv.id),models.storage.all().keys())
        
class TestFileStorageStorageIn(unittest.TestCase): 
    """Tests if the files are stored"""       
    def test_FileStorage_Classes(self):
        us = User()
        st = State()
        pl = Place()
        cy = City()
        am = Amenity()
        rv = Review()
        models.storage.new(us)
        models.storage.new(st)
        models.storage.new(pl)
        models.storage.new(cy)
        models.storage.new(am)
        models.storage.new(rv)
        self.assertIn(us,models.storage.all().values())
        self.assertIn(st,models.storage.all().values())
        self.assertIn(pl,models.storage.all().values())
        self.assertIn(cy,models.storage.all().values())
        self.assertIn(am,models.storage.all().values())
        self.assertIn(rv,models.storage.all().values())
    
if __name__ == "__main__":
    unittest.main()