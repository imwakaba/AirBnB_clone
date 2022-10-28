#!/usr/bin/python3
"""Module that Define city class"""
from models.base_model import BaseModel

class City(BaseModel):
    """defines city to look for"""
    state_id = ""
    name = ""
