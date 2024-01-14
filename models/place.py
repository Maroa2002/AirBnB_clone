#!/usr/bin/pythpn3
"""class Place"""

from models.base_model import BaseModel


class Place(BaseModel):
    """inherits from BaseModel"""

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.00
    longitude = 0.00
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """initialize Place instance"""
        super().__init__(*args, **kwargs)
