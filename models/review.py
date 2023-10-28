#!/usr/bin/python3
"""Review class that inherits from Base Model"""
from base_model import BaseModel

class Review(BaseModel):
    """state class"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        place_id = ""
        user_id = ""
        text = ""