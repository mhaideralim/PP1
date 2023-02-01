from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional,List

app = FastAPI()

students = {
    1: {
        "name": "Ali",
        "degree": "IT",
        "cgpa": 3.0,
        "time": 4
    },
    2: {
        "name": "Ahmed",
        "degree": "cs",
        "cgpa": 3.35,
        "time": 5
    },
    3: {
        "name": "umer",
        "degree": "se",
        "cgpa": 2.9,
        "time": 4
    }

}


class Students(BaseModel):
    name: str
    degree: str
    cgpa: float
    time: int

class UpdateStudents(BaseModel):
    name: Optional[str] = None
    degree: Optional[str] = None
    cgpa: Optional[float] = None
    time: Optional[int] = None



@app.get("/get-value/{student_id}")
def get_values(student_id: int, name: str):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
        else:
            return {"Data not found"}


@app.post("/create-user/{student_id}")
def set_values(student_id: int, student: Students):
    if student_id in students:
        return {"ERROR! ID already exists"}
    else:
        students[student_id] = student
        return students[student_id]

@app.put("update-user/{student_id}")
def update_values(student_id, student:UpdateStudents):
    if student_id not in students:
        return {"ERROR! ID already exists"}
    else:
        students[student_id] = student
        return students[student_id]


@app.delete("/delete-user/{student_id}")
def delete_values(student_id:int):
    if student_id not in students:
        return {"Student does not exist"}
    else:
        del students[student_id]
        return{"Data deleted successfully"}

