#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import environ
import models


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if environ['HBNB_TYPE_STORAGE'] == 'db':
        cities = relationship('City', cascade='all, delete', backref='state')
    else:
        @property
        def cities(self):
            """
            returns the list of City instances with state_id
            equals to the current State.id
            """

            all_cities = models.storage.all(models.City)
            city_instances = []
            for city in all_cities.values():
                if city.state_id == self.id:
                    city_instances.append(city)
            return (city_instances)
