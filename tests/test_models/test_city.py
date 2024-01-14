#!/usr/bin/python3
"""city unittesting"""

import unittest


class TestCity(unittest.TestCase):
    """class TestCity"""

    def test_checking_for_attributes(self):
        """checking for attributes"""

        self.assertTrue('id' in self.city1.__dict__)
        self.assertTrue('created_at' in self.city1.__dict__)
        self.assertTrue('updated_at' in self.city1.__dict__)
        self.assertTrue('state_id' in self.city1.__dict__)
        self.assertTrue('name' in self.city1.__dict__)
