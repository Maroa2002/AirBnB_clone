#!/usr/bin/python3
"""base_model unittesting"""

import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """class TestBaseModel"""

    def test_for_attributes(self):
        """checking for attributes"""

        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))
