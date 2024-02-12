#!/usr/bin/python3

import uuid
from datetime import datetime
import models

class BaseModel:
    """ Defines all common attributes/methods for other classes """

    def __init__(self):
        """Initializes a new instance of the Base Model"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()

    def __str__(self) -> str:
        """Returns the string representation of an instance"""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """Updates the public instance attribute 'updated_at' with current datetime."""
        self.updated_at = datetime.now()

    def to_dict(self) -> dict:
        """returns dictionary containing keys/values of the instance"""
        dict_repr = self.__dict__.copy()
        dict_repr['__class__'] = self.__class__.__name__
        dict_repr['created_at'] = self.created_at.isoformat()
        dict_repr['updated_at'] = self.updated_at.isoformat()
        return dict_repr
