#!/usr/bin/python3
"""
The magic file that makes a folder to be a package
"""

from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
