from .model import Unit
from dotenv import load_dotenv
import os
import motor.motor_asyncio

load_dotenv()
cnxn_string = os.getenv('CNXN_STRING')

client = motor.motor_asyncio.AsyncIOMotorClient(cnxn_string)
database = client.UnitsList
collection = database.Units

async def fetch_one_unit(unit):
    document = await collection.find_one({"unit": unit})
    return document

async def fetch_all_units():
    units = []
    cursor = collection.find({})
    async for document in cursor:
        units.append(Unit(**document))
    return units

async def create_unit(unit):
    document = unit
    result = await collection.find_one({"unit": document["unit"]})
    if result == None:
        await collection.insert_one(document)
        return document
    else:
        raise Exception("Unit already exists")

async def update_unit(unit, data):
    await collection.update_one({"unit": unit}, {"$set": {"power": data}})
    document = await collection.find_one({"unit": unit})
    return document

async def remove_unit(unit):
    await collection.delete_one({"unit": unit})
    return True