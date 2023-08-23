#!/usr/bin/python3
"""Module contains storage Class"""
import os

from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage

storage = DBStorage() if os.getenv(
    'HBNB_TYPE_STORAGE') == 'db' else FileStorage()
"""A special instance for all model instances.
"""
storage.reload()
