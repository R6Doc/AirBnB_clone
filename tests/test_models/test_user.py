#!/usr/bin/python3
""" Test for user """

import unittest
import models
from models.user import User
from models.base_model import BaseModel


class user_tests(unittest.TestCase):
    """ Test for the user file """

    def test_usersub(self):
        """ Test for the subclass user """
        instance = User()
        self.assertIsInstance(instance, BaseModel)
        self.assertTrue(hasattr(instance, "id"))
        self.assertTrue(hasattr(instance, "created_at"))
        self.assertTrue(hasattr(instance, "updated_at"))

    def test_userout(self):
        """ Test the correct output """
        instance = User()
        output = "[User] ({}) {}".format(instance.id, instance.__dict__)
        self.assertEqual(output, str(instance))

    def test_username(self):
        """ Test the name """
        instance = User()
        self.assertTrue(hasattr(instance, "email"))
        self.assertEqual(instance.email, "")
        self.assertTrue(hasattr(instance, "password"))
        self.assertEqual(instance.password, "")
        self.assertTrue(hasattr(instance, "first_name"))
        self.assertEqual(instance.first_name, "")
        self.assertTrue(hasattr(instance, "last_name"))
        self.assertEqual(instance.last_name, "")
