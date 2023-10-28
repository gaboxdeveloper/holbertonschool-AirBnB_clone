#!/usr/bin/python3
"""Amenity class that inherits from Base Model"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """amenity class"""
    name = ""

    def __init__(self, *args, **kwargs):
        """init method"""
        super().__init__(*args, **kwargs)
