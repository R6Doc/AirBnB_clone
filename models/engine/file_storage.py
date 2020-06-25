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
    __file_path = "file.json"
    __objects = {}
    """Serialization to JSON"""


    def all(self):
        """Return dict _objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj:
            classname = obj.__class__.__name__
            self.__objects["{}.{}".format(classname, obj.id)] = obj

    def save(self):
        """Serializa objs in JSON"""
        jsonObjects = []
        for key in self.__objects.keys():
            jsonObjects[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(jsonObjects, f)

    def reload(self):
        """ deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, "r") as f:
                objson = json.load(f)
                for dicts in objson.values():
                    self.new(self, dicts)
        except FileNotFoundError:
            return
