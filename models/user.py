#!/usr/bin/python3

"""User Module:
Inherits from Superclass BaseModel
"""

from models.base_model import BaseModel


class User(BaseModel):
    """User class that inherits from BaseModel.
    creates the profile for the user user"""
    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""
