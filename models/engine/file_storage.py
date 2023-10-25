#!/usr/bin/python3
"""Base model defining all common attributes/methods for other classes"""
import json

class FileStorage:
    """File Sotrage Class"""
    __file_path = "file.json"
    objects = {}
        
    def all(self):
        """Return all dictionary"""
        return object
    
    def new(self, obj):
        """"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj
    
    def save(self):
        """a"""
        with open("__objects.json", "w") as __file_path:
            json.dump(self.__objects, __file_path)
            