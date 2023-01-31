from fastapi import FastAPI

app = FastAPI()

db = [
    {"id": 1, "gen": 5, "ram": 8, "rom": 250, "brand": "dell"},
    {"id": 2, "gen": 4, "ram": 4, "rom": 128, "brand": "hp"},
    {"id": 3, "gen": 5, "ram": 16, "rom": 500, "brand": "dell"},
    {"id": 4, "gen": 7, "ram": 32, "rom": 1000, "brand": "dell"},
    {"id": 5, "gen": 8, "ram": 32, "rom": 500, "brand": "hp"},
    {"id": 6, "gen": 6, "ram": 16, "rom": 250, "brand": "hp"}

]
@app.get("/laptop")
def data(brand: str|None= None, ram: int|None= None) -> list:
    result = db
    if brand:
        result = [data for data in result if data['brand'] == brand ]
    if ram:
        result = [data for data in result if data['ram'] <= ram ]
    else:
        return result