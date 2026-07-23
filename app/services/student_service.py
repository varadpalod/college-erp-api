from sqlalchemy.orm import Session
from fastapi import HTTPException 
from schemas.student import StudentCreate
from models.student import Student

def get_students(db:Session):
    students = db.query(Student).all()
    return students

def get_student(id:int, db:Session):
    student = db.query(Student).filter(Student.id==id).first() 
    if(student is None):
        raise HTTPException(status_code=404,detail="Student not found")
    return student

def create_student(db:Session ,student:StudentCreate):
    existing_student= db.query(Student).filter(Student.roll_no==student.roll_no).first()
    if(existing_student is not None):
        raise HTTPException(status_code=400,detail="Roll No already Exists")
    
    db_student = Student(**student.model_dump())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    
    return db_student

def update_student(id :int,student:StudentCreate,db: Session):
    existing_student=db.query(Student).filter(Student.id==id).first()
    if(existing_student is None):
        raise HTTPException(status_code=404,detail="ID not found")

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

def delete_student(id:int, db:Session):
    existing_student=db.query(Student).filter(Student.id==id).first()
    
    if(existing_student is None):
        raise HTTPException(status_code=404,detail="ID not found")
    
    db.delete(existing_student)
    db.commit()
    return "deletion suucesfull"
    
