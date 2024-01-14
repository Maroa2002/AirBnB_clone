#!/usr/bin/python3
"""amenity unittesting"""

import unittest


class TestAmmenity(unittest.TestCase):
    """class TestAmenity"""

    def test_checking_for_attributes(self):
        """checking for attributes"""

        self.assertTrue('id' in self.amenity1.__dict__)
        self.assertTrue('created_at' in self.amenity1.__dict__)
        self.assertTrue('updated_at' in self.amenity1.__dict__)
        self.assertTrue('name' in self.amenity1.__dict__)
