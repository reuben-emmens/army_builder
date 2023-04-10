# pylint: disable=invalid-name relative-beyond-top-level line-too-long broad-exception-raised
'''This file contains the database connection and functions to interact with the database.'''
import os

import motor.motor_asyncio
from dotenv import load_dotenv

from .model import Unit

# Establish connection to the database
load_dotenv()
cnxn_string = os.getenv('CNXN_STRING')
client = motor.motor_asyncio.AsyncIOMotorClient(cnxn_string)
database = client.UnitsList
collection = database.Units

async def create_unit(unit):
    '''This function creates a new unit in the database'''
    fetch_result = await collection.find_one({"unit": unit["unit"]})
    if fetch_result is None:
        create_result = await collection.insert_one(unit)
        if create_result.inserted_id:
            return f'Successfully created {unit["unit"]}'
        raise Exception()
    raise ValueError()

async def fetch_one_unit(unit):
    '''This function fetches a single unit from the database'''
    fetch_result = await collection.find_one({"unit": unit})
    if fetch_result is not None:
        return fetch_result
    raise Exception()

async def fetch_all_units():
    '''This function fetches all units from the database'''
    units = []
    cursor = collection.find({})
    async for document in cursor:
        units.append(Unit(**document))
    if len(units) > 0:
        return units
    raise Exception()

async def update_unit(unit, unit_dictionary):
    '''This function updates a unit in the database'''
    matches = []
    for key in unit_dictionary:
        if unit_dictionary[key] is not None:
            update_result = await collection.update_one({"unit": unit}, {"$set": {key: unit_dictionary[key]}})
            matches.append(update_result.matched_count)
    if sum(matches) > 0:
        return 'Your updates have been successful'
    raise Exception()

async def delete_unit(unit):
    '''This function removes a unit from the database'''
    delete_result = await collection.delete_one({"unit": unit})
    if delete_result.deleted_count > 0:
        return f"Successfully deleted {unit}"
    raise Exception()
