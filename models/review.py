#!/usr/bin/python3
"""Module theat define reviwm class"""
from models.base_model import BaseModel

class Review(BaseModel):
    """Reviews made by users about a place"""
    place_id = ""
    user_id = ""
    text = ""
