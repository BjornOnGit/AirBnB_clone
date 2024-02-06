#!/usr/bin/ env python3
""" Unit tests for Amenity class"""

import unittest
import os
from models.amenity import Amenity
from models.base_model import BaseModel

class TestingAmenity(unittest.TestCase):
    """This will test the Amenity class """

    @classmethod
    def setUpClass(cls):
        """set up for every test"""
        cls.amenity = Amenity()
        cls.amenity.name = "Swimming Pool"

    @classmethod
    def teardown(cls):
        """Removes test instances at the end of a test"""
        del cls.amenity

    def tearDown(self):
        """Removes JSON file at the end of a test"""
        try:
            if os.path.exists("file.json"):
                os.remove("file.json")
        except IOError:
            print("No JSON file to delete")

    def test_check_for_docstrings(self):
        """checks for docstrings"""
        self.assertIsNotNone(Amenity.__doc__)

    def test_attributes(self):
        """checks if attributes exist"""
        self.assertTrue('id' in self.amenity.__dict__)
        self.assertTrue('created_at' in self.amenity.__dict__)
        self.assertTrue('updated_at' in self.amenity.__dict__)
        self.assertTrue('name' in self.amenity.__dict__)

    def test_is_subclass(self):
        """"Checks if Amenity is a subclass of BaseModel"""
        self.assertTrue(issubclass(self.amenity.__class__, BaseModel), True)

    def test_attribute_type(self):
        """Checks if attribute is of the correct type"""
        self.assertEqual(type(self.amenity.name), str)

    def test_save(self):
        """Checks if save method works"""
        self.amenity.save()
        self.assertNotEqual(self.amenity.created_at, self.amenity.updated_at)

    def test_dict(self):
        """Checks if the to_dict method works"""
        self.assertEqual('to_dict' in dir(self.amenity), True)

if __name__ == "__main__":
    unittest.main()
