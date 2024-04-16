#!/usr/bin/python3
"""
Defines a database engine
"""
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm.session import sessionmaker, Session
from os import getenv


class DBStorage:
    """A database storage class"""
    __engine = None
    __session = None

    def __init__(self):
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        db = getenv("HBNB_MYSQL_DB")
        host = getenv("HBNB_MYSQL_HOST")
        env = getenv("HBNB_ENV")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, passwd, host, db),
                                      pool_pre_ping=True)

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        query on the current database session (self.__session) all
        objects depending of the class name (argument cls)

        Return:
            dictionary of objects
        """

        objects = {}
        all_class_models = {'State': State, 'City': City,
                            'User': User, 'Place': Place,
                            'Review': Review, 'Amenity': Amenity}

        if cls:
            for row in self.__session.query(cls).all():
                # create an object in the format <class-name>.<object-id>
                objects.update({'{}.{}'.
                                format(type(cls).__name__, row.id,): row})
        else:
            for key, val in all_class_models.items():
                for row in self.__session.query(val):
                    objects.update({'{}.{}'.
                                    format(type(row).__name__, row.id,): row})
        return objects

    def new(self, obj):
        """
        adds' a new model to the database
        """
        self.__session.add(obj)

    def save(self):
        """
        save changes to the database
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        delete a model from the database
        """
        if obj:
            self.session.delete(obj)

    def reload(self):
        """
        create all the schemas of the model to the database and initialize
        the session
        """
        Base.metadata.create_all(self.__engine)
        smaker = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(smaker)
        self.__session = Session()

    def close(self):
        """
        release all the resources held by the session and
        terminate the connection
        """
        self.__session.close()
