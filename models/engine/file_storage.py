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
        formato_dict = {}
        for key, value in self.__objects.items():
            formato_dict[key] = value.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(formato_dict, f)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as file:
                formato_dict = json.load(file)
                for key, value in formato_dict.items():
                    self.__objects[value] = value
        except FileNotFoundError:
            pass
