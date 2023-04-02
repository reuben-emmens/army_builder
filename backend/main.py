from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from model import Unit
from database import (
    fetch_one_unit,
    fetch_all_units,
    create_unit,
    update_unit,
    remove_unit
)

# App object
app = FastAPI()

origins = ['https://localhost:3000']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials = True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Ping": "Pong"}

@app.get("/api/unit")
async def get_unit():
    response = await fetch_all_units()
    return response

@app.get("/api/unit/{unit}", response_model=Unit)
async def get_unit_by_unit_name(unit:str):
    response = await fetch_one_unit(unit)
    if response:
        return response
    raise HTTPException(404, f"There is no unit with the name: {unit}")

@app.post("/api/unit/", response_model=Unit)
async def post_unit(unit:Unit):
    response = await create_unit(unit.dict())
    if response:
        return response
    raise HTTPException(400, "Bad Request")

@app.put("/api/unit/{unit}", response_model=Unit)
async def put_unit(unit:str, data:int):
    response = await update_unit(unit, data)
    if response:
        return response
    raise HTTPException(404, f"There is no unit with the name: {unit}")

@app.delete("/api/unit/{unit}")
async def delete_unit(unit:str):
    response = await remove_unit(unit)
    if response:
        return "Successfully deleted unit"
    raise HTTPException(404, f"There is no unit with the name: {unit}")