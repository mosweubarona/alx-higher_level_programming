#!/usr/bin/python3
"""Definition of the City class"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()
"""
    Module that performs creates a States class based off of Base.
"""


class City(Base):
    """
        The ``City`` class which inherits from ``Base`` class.
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
