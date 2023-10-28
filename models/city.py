#!/usr/bin/python3
"""City class that inherits from Base Model"""
from base_model import BaseModel

class City(BaseModel):
    """state class"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        name = ""
        state_id = ""
