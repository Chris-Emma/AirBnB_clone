#!/usr/bin/python3

import uuid
from datetime import datetime
import models

class BaseModel:
    """ Defines all common attributes/methods for other classes """

    def __init__(self, *args, **kwargs):
        """Initializes a new Instance of the Base Mode
        - *args: Will not be used
        - **kwargs: a dict containing key-value arguments
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    if not isinstance(value, datetime):
                        value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

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
