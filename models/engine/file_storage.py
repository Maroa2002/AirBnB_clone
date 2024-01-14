#!/usr/bin/python3
"""contains the class FileStorge"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    serializes instances to a JSON file and
    deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}
    classes = {"BaseModel": BaseModel, "User": User, "Place": Place,
               "Amenity": Amenity, "City": City, "Review": Review,
               "State": State}

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

    def serialize(self):
        """Serialize __objects to a JSON file"""

        serialized = {}
        for key, value in self.__objects.items():
            serialized[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(serialized, file)

    def deserialize(self):
        """Deserialize the JSON file to __objects"""

        try:
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name = value['__class__']
                    obj = eval(class_name)(**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
