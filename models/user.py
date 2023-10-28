#!/usr/bin/python3
"""user that inherits from base model"""
from models.base_model import BaseModel


class User(BaseModel):
    """class user"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
    
    def __init__(self, *args, **kwargs):
        """init method"""
        super().__init__(*args, **kwargs)