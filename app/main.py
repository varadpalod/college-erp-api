from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from models.models import StudentPydantic
from models.student import Student
from database.database import Base, engine, get_db

Base.metadata.create_all(bind=engine)

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
def get_students(db: Session = Depends(get_db)):
    students = db.query(Student).all()
    return students

@app.get("/students/{id}")
def get_student(id:int,db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id==id) 
    return student

@app.post("/students")
def create_student(student :StudentPydantic,db:Session=Depends(get_db)):
    existing_student= db.query(Student).filter(Student.roll_no==student.roll_no).first()
    if(existing_student is not None):
        return "ROll No already exists"

    db_student = Student(**student.model_dump())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)

    return db_student
    
