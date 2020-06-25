#!/usr/bin/python3
from datetime import datetime
import uuid


class BaseModel:
    """ Class Base """

    def __init__(self, id, created_at, updated_at):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = created_at

    def __str__ (self):
        """ Returns the string representation """
        return "{[<>]} {(<>)} {<>} ".format(self.__class__.__name__,
                                            self.id,
                                            self.__dict__)

    def save(self):
        """ Update the updatet_at attribute """
        self.updated_at = datetime.now()

    def to_dict(self):
        return (
            {
                "id":self.id,
                
                created_at = created_at.strftime(time)
            }
        )




print(BaseModel.__dict__)


