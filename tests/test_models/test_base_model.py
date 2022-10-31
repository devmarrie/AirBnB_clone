#!/usr/bin/python3

"""Defines the tests for the BaseModel class
   Unittest classes:
   TestBaseModel_instantiation
   TestBaseModel_save
   TestBaseModel_to_dict
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Checking for class instantiation"""

    def test_instance(self):
        self.assertEqual(BaseModel, type(BaseModel))

    def test_id_type(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_type(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_type(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_kwargs(self):
        kwgs = {'id': '3a68d630-8a02-406f-927d-71b4526554d5',
                'created_at': '2022-10-29T08:52:59.957348',
                'updated_at': '2022-10-29T08:55:14.470644',
                '__class__': 'BaseModel'
                }
        new = BaseModel(**kwgs)
        self.assertEqual(new.id, kwgs['id'])


class TestBaseModel_Save(unittest.TestCase):
    """Tests the save method"""
    def test_updated(self):
        base = BaseModel()
        t1 = base.updated_at
        base.save()
        t2 = base.updated_at
        self.assertNotEqual(t1, t2)


class TestBaseModel_Todict(unittest.TestCase):
    """Test if our base function converts to dict and ISO format"""
    def test_type(self):
        dt = BaseModel()
        self.assertTrue(dt, type(dict.to_dict()))

    def test_dict(self):
        dt = self.__dict__
        new_dict = self.__dict__.copy()
        self.assertEqual(new_dict, dt)

    def test_contains(self):
        dt = BaseModel()
        self.assertIn("id", dt.to_dict())
        self.assertIn("created_at", dt.to_dict())
        self.assertIn("updated_at", dt.to_dict())
        self.assertIn("__class__", dt.to_dict())
