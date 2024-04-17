#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
import models


class State(BaseModel):
    """ State class """
    name = ''

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
