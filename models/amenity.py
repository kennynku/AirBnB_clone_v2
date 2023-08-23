#!/usr/bin/python3
""" Amenity class """
import os
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from models.base_model import BaseModel, Base


class Amenity(BaseModel, Base):
    """Amenity class set"""
    __tablename__ = 'amenities'
    name = Column(
        String(128), nullable=False
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
