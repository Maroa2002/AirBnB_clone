#!/usr/bin/python3
"""review unittesting"""

import unittest


class TestReview(unittest.TestCase):
    """class TestReview"""

    def test_checking_for_attributes(self):
        """checking for attributes"""

        self.assertTrue('id' in self.rev1.__dict__)
        self.assertTrue('created_at' in self.rev1.__dict__)
        self.assertTrue('updated_at' in self.rev1.__dict__)
        self.assertTrue('place_id' in self.rev1.__dict__)
        self.assertTrue('text' in self.rev1.__dict__)
        self.assertTrue('user_id' in self.rev1.__dict__)
