from pydantic import BaseModel


class machine(BaseModel):
    id: int
    gen: int
    ram: int
    rom: int
    brand: str
