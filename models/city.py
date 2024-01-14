#!/usr/bin/pythpn3
"""class City"""

from models.base_model import BaseModel


class City(BaseModel):
    """inherits from BaseModel"""

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """initialize City instance"""
        super().__init__(*args, **kwargs)
