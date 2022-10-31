#!/usr/bin/python3
from models.base_model import BaseModel

"""Inherits from the BaseModel class"""


class Review(BaseModel):
    """Public class attributes:
    place_id: string - empty string: it will be the Place.id
    user_id: string - empty string: it will be the User.id
    text: string - empty string
    """
    place_id = ""
    user_id = ""
    text = ""
