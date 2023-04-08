'''Test the database functions are functioning correctly with expected outputs'''
import os
import json
import motor.motor_asyncio
import pytest
from dotenv import load_dotenv

# This is the same as using the @pytest.mark.anyio on all test functions in the module
pytestmark = pytest.mark.anyio

@pytest.fixture
def unit():
    '''This function returns a sample unit to test the database functions'''
    file_path = 'static/field_ordnance_battery.json'
    with open(file_path, 'r', encoding='UTF-8') as f: #pylint: disable=invalid-name
        read_file = f.read()
        unit = json.loads(read_file)
        return unit


# @pytest.fixture
# def collection():
#     '''This function establishes a connection to the MongoDB database via the Motor driver.'''
#     load_dotenv()
#     cnxn_string = os.getenv('CNXN_STRING')
#     client = motor.motor_asyncio.AsyncIOMotorClient(cnxn_string)
#     database = client.UnitsList
#     collection_marker = database.Units
#     return collection_marker

async def test_can_connect_to_db(unit):
    '''Tests if a connection can be made to the Units collection'''
    load_dotenv()
    cnxn_string = os.getenv('CNXN_STRING')
    client = motor.motor_asyncio.AsyncIOMotorClient(cnxn_string)
    database = client.UnitsList
    collection = database.Units
    document = await collection.find_one({"unit": "Field Ordnance Battery"})
    assert document[unit] == "Field Ordnance Battery"


# load_dotenv()
# cnxn_string = os.getenv('CNXN_STRING')
# client = motor.motor_asyncio.AsyncIOMotorClient(cnxn_string)
# database = client.UnitsList
# collection = database.Units
# document = await collection.find_one({"unit": "Field Ordnance Battery"})
# print(document)
