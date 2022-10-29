#!/usr/bin/python3

"""
making file storage available everywhere
"""

from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
