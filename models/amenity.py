#!/usr/bin/python3
"""Amenity class that inherits from Base Model"""
from base_model import BaseModel

class Amenity(BaseModel):
    """state class"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        name = ""
