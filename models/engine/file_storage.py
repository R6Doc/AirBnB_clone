#!/usr/bin/python3
"""Contains the FileStorage class"""

import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class FileStorage:
    """Serialization to JSON"""

    def all(self):
        """Return dict _objects"""
        pass

    def new(self):
        """sets in __objects the obj with key <obj class name>.id"""
        pass

    def save(self):
        """Serializa objs in JSON"""
        pass

    def reload(self):
        """ deserializes the JSON file to __objects"""
        pass
