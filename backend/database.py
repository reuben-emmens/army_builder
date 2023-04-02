'''This file contains the database connection and functions to interact with the database.'''

import os

import motor.motor_asyncio
from dotenv import load_dotenv

from .model import Unit  # pylint: disable=relative-beyond-top-level

load_dotenv()
cnxn_string = os.getenv('CNXN_STRING')

client = motor.motor_asyncio.AsyncIOMotorClient(cnxn_string)
database = client.UnitsList
collection = database.Units

async def fetch_one_unit(unit):
    '''This function fetches a single unit from the database'''
    document = await collection.find_one({"unit": unit})
    return document

async def fetch_all_units():
    '''This function fetches all units from the database'''
    units = []
    cursor = collection.find({})
    async for document in cursor:
        units.append(Unit(**document))
    return units

async def create_unit(unit):
    '''This function creates a new unit in the database'''
    document = unit
    result = await collection.find_one({"unit": document["unit"]})
    if result is None:
        await collection.insert_one(document)
        return document
    else:
        raise ValueError("Unit already exists")

async def update_unit(unit, data):
    '''This function updates a unit in the database'''
    await collection.update_one({"unit": unit}, {"$set": {"power": data}})
    document = await collection.find_one({"unit": unit})
    return document

async def remove_unit(unit):
    '''This function removes a unit from the database'''
    await collection.delete_one({"unit": unit})
    return True
