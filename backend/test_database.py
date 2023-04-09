# pylint: disable=redefined-outer-name
'''Test the database functions are functioning correctly with expected outputs'''
import os
import json #pylint: disable=unused-import
import motor.motor_asyncio
import pytest
from dotenv import load_dotenv

pytestmark = pytest.mark.asyncio

@pytest.fixture
async def collection_fixture():
    '''This function establishes a connection to the MongoDB database via the Motor driver.'''
    load_dotenv()
    cnxn_string = os.getenv('CNXN_STRING')
    client = motor.motor_asyncio.AsyncIOMotorClient(cnxn_string)
    database = client.UnitsList
    collection_marker = database.Units
    return collection_marker

@pytest.fixture
async def document_fixture():
    '''This function establishes a connection to the MongoDB database via the Motor driver.'''
    load_dotenv()
    cnxn_string = os.getenv('CNXN_STRING')
    client = motor.motor_asyncio.AsyncIOMotorClient(cnxn_string)
    database = client.UnitsList
    collection = database.Units
    doc = await collection.find_one({"unit": "Field Ordnance Battery"})
    return doc

async def test_document(document_fixture):
    '''Tests if the document fixture is working correctly'''
    document = await document_fixture
    assert document['unit'] == 'Field Ordnance Battery'

async def test_collection(collection_fixture):
    '''Tests if the collection fixture is working correctly'''
    collection = await collection_fixture
    assert collection.name == 'Units'
