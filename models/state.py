#!/usr/bin/python3
"""State Class"""
from models.base_model import BaseModel


class State(BaseModel):
    """An State"""

    def __init__(self, *args, **kwargs):
        """Init State"""
        super().__init__(*args, **kwargs)
