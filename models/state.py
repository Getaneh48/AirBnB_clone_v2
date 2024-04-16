#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models
from models.city import City
from os import environ


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", back_populates="state",
                          cascade='all, delete, delete-orphan')

    if environ['HBNB_TYPE_STORAGE'] == 'db':
        cities = relationship('City', cascade='all, delete', backref='state')
    else:
        @property
        def cities(self):
            """
            returns the list of City instances with state_id
            equals to the current State.id
            """

            all_cities = models.storage.all(City)
            city_instances = []
            for city in all_cities.values():
                if city.state_id == self.id:
                    city_instances.append(city)
            return (city_instances)
