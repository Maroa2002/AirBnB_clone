#!/usr/bin/pythpn3
"""class Review"""

from models.base_model import BaseModel


class Review(BaseModel):
    """inherits from BaseModel"""

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """initialize Review instance"""
        super().__init__(*args, **kwargs)
