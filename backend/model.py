from typing import Optional
from pydantic import BaseModel

class Unit(BaseModel):
    '''Allows the request body to be parsed into a python object'''
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
