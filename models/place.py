#!/usr/bin/python3
"""Class Place"""
from models.base_model import BaseModel


class Place(BaseModel):
	"""A place"""
	city_id = ""
	user_id = ""
	name = ""
	description = ""
	number_rooms = 0
	number_bathrooms = 0
	max_guest = 0
	price_by_night = 0
	latitude = 0
	longitude = 0
	amenity_aids = []

	def __init__(self, *args, **kwargs):
		"""Init Place"""
		super().__init__(*args, **kwargs)
