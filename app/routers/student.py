from fastapi import APIRouter
from fastapi import FastAPI, Depends, HTTPException 
from sqlalchemy.orm import Session

from schemas.student import StudentCreate,StudentResponse
from models.student import Student
from database.database import Base, engine, get_db
from services import student_service

router=APIRouter(prefix="/students",tags=["Students"])


@router.get("/")
def get_students(db: Session = Depends(get_db)):
    return student_service.get_students(db)

@router.get("/{id}",response_model=StudentResponse)
def get_student(id:int,db: Session = Depends(get_db)):
    return student_service.get_student(id,db)

@router.post("/",response_model=StudentResponse)
def create_student(student :StudentCreate,db:Session=Depends(get_db)):
    return student_service.create_student(db,student)
    
@router.put("/{id}",response_model=StudentResponse)
def update_student(id :int,student:StudentCreate,db: Session=Depends(get_db)):
    return student_service.update_student(id,student,db)

@router.delete("/{id}")
def remove_student(id:int, db:Session=Depends(get_db)):
    return student_service.delete_student(id,db)