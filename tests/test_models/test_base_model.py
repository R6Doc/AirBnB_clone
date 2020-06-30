#!/usr/bin/python3
"""
Test BaseModel
"""

import unittest
import models
from models.base_model import BaseModel
from datetime import datetime
from time import sleep


class TestBaseModel(unittest.TestCase):
    """Diferent cases to test BaseModel Class"""

    def test_noargs(self):
        """basemodel exists without any arg"""
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_id(self):
        """test id id exists"""
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at(self):
        """test if created at exists and have correct dateform"""
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at(self):
        """test id updated_at exists and have correct dateform"""
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_dict(self):
        """test id to_dict exist when we create a new instance(tester)"""
        tester = BaseModel()
        self.assertTrue(dict, type(tester.to_dict()))

    def test_dict_content(self):
        """test if dict contain correct attributes"""
        tester = BaseModel()
        self.assertIn("id", tester.to_dict())
        self.assertIn("created_at", tester.to_dict())
        self.assertIn("updated_at", tester.to_dict())

    def test_different_ids(self):
        """test if 2 instances have different ids attributes"""
        tester1 = BaseModel()
        tester2 = BaseModel()
        self.assertNotEqual(tester1.id, tester2, id)

    def test_different_times(self):
        """test if created_at and updated_at are different in 2 instances"""
        tester1 = BaseModel()
        sleep(0.01)
        tester2 = BaseModel()
        self.assertNotEqual(tester1.created_at, tester2.created_at)
        self.assertNotEqual(tester1.updated_at, tester2.updated_at)

    def test_save(self):
        """test save"""
        tester1 = BaseModel()
        updt = tester1.updated_at
        sleep(0.2)
        tester1.save()
        self.assertNotEqual(tester1.updated_at, updt)

    def test_str(self):
        """Test __str___"""
        date1 = datetime.today()
        tester1 = BaseModel()
        tester1.id = 821983719274
        tester1.created_at = date1
        tester1.updated_at = date1
        testerstr = tester1.__str__()
        self.assertIn("[BaseModel] (821983719274)", testerstr)
        self.assertIn("'id': 821983719274", testerstr)
        self.assertIn("'created_at': " + repr(date1), testerstr)
        self.assertIn("'updated_at': " + repr(date1), testerstr)