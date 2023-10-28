#!/usr/bin/python3
"""City class that inherits from Base Model"""
from models.base_model import BaseModel


class City(BaseModel):
    """city class"""
    name = ""
    state_id = ""

    def __init__(self, *args, **kwargs):
        """init method"""
        super().__init__(*args, **kwargs)
