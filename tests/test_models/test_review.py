#!/usr/bin/env python3
"""Unittest for the Review class"""

import unittest
import os
from os import getenv
from models.review import Review
from models.base_model import BaseModel

class TestingReview(unittest.TestCase):
    """This will test the review class"""

    @classmethod
    def setUpClass(cls):
        """setting up for a test"""
        cls.revw = Review()
        cls.revw.place_id = "235-abcd"
        cls.revw.user_id = "123-efgh"
        cls.revw.text = "This is a review"

    @classmethod
    def teardown(cls):
        """at the end of the test, this tears it down"""
        del cls.revw

    def tearDown(self):
        """tears down the test"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_checking_for_docstring(self):
        """checks for docstrings"""
        self.assertIsNotNone(Review.__doc__)

    def test_attributes(self):
        """checks to see if attributes exist"""
        self.assertTrue('id' in self.revw.__dict__)
        self.assertTrue('created_at' in self.revw.__dict__)
        self.assertTrue('updated_at' in self.revw.__dict__)
        self.assertTrue('place_id' in self.revw.__dict__)
        self.assertTrue('user_id' in self.revw.__dict__)
        self.assertTrue('text' in self.revw.__dict__)

    def test_subclass(self):
        """checks if it is a subclass"""
        self.assertTrue(issubclass(self.revw.__class__, BaseModel), True)

    def test_attribute_types(self):
        """tests attribute type"""
        self.assertEqual(type(self.revw.place_id), str)
        self.assertEqual(type(self.revw.user_id), str)
        self.assertEqual(type(self.revw.text), str)

    @unittest.skipIf(getenv('HBNB_TYPE_STORAGE') == 'db', 'DB')
    def test_save(self):
        """tests save"""
        self.revw.save()
        self.assertNotEqual(self.revw.created_at, self.revw.updated_at)

    def test_to_dict(self):
        """tests to_dict"""
        self.assertEqual('to_dict' in dir(self.revw), True)

if __name__ == "__main__":
    unittest.main()
