#!/usr/bin/python3
"""place unittesting"""

import unittest


class TestPlace(unittest.TestCase):
    """class TestPlace"""

    def test_checking_for_attributes(self):
        """checking for attributes"""

        self.assertTrue('id' in self.place1.__dict__)
        self.assertTrue('created_at' in self.place1.__dict__)
        self.assertTrue('updated_at' in self.place1.__dict__)
        self.assertTrue('city_id' in self.place1.__dict__)
        self.assertTrue('user_id' in self.place1.__dict__)
        self.assertTrue('name' in self.place1.__dict__)
        self.assertTrue('description' in self.place1.__dict__)
        self.assertTrue('number_rooms' in self.place1.__dict__)
        self.assertTrue('number_bathrooms' in self.place1.__dict__)
        self.assertTrue('max_guest' in self.place1.__dict__)
        self.assertTrue('price_by_night' in self.place1.__dict__)
        self.assertTrue('latitude' in self.place1.__dict__)
        self.assertTrue('longitude' in self.place1.__dict__)
        self.assertTrue('amenity_ids' in self.place1.__dict__)
