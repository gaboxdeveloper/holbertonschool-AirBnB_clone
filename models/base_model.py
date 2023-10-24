#!/usr/bin/python3
"""Base model defining all common attributes/methods for other classes"""
import datetime
import uuid


class BaseModel:
    """Base model class"""
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """returning string representation"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """save current """
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
