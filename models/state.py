#!/usr/bin/python3

"""Iinherits from the  base model"""
from models.base_model import BaseModel


class State(BaseModel):
    """Has attributes unique to the state class"""
    name = ""
