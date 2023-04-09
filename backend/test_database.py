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
    cnxn_string = os.getenv("CNXN_STRING")
    client = motor.motor_asyncio.AsyncIOMotorClient(cnxn_string)
    database = client.UnitsList
    collection_marker = database.Units
    return collection_marker

@pytest.fixture
def sample_data_fixture():
    '''This function loads the sample data from the sample_data.json file'''
    sample_data_file = 'backend/static/sample_data.json'
    with open(sample_data_file, 'r', encoding='utf-8') as file:
        return json.load(file)

async def test_collection(collection_fixture):
    '''Tests if a connection can be made to the collection in the database'''''
    collection = await collection_fixture
    assert collection.name == 'Units'

async def test_create_unit(collection_fixture, sample_data_fixture):
    '''Tests if the create_unit function is working correctly'''
    collection = await collection_fixture
    document = sample_data_fixture
    result = await collection.find_one({"unit": document["unit"]})
    if result is None:
        await collection.insert_one(document)
        record = await collection.find_one({"unit": document["unit"]})
        assert record['unit'] == document['unit']
    else:
        pytest.fail("Unit already exists")

async def test_fetch_one_unit(collection_fixture, sample_data_fixture):
    '''Tests if the fetch_one_unit function is working correctly'''
    collection = await collection_fixture
    document = sample_data_fixture
    record = await collection.find_one({"unit": document['unit']})
    assert record['unit'] == document['unit']

async def test_fetch_all_units(collection_fixture):
    '''Tests if the fetch_all_units function is working correctly'''
    collection = await collection_fixture
    units = []
    cursor = collection.find({})
    async for document in cursor:
        units.append(document)
    assert len(units) > 0

async def test_update_unit(collection_fixture, sample_data_fixture):
    '''Tests if the update_unit function is working correctly'''
    collection = await collection_fixture
    document = sample_data_fixture
    await collection.update_one({"unit": document['unit']}, {"$set": {"power": "0"}})
    record = await collection.find_one({"unit": document['unit']})
    assert record['power'] == '0'

async def test_delete_unit(collection_fixture, sample_data_fixture):
    '''Tests if the delete_unit function is working correctly'''
    collection = await collection_fixture
    document = sample_data_fixture
    await collection.delete_one({"unit": document['unit']})
    record = await collection.find_one({"unit": document['unit']})
    assert record is None
