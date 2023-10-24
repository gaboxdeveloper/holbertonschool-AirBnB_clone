#!/usr/bin/python3
"""Base model defining all common attributes/methods for other classes"""
import datetime
import uuid


class BaseModel:
    """Base model class"""
    id = str(uuid.uuid4())
    created_at = datetime.datetime.now()
    updated_at = datetime.datetime.now()

    def __str__(self):
        """returning string representation"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.to_dict()}"

    def save(self):
        """save current """
        return self.updated_at

    def to_dict(self):
        """to dict method"""
        self.updated_at.isoformat("T")
        self.created_at.isoformat("T")
        dictionary = {
            'my_number': self.my_number,
            'name': self.name,
            'updated_at': self.updated_at,
            'id': self.id,
            'created_at': self.created_at,
        }
        return dictionary
