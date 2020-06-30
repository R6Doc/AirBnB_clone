#!/usr/bin/python3
"""Class Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Init Review"""
        super().__init__(*args, **kwargs)
