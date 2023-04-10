'''This file contains the model for the request body'''

from typing import Optional
from pydantic import BaseModel #pylint: disable=no-name-in-module

class Unit(BaseModel):
    '''A model of a unit datacard'''
    unit: str
    power: int
    description: list
    model: dict
    equipment: dict
    weapons: dict
    other_wargear: Optional[dict]
    wargear_options: Optional[dict]
    abilities: dict
    command_authority: Optional[dict]
    keywords: dict

class UpdatedUnit(BaseModel):
    '''A model of a unit datacard'''
    unit: Optional[str] = None
    power: Optional[int] = None
    description: Optional[list] = None
    model: Optional[dict] = None
    equipment: Optional[dict] = None
    weapons: Optional[dict] = None
    other_wargear: Optional[dict] = None
    wargear_options: Optional[dict] = None
    abilities: Optional[dict] = None
    command_authority: Optional[dict] = None
    keywords: Optional[dict] = None
