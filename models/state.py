#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
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
        for model in all_models():
            for key, value in model.items():
                
