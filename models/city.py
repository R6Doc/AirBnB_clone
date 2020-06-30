#!/user/bin/python3
"""Class City"""
from models.base_model import BaseModel


class City(BaseModel):
    """A city"""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Init City"""
        super().__init__(*args, **kwargs)
