#!/usr/bin/python3
"""Review class that inherits from Base Model"""
from models.base_model import BaseModel


class Review(BaseModel):
    """review class"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """init method"""
        super().__init__(*args, **kwargs)
