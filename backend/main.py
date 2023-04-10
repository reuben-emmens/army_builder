# pylint: disable=relative-beyond-top-level
'''This file contains the FastAPI app and routes'''

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from .database import (create_unit, fetch_all_units, fetch_one_unit,
                       delete_unit, update_unit)
from .model import Unit

# App object
app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials = True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    '''This function returns a simple message to test the connection'''
    return {"Welcome": "to the Astra Militarum API"}

@app.get("/api/unit")
async def get_unit():
    '''This function returns all units in the database'''
    response = await fetch_all_units()
    return response

@app.get("/api/unit/{unit}", response_model=Unit)
async def get_unit_by_name(unit:str):
    '''This function returns a single unit from the database'''
    response = await fetch_one_unit(unit)
    if response:
        return response
    raise HTTPException(404, f"There is no unit with the name: {unit}")

@app.post("/api/unit/", response_model=Unit)
async def post_unit(unit:Unit):
    '''This function creates a new unit in the database'''
    response = await create_unit(unit.dict())
    if response:
        return response
    raise HTTPException(400, "Bad Request")

@app.put("/api/unit/{unit}", response_model=Unit)
async def put_unit(unit:str, data:int):
    '''This function updates a unit in the database'''
    response = await update_unit(unit, data)
    if response:
        return response
    raise HTTPException(404, f"There is no unit with the name: {unit}")

@app.delete("/api/unit/{unit}")
async def delete_unit(unit:str):
    '''This function deletes a unit from the database'''''
    response = await remove_unit(unit)
    if response:
        return "Successfully deleted unit"
    raise HTTPException(404, f"There is no unit with the name: {unit}")
