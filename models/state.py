#!/usr/bin/pythpn3
"""class State"""

from models.base_model import BaseModel


class State(BaseModel):
    """inherits from BaseModel"""

    name = ""

    def __init__(self, *args, **kwargs):
        """initialize State instance"""
        super().__init__(*args, **kwargs)
