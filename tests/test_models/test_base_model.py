#!/usr/bin/ env python3
"""Unit tests for Base Model class"""

import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestingBaseModel(unittest.TestCase):
    """This will test the BaseModel class"""

    def setUp(self):
        try:
            self.created_baz1 = round(datetime.now().timestamp())
            self.baz1 = BaseModel()
            self.baz2 = BaseModel()
        except Exception as e:
            print(e)

    def tearDown(self):
        """Tidies up after each test method has been run"""
        try:
            del self.baz1
            del self.baz2
        except Exception as e:
            print(e)

    def test_init(self):
        """Checks if the instance is properly created"""
        try:
            self.assertEqual(type(self.baz1.id).__name__, "str")
            self.assertNotEqual(self.baz1.id, self.baz2.id)
            self.assertEqual(self.baz1.created_at.timestamp(), self.baz1.updated_at.timestamp())
            self.assertEqual(type(self.baz1.created_at).__name__, "datetime")
            self.assertAlmostEqual(round(self.baz1.created_at.timestamp()), self.created_baz1)
        except Exception as e:
            print(e)

    def test_save(self):
        """Checks if the save method works"""
        try:
            updated_baz1 = round(datetime.now().timestamp())
            self.baz1.save()
            self.assertAlmostEqual(round(self.baz1.updated_at.timestamp()), updated_baz1)
        except Exception as e:
            print(e)

    def test_dict(self):
        """Checks if the to_dict method works"""
        try:
            baz1_dict = self.baz1.to_dict()
            self.assertEqual(baz1_dict["__class__"], "BaseModel")
            self.assertEqual(baz1_dict["created_at"], self.baz1.created_at.isoformat())
            self.assertEqual(baz1_dict["updated_at"], self.baz1.updated_at.isoformat())
        except Exception as e:
            print(e)

if __name__ == "__main__":
    unittest.main()
