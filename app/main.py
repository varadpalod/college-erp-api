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

@app.get("/students")
def get_students(db: Session = Depends(get_db)):
    students = db.query(Student).all()
    return students

@app.get("/students/{id}")
def get_student(id:int,db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id==id).first() 
    if(student is None):
            return "ID already exists"
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
    
@app.put("/students/{id}")
def update_student(id :int,student:StudentPydantic,db: Session=Depends(get_db)):
    existing_student=db.query(Student).filter(Student.id==id).first()
    if(existing_student is None):
        return "ID does not exists"

    existing_student.roll_no = student.roll_no
    existing_student.first_name = student.first_name
    existing_student.last_name = student.last_name
    existing_student.email = student.email
    existing_student.phone = student.phone
    existing_student.branch = student.branch
    existing_student.semester = student.semester
    existing_student.division = student.division
    existing_student.cgpa = student.cgpa
    existing_student.dob = student.dob
    db.commit()
    db.refresh(existing_student)
    return existing_student


@app.delete("/students/{id}")
def remove_student(id:int, db:Session=Depends(get_db)):
    existing_student=db.query(Student).filter(Student.id==id).first()

    if(existing_student is None):
        return "ID does not exist"

    db.delete(existing_student)
    db.commit()
    return "deletion suucesfull"

    