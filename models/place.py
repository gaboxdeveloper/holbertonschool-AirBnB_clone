#!/usr/bin/python3
"""Place class that inherits from Base Model"""
from base_model import BaseModel

class Place(BaseModel):
    """state class"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        name = ""
        city_id = ""
        user_id = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []
