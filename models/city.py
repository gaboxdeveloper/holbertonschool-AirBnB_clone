#!/usr/bin/python3
"""City class that inherits from Base Model"""
from base_model import BaseModel


class City(BaseModel):
    """state class"""
    name = ""
    state_id = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
