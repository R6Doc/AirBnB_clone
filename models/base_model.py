#!/usr/bin/python3
from datetime import datetime
import uuid


class BaseModel:
    """ Class Base """

    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

    def __str__(self):
        """ Returns the string representation """
        return "[{}] ({}) {} ".format(self.__class__.__name__,
                                      self.id,
                                      self.__dict__)

    def save(self):
        """ Update the updatet_at attribute """
        self.updated_at = datetime.today()

    def to_dict(self):
        my_dict = self.__dict__.copy()
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        my_dict["__class__"] = self.__class__.__name__
        return my_dict
