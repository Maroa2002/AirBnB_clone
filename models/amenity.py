#!/usr/bin/pythpn3
"""class Amenity"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """inherits from BaseModel"""

    name = ""

    def __init__(self, *args, **kwargs):
        """initialize Amenity instance"""
        super().__init__(*args, **kwargs)
