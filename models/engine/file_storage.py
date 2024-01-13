#!/usr/bin/python3
import json
from models.base_model import BaseModel

"""contains the class FileStorge"""


class FileStorage:
    """
    serializes instances to a JSON file and
    deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""

        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""

        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""

        serialized_objects_dict = dict()
        for key, obj in self.__objects.items():
            serialized_objects_dict[key] = obj.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(serialized_objects_dict, file)

    def reload(self):
        """deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ;
        otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised)"""

        try:
            with open(self.__file_path, "r", encoding="utf-8") as file:
                loaded_obj = json.load(file)
            for key, value in loaded_obj.items():
                self.__objects[key] = BaseModel(**value)
        except FileNotFoundError:
            pass
