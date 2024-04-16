#!/usr/bin/python3
"""
This modules determines the type of storage and instantiate and initialize
it accordingly
"""
from os import environ
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


if environ['HBNB_TYPE_STORAGE'] == 'db':
    # storage type is database storage
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()

else:
    # storage type is file storage
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()
