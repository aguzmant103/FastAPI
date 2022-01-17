from fastapi import FastAPI, Path
from typing import Optional

app = FastAPI()

students = {
    1:{
        "name":"Johns",
        "age": 17,
        "class": "Year 12"
    },
    2:{
        "name":"Peter",
        "age": 16,
        "class": "Year 13"
    }
}

@app.get("/")
def index():
    return {"name" : "First Data"}

@app.get("/students")
def get_students():
    return students

@app.get("/students/{student_id}")
def get_student(student_id : int = Path(None, description="The ID of the student you want to view", gt=0, lt=3)):
    return students[student_id]

@app.get("/get-by-name")
def get_student(*, name : Optional[str] = None, test : int):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data" : "Not found"}

@app.post("/")
def create():
    return {"Succeed"}

@app.post("/trick/")
def create():
    return {"Trick"}