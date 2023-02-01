import uvicorn
from fastapi import FastAPI, HTTPException

app = FastAPI()

db = [
    {"id": 1, "gen": 5, "ram": 8, "rom": 250, "brand": "dell"},
    {"id": 2, "gen": 4, "ram": 4, "rom": 128, "brand": "hp"},
    {"id": 3, "gen": 5, "ram": 16, "rom": 500, "brand": "dell"},
    {"id": 4, "gen": 7, "ram": 32, "rom": 1000, "brand": "dell"},
    {"id": 5, "gen": 8, "ram": 32, "rom": 500, "brand": "hp"},
    {"id": 6, "gen": 6, "ram": 16, "rom": 250, "brand": "hp"}

]


@app.get("/error-handling/{id}")
def machine_by_id(id: int) -> dict:
    result = [data for data in db if data['id'] == id]
    if result:
        return result[0]
    else:
        raise HTTPException(status_code=404, detail=f"No machine with id={id}.")


if __name__ == "__main__":
    uvicorn.run("errorhandling:app", reload=True)
