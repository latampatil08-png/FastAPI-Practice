
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Student data model
class Student(BaseModel):
    name: str
    age: int
    email: str


# Home endpoint
@app.get("/")
def home():
    return {"message": "Student Management API is running"}


# GET - Retrieve all students
@app.get("/students")
def get_students():
    return {
        "students": ["Lata", "Priya", "Anu"]
    }


# POST - Add a student
@app.post("/students")
def add_student(student: Student):
    return {
        "message": "Student added successfully",
        "student": {
            "name": student.name,
            "age": student.age,
            "email": student.email
        }
    }
