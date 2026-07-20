from fastapi import FastAPI
from models.models import Student 

app = FastAPI(
    title="CampusCore API",
    description="ERP Backend built with FastAPI",
    version="0.1.0"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to CampusCore 🚀"
    }

students = [
    {
        "id": 1,
        "name": "Varad",
        "branch": "ENTC"
    },
    {
        "id": 2,
        "name": "Sam",
        "branch": "IT"
    }
]

@app.get("/students")
def get_students():
    return [
        {
        "id":1,
        "name" : "varad",
        "branch": "entc"

    },
    {
        "id":2,
        "name": "sam",
        "branch": "it"
    }
    ]

@app.get("/students/{id}")
def get_student(id: int):
    for student in students:
        if student["id"]==id:
            return student 
        
    return {
        "error" : "user not found"
    }

@app.post("/students")
def create_student(student :Student):
    for existing_student in students:
        if existing_student["id"]==student.id:
            return {"error":"id already exists"}
        
    students.append(student.model_dump())

    return {
        "message": "Student Added ",
        "student": student
    }

