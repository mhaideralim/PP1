from fastapi import FastAPI, HTTPException, Body
from fastapi.encoders import jsonable_encoder
from pymongo import MongoClient
from pydantic import BaseModel
from typing import Optional, List
from pymongo.errors import PyMongoError
from starlette import status
from starlette.responses import JSONResponse
import asyncio

app = FastAPI()

client = MongoClient("mongodb://localhost:27017/")
try:
    client.admin.command('ismaster')
    print("Connected to the database successfully.")

except Exception as e:
    print(f"Could not connect to the database: {e}")

db = client["ali1"]
hali = db["ali"]























class Person(BaseModel):
    id: int
    name: str
    email: str
    height: float
    weight: int

class UpdatePerson(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    email: Optional[str] = None
    height: Optional[float] = None
    weight: Optional[int] = None



@app.get("/get-data/{data_id}")
async def get_data(id: int):
    data = hali.find_one({"id": id})

    if not data:
        raise HTTPException(status_code=404, detail="Data not found")

    return data












@app.post("/update-data")
async def set_data(persons: Person):
    if id in hali:
        raise HTTPException(status_code=309, detail="Data already exists")
    else:
        hali.insert_one(persons.dict())
    return {"message": "Data inserted successfully"}




@app.put("/update-data")
async def update_data(id: int, Person: dict):
    query = {"id": id}
    new_values = {"$set": Person}

    result = hali.update_one(query, new_values)

    if result.modified_count == 0:
        raise HTTPException(status_code=400, detail="Data not found")

    return {"message": "Data updated successfully"}



@app.delete("/delete-data/{id}")
async def delete_data(id: int):
    result = hali.delete_one({"id": id})

    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Data not found")

    return {"message": "Data deleted successfully"}


















