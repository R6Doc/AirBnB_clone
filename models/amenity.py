#!/usr/bin/python3
"""Class Amenity"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity"""
    name = ""

    def __init__(self, *args, **kwargs):
        """Init Amenity"""
        super().__init__(*args, **kwargs)
