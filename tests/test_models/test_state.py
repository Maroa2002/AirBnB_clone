#!/usr/bin/python3
"""state unittesting"""

import unittest


class TestState(unittest.TestCase):
    """class TestState"""

    def test_checking_for_attributes(self):
        """checking for attributes"""

        self.assertTrue('id' in self.state1.__dict__)
        self.assertTrue('created_at' in self.state1.__dict__)
        self.assertTrue('updated_at' in self.state1.__dict__)
        self.assertTrue('name' in self.state1.__dict__)
