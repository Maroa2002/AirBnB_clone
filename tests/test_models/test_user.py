#!/usr/bin/python3
"""user unittesting"""

import unittest


class TestUser(unittest.TestCase):
    """class TestUser"""

    def test_checking_for_attributes(self):
        """checking for attributes"""

        self.assertTrue('email' in self.my_user.__dict__)
        self.assertTrue('id' in self.my_user.__dict__)
        self.assertTrue('created_at' in self.my_user.__dict__)
        self.assertTrue('updated_at' in self.my_user.__dict__)
        self.assertTrue('password' in self.my_user.__dict__)
        self.assertTrue('first_name' in self.my_user.__dict__)
        self.assertTrue('last_name' in self.my_user.__dict__)
