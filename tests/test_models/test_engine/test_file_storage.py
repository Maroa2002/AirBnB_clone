#!/usr/bin/python3
"""filestorage testing"""

import unittest
from models.engine.file_storage import FileStorage
from models import storage


class TestFileStorage(unittest.TestCase):
    """class TestFileStorage"""

    def test_type(self):
        """type checks for FileStorage
        """
        self.assertIsInstance(storage, FileStorage)
        self.assertEqual(type(storage), FileStorage)
