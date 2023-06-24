#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
import models
import sqlalchemy
# from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    if models.storage_type == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                              cascade="all, delete, delete-orphan")
    else:
        name = ""

        @property
        def cities(self):
            """
            Return the list of ``City`` instances with ``state_id`` equal to
            the current ``State.id``
            """
            return [value for key, value in models.storage.all().items()
                    if key.split(".")[0] == "City"
                    and value.state_id == self.id]
