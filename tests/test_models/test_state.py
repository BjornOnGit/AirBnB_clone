#!/usr/bin/env python3
"""Unittest for State class"""

import unittest
import os
from models.state import State
from models.base_model import BaseModel

class TestingState(unittest.TestCase):
    """This tests the state class"""

    @classmethod
    def setUpClass(cls):
        """set up before every test method"""
        cls.state = State()
        cls.state.name = "California"

    @classmethod
    def teardown(cls):
        """remove test instances"""
        del cls.state

    def tearDown(self):
        """remove test instances"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_checking_for_docstring(self):
        """checking for docstrings"""
        self.assertIsNotNone(State.__doc__)

    def test_attributes(self):
        """checking if attributes exist"""
        self.assertTrue('name' in self.state.__dict__)
        self.assertTrue('id' in self.state.__dict__)
        self.assertTrue('created_at' in self.state.__dict__)
        self.assertTrue('updated_at' in self.state.__dict__)

    def test_subclass(self):
        """checks if it is a subclass"""
        self.assertTrue(issubclass(self.state.__class__, BaseModel), True)

    def test_attribute_types(self):
        """testing if attribute types are correct"""
        self.assertEqual(type(self.state.name), str)

    def test_save(self):
        """tests if save method works"""
        self.state.save()
        self.assertNotEqual(self.state.created_at, self.state.updated_at)

    def test_to_dict(self):
        """tests if to_dict method works"""
        self.assertEqual('to_dict' in dir(self.state), True)

if __name__ == "__main__":
    unittest.main()
