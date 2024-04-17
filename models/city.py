#!/usr/bin/python3
""" City Module for HBNB project """

from models.base_model import BaseModel
import models


class City(BaseModel):
    """
    City Class
    Attributes:
        state_id: The state id
        name: input name
    """

    name = '' 
    state_id = ''
