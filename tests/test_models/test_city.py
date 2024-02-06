#!/usr/bin/env python3
"""Unittests for City class"""

import unittest
import os
from os import getenv
from models.city import City
from models.base_model import BaseModel

class TestingCity(unittest.TestCase):
    """This tests the city class"""

    @classmethod
    def setUpClass(cls):
        """sets up the instance"""
        cls.city = City()
        cls.city.name = "San Francisco"
        cls.city.state_id = "CA"

    @classmethod
    def teardown(cls):
        """deletes the instance at the end of the test"""
        del cls.city

    def tearDown(self):
        """deletes the file at the end of the test"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_is_subclass(self):
        """tests if city is a subclass of BaseModel"""
        self.assertTrue(issubclass(self.city.__class__, BaseModel), True)

    def test_attribute_type(self):
        """tests if the attributes are strings"""
        self.assertEqual(type(self.city.name), str)
        self.assertEqual(type(self.city.state_id), str)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") == 'db', 'DB')
    def test_save(self):
        """tests if save works"""
        self.city.save()
        self.assertNotEqual(self.city.created_at, self.city.updated_at)

    def test_to_dict(self):
        """tests if to_dict works"""
        self.assertEqual('to_dict' in dir(self.city), True)

if __name__ == "__main__":
    unittest.main()
