from fastapi import FastApi

app = FastApi()

@app.get("/")
def hello():
    return {'message':"hello world"}