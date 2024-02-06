#!/usr/bin/env python3
"""Unittest for the Place class"""

import unittest
import os
from os import getenv
from models.place import Place
from models.base_model import BaseModel


class TestingPlace(unittest.TestCase):
    """This will test the place class"""

    @classmethod
    def setUpClass(cls):
        """setting up for a test"""
        cls.place = Place()
        cls.place.city_id = "235-abcd"
        cls.place.user_id = "123-efgh"
        cls.place.name = "Holberton"
        cls.place.description = "School"
        cls.place.number_of_rooms = 3
        cls.place.number_of_bathrooms = 2
        cls.place.max_guests = 4
        cls.place.price_per_night = 100
        cls.place.latitude = 37.773972
        cls.place.longitude = -122.431297
        cls.place.amenity_ids = ["234-asdf"]

    @classmethod
    def teardown(cls):
        """at the end of the test, this tears it down"""
        del cls.place

    def tearDown(self):
        """tears down the test"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_checking_for_docstring(self):
        """Checks for docstrings"""
        self.assertIsNotNone(Place.__doc__)

    def test_attributes(self):
        """Checks to see if attributes exist"""
        self.assertTrue('id' in self.place.__dict__)
        self.assertTrue('created_at' in self.place.__dict__)
        self.assertTrue('updated_at' in self.place.__dict__)
        self.assertTrue('city_id' in self.place.__dict__)
        self.assertTrue('user_id' in self.place.__dict__)
        self.assertTrue('name' in self.place.__dict__)
        self.assertTrue('description' in self.place.__dict__)
        self.assertTrue('number_of_rooms' in self.place.__dict__)
        self.assertTrue('number_of_bathrooms' in self.place.__dict__)
        self.assertTrue('max_guests' in self.place.__dict__)
        self.assertTrue('price_per_night' in self.place.__dict__)
        self.assertTrue('latitude' in self.place.__dict__)
        self.assertTrue('longitude' in self.place.__dict__)
        self.assertTrue('amenity_ids' in self.place.__dict__)

    def test_subclass(self):
        """Checks to see if it is a subclass of BaseModel"""
        self.assertTrue(issubclass(self.place.__class__, BaseModel), True)

    def test_attribute_types(self):
        """Checks for the attributes types"""
        self.assertTrue(type(self.place.city_id), str)
        self.assertTrue(type(self.place.user_id), str)
        self.assertTrue(type(self.place.name), str)
        self.assertTrue(type(self.place.description), str)
        self.assertTrue(type(self.place.number_of_rooms), int)
        self.assertTrue(type(self.place.number_of_bathrooms), int)
        self.assertTrue(type(self.place.max_guests), int)
        self.assertTrue(type(self.place.price_per_night), int)
        self.assertTrue(type(self.place.latitude), float)
        self.assertTrue(type(self.place.longitude), float)
        self.assertTrue(type(self.place.amenity_ids), list)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") == 'db', 'DB')
    def test_save(self):
        """Tests to see if save works"""
        self.place.save()
        self.assertNotEqual(self.place.created_at, self.place.updated_at)

    def test_to_dict(self):
        """Tests to see if to_dict works"""
        self.assertEqual('to_dict' in dir(self.place), True)

if __name__ == "__main__":
    unittest.main()
