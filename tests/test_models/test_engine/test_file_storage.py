#!/usr/bin/python3
""" Testing of file storage engine"""
import os
import unittest

from models import storage
from models.base_model import BaseModel


@unittest.skipIf(
    os.getenv('HBNB_TYPE_STORAGE') == 'db', 'FileStorage test')
class TestFileStorage(unittest.TestCase):
    """ Definition of storage engine test class"""
    def setUp(self):
        """ Prepare tests env """
        del_list = []
        for key in storage.all().keys():
            del_list.append(key)
        for key in del_list:
            del storage.all()[key]

    def tearDown(self):
        """ Delete files createed by tests """
        try:
            os.remove('file.json')
        except Exception:
            pass

    def test_obj_list_empty(self):
        """ check if __objects is empty """
        self.assertEqual(len(storage.all()), 0)

    def test_new(self):
        """ Test if a new object is added to __objects """
        new = BaseModel()
        new.save()
        for obj in storage.all().values():
            temp = obj
        self.assertTrue(temp is obj)

    def test_all(self):
        """ return of objects  """
        new = BaseModel()
        temp = storage.all()
        self.assertIsInstance(temp, dict)

    def test_base_model_instantiation(self):
        """ Test file file creation failed on save"""
        new = BaseModel()
        self.assertFalse(os.path.exists('file.json'))

    def test_empty(self):
        """ Check if file is not empty """
        new = BaseModel()
        thing = new.to_dict()
        new.save()
        new2 = BaseModel(**thing)
        self.assertNotEqual(os.path.getsize('file.json'), 0)

    def test_save(self):
        """ Save method test """
        new = BaseModel()
        new.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_reload(self):
        """ Storage file starts on objects """
        new = BaseModel()
        new.save()
        storage.reload()
        loaded = None
        for obj in storage.all().values():
            loaded = obj
        self.assertEqual(new.to_dict()['id'], loaded.to_dict()['id'])

    def test_reload_empty(self):
        """ Starts on empty file """
        with open('file.json', 'w') as f:
            pass
        with self.assertRaises(ValueError):
            storage.reload()

    def test_reload_from_nonexistent(self):
        """ fails upon fail existence """
        self.assertEqual(storage.reload(), None)

    def test_base_model_save(self):
        """ Save is called by Base """
        new = BaseModel()
        new.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_type_path(self):
        """ check if file path is str type """
        self.assertEqual(type(storage._FileStorage__file_path), str)

    def test_type_objects(self):
        """ Check if obj id dict """
        self.assertEqual(type(storage.all()), dict)

    def test_key_format(self):
        """ format is prepared for serialization """
        new = BaseModel()
        _id = new.to_dict()['id']
        temp = ''
        new.save()
        for key, value in storage.all().items():
            if value is new:
                temp = key
        self.assertEqual(temp, 'BaseModel' + '.' + _id)

    def test_storage_var_created(self):
        """ Check if storage saved """
        from models.engine.file_storage import FileStorage
        self.assertEqual(type(storage), FileStorage)
