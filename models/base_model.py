#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime


class BaseModel:
    """A base class for all hbnb models"""
    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if len(kwargs) != 0:
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            for key, value in kwargs.items():
                if key in ["updated_at", "created_at"]:
                    dts = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    self.__dict__[key] = dts
                elif key == '__class__':
                    pass
                else:
                    self.__dict__[key] = value
            if 'created_at' not in kwargs:
                self.__dict__['created_at'] = datetime.now()
                self.__dict__['updated_at'] = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
