from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to Exam Guidance System"}

@app.get("/exams")
def get_exams():
    return {
        "exams": ["SSC CGL", "UPSC", "RRB NTPC"]
    }
@app.get("/students")
def get_students():
    return {
        "students": ["Lata", "Priya", "Anu"]
    }