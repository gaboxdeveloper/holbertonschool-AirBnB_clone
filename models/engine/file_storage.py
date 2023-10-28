#!/usr/bin/python3
"""Base model defining all common attributes/methods for other classes"""
import json


class FileStorage():
    """File Sotrage Class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return all dictionary"""
        return self.__objects

    def new(self, obj):
        """new method"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        try:
            formato_dict = {}
            for key, value in self.__objects.items():
                formato_dict[key] = value.to_dict()
            with open(self.__file_path, 'w') as f:
                json.dump(formato_dict, f, indent=4)
        except AttributeError:
            pass

    def classeneitor(self, class_name):
        if class_name == 'BaseModel':
            from models.base_model import BaseModel
            return BaseModel
        if class_name == 'User':
            from models.user import User
            return User
        if class_name == 'City':
            from models.city import City
            return City
        if class_name == 'Place':
            from models.place import Place
            return Place
        if class_name == 'State':
            from models.state import State
            return State
        if class_name == 'Review':
            from models.review import Review
            return Review
        if class_name == 'Amenity':
            from models.amenity import Amenity
            return Amenity

    def reload(self):
        try:
            with open(self.__file_path, 'r') as file:
                formato_dict = json.load(file)
                for key, value in formato_dict.items():
                    Class = self.classeneitor(value['__class__'])
                    instance = Class(**value)
                    self.__objects[key] = instance
        except FileNotFoundError:
            pass
