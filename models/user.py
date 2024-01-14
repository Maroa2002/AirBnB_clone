#!/usr/bin/pythpn3
"""class User"""

from models.base_model import BaseModel


class User(BaseModel):
    """inherits from BaseModel"""

    email = ""
    passsword = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """initialize User instance"""
        super().__init__(*args, **kwargs)
