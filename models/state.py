#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", back_populates="state",
                          cascade='all, delete, delete-orphan')

    @property
    def cities(self):
        """
        returns the list of City instances with state_id
        equals to the current State.id
        """

        all_models = models.storage.all()
        city_instances = []
        for model in all_models():
            for obj in model.values():
                if type(obj) == City and obj.state_id == self.id:
                    city_instances.append(obj)
        return (city_instances)
