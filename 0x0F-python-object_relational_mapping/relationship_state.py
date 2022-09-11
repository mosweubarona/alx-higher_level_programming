#!/usr/bin/python3
"""Definition of the State class with relationship to City"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from relationship_city import City, Base
"""
    Module that performs creates a States class based off of Base.
"""

Base = declarative_base()


class State(Base):
    """
        The ``States`` class which inherits from ``Base`` class.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True,
                nullable=False, unique=Truprimary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
