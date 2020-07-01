#!/usr/bin/python3
""" Test city """

import unittest
import models
from models.city import City
from models.base_model import BaseModel


class city_tests(unittest.TestCase):
    """ Test for city file """

    def test_city(self):
        """ Test the city subclass """
        instance = City()
        self.assertIsInstance(instance, BaseModel)
        self.assertTrue(hasattr(instance, "id"))
        self.assertTrue(hasattr(instance, "created_at"))
        self.assertTrue(hasattr(instance, "updated_at"))

    def test_cityout(self):
        """ Tests for the correct output """
        instance = City()
        output = "[City] ({}) {}".format(instance.id, instance.__dict__)
        self.assertEqual(output, str(instance))

    def test_cityname(self):
        """ Test if the name exists """
        instance = City()
        self.assertTrue(hasattr(instance, "name"))
        self.assertEqual(instance.name, "")
        self.assertTrue(hasattr(instance, "state_id"))
        self.assertEqual(instance.state_id, "")
