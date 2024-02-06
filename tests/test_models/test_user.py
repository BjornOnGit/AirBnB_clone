#!/usr/bin/python3
"""Unittest for User class"""

import unittest
import datetime
from models.user import User
from models.base_model import BaseModel

class TestingUser(unittest.TestCase):
    """Tests instances and methods from user class"""

    def setUp(self):
        """sets up the test"""
        self.user = User()

    def test_class_exists(self):
        """checks if class exists"""
        ret_dict = self.user.to_dict()
        self.assertEqual(ret_dict["__class__"], "User")

    def test_inheritance(self):
        """checks if class inherits from BaseModel"""
        self.assertIsInstance(self.user, BaseModel)

    def test_attributes(self):
        """checks if attributes exist"""
        self.assertTrue(hasattr(self.user, "email"))
        self.assertTrue(hasattr(self.user, "password"))
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertTrue(hasattr(self.user, "last_name"))
        self.assertTrue(hasattr(self.user, "id"))
        self.assertTrue(hasattr(self.user, "created_at"))
        self.assertTrue(hasattr(self.user, "updated_at"))

    def test_types(self):
        """checks if attributes are of the right type"""
        self.assertIsInstance(self.user.email, str)
        self.assertIsInstance(self.user.password, str)
        self.assertIsInstance(self.user.first_name, str)
        self.assertIsInstance(self.user.last_name, str)
        self.assertIsInstance(self.user.id, str)
        self.assertIsInstance(self.user.created_at, datetime.datetime)
        self.assertIsInstance(self.user.updated_at, datetime.datetime)

if __name__ == "__main__":
    unittest.main()
