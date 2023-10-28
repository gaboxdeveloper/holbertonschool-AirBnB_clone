#!/usr/bin/python3
"""State class that inherits from Base Model"""
from base_model import BaseModel

class State(BaseModel):
    """state class"""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
