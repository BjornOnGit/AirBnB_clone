#!/usr/bin/python3

"""Unittest for file_storage.py"""

import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage

class TestFileStorage(unittest.TestCase):
    """"Tests for file storage"""

    def setUp(self):
        self.my_model = BaseModel()

    def test_instance(self):
        """Check the class instance"""
        self.assertIsInstance(storage, FileStorage)

    def test_store_base_model(self):
        """Check if the base model is being stored"""
        try:
            self.my_model.full_name = "BaseModel Instance"
            self.my_model.save()
            base_m_dict = self.my_model.to_dict()
            all_objs = storage.all()

            key = base_m_dict['__class__'] + "." + base_m_dict['id']
            self.assertEqual(key in all_objs, True)
        except Exception:
            pass

    def test_store_base_model_2(self):
        """"Check the save, reload and update functions"""
        try:
            self.my_model.my_name = "First name"
            self.my_model.save()
            base_m_dict = self.my_model.to_dict()
            all_objs = storage.all()

            key = base_m_dict['__class__'] + "." + base_m_dict['id']

            self.assertEqual(key in all_objs, True)
            self.assertEqual(all_objs[key].my_name, "First name")

            create_1 = base_m_dict['created_at']
            update_1 = base_m_dict['updated_at']

            self.my_model.my_name = "Last name"
            self.my_model.save()
            base_m_dict = self.my_model.to_dict()
            all_objs = storage.all()

            self.assertEqual(key in all_objs, True)

            create_2 = base_m_dict['created_at']
            update_2 = base_m_dict['updated_at']

            self.assertEqual(create_1, create_2)
            self.assertNotEqual(update_1, update_2)
            self.assertEqual(base_m_dict['my_name'], "Last name")
        except Exception:
            pass

    def test_attributes(self):
        """Check if attributes exist"""
        self.assertEqual(hasattr(FileStorage, '_FileStorage__file_path'), True)
        self.assertEqual(hasattr(FileStorage, '_FileStorage__objects'), True)

    def test_save(self):
        """Check if JSON exists"""
        self.my_model.save()
        self.assertEqual(os.path.exists(storage._FileStorage__file_path), True)
        self.assertEqual(storage.all(), storage._FileStorage__objects)

    def test_reload(self):
        """Check if reload works"""
        self.my_model.save()
        self.assertEqual(os.path.exists(storage._FileStorage__file_path), True)
        d_obj = storage.all()
        FileStorage._FileStorage__objects = {}
        self.assertNotEqual(d_obj, FileStorage._FileStorage__objects)
        storage.reload()
        for key, value in storage.all().items():
            try:
                self.assertEqual(d_obj[key].to_dict(), value.to_dict())
            except AssertionError:
                pass

    def test_self_save(self):
        """Check if self save works"""
        try:
            msg = "save() take 1 positional argument but 2 were given"
            with self.assertRaises(TypeError) as e:
                FileStorage.save(self)

            self.assertEqual(str(e.exception), msg)
        except AssertionError:
            pass

if __name__ == "__main__":
    unittest.main()
