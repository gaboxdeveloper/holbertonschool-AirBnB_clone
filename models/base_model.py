#!/usr/bin/python3
"""Base model defining all common attributes/methods for other classes"""
from datetime import datetime
import uuid
from models import storage


class BaseModel:
    """Base model class"""
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            self.my_number = None
            self.name = None
            storage.new()

    def __str__(self):
        """returning string representation"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """save current """
        storage.save(self)
        self.updated_at = datetime.now()
        return self.updated_at

    def to_dict(self):
        """to dict method"""
        self.created_at_iso = self.created_at.isoformat()
        self.updated_at_iso = self.updated_at.isoformat()
        dictionary = {
            'my_number': self.my_number,
            'name': self.name,
            '__class__': self.__class__.__name__,
            'updated_at': self.updated_at_iso,
            'id': self.id,
            'created_at': self.created_at_iso
        }
        return dictionary
