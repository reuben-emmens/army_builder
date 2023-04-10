# pylint: disable=relative-beyond-top-level line-too-long
'''This file contains the FastAPI app and routes'''
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from .database import (create_unit, delete_unit, fetch_all_units,
                       fetch_one_unit, update_unit)
from .model import Unit, UpdatedUnit

# App object
app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials = True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# CREATE
@app.post("/api/unit/")
async def post_unit(unit_obj:Unit):
    '''This function creates a new unit in the database'''
    try:
        create_result = await create_unit(unit_obj.dict())
    except ValueError as exc:
        raise HTTPException(400, f'{unit_obj.unit} already exists in the database') from exc
    except Exception as exc:
        raise HTTPException(500, 'Something has gone wrong when inserting the record.') from exc
    return create_result

# READ
@app.get("/")
def read_root():
    '''This function returns a simple message to test the connection'''
    return {"Welcome": "to the Astra Militarum API"}

@app.get("/api/unit")
async def get_unit():
    '''This function returns all units in the database'''
    try:
        fetch_result = await fetch_all_units()
    except Exception as exc:
        raise HTTPException(500, 'Something has gone wrong when fetching all units') from exc
    return fetch_result

@app.get("/api/unit/{unit}", response_model=Unit)
async def get_unit_by_name(unit:str):
    '''This function returns a single unit from the database'''
    try:
        fetch_result = await fetch_one_unit(unit)
    except Exception as exc:
        raise HTTPException(404, f'Something has gone wrong. Most likely, {unit} has not been found in the database.') from exc
    return fetch_result

# UPDATE
@app.put("/api/unit/{unit}")
async def put_unit(unit:str, unit_obj:UpdatedUnit):
    '''This function updates a unit in the database'''
    try:
        update_result = await update_unit(unit, unit_obj.dict())
    except Exception as exc:
        raise HTTPException(404, f'Something has gone wrong. Most likely, {unit} has not been found in the database.') from exc
    return update_result

# DELETE
@app.delete("/api/unit/{unit}")
async def delete_unit_request(unit: str):
    '''This function deletes a unit from the database'''''
    try:
        delete_result = await delete_unit(unit)
    except Exception as exc:
        raise HTTPException(404, f'Something has gone wrong. Most likely, {unit} has not been found in the database.') from exc
    return delete_result
