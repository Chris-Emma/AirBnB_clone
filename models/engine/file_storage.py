#!/usr/bin/python3

"""
    a class FileStorage that serializes
    instances to a JSON file and deserializes
    JSON file to instances:
"""
import json
from os import path
from models.base_model import BaseModel

class FileStorage:

    """
        Private class attributes:
    __file_path: string - path to the JSON file
    __objects: dictionary - empty but will store all objects by <class name>.id
    """

    CLASSES = {
            'BaseModel': BaseModel
    }

    __file_path = "file.json"
    __objects = {} #dict to store all objects by <class_name>.id

    def all(self):
        """ returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, 'w') as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects.
        Only if the JSON file (__file_path) exists; otherwise, do nothing.
        No exemption if the file is empty
        """
        if path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding="utf-8") as file:
                serialized_objects = json.load(file)
                for key, obj_data in serialized_objects.items():
                    class_name, obj_id = key.split('.')
                    # create an instance of
                    # the class based on class_name dynamically
                    obj_class = globals()[class_name]
                    obj_instance = obj_class(**obj_data)
                    # Store the instance in __objects
                    self.__objects[key] = obj_instance
