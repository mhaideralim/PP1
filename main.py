from datetime import datetime
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {'message':"hello world"}

@app.get("/date")
def time():
    return {'datetime':datetime.now()}