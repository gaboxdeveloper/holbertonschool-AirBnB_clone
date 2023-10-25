#!/usr/bin/python3
"""Base model defining all common attributes/methods for other classes"""
import json


class FileStorage:
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
        """save method"""
        with open(self.__file_path, "w") as f:
            json.dump(self.__objects, f)

    def reload(self):
        try:
            with open(self.__file_path, "r") as f:
                self.__objects = json.load(f)
        except:
            pass
