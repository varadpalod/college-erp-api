from fastapi import APIRouter
from fastapi import FastAPI, Depends, HTTPException 
from sqlalchemy.orm import Session

from schemas.attendance import AttendanceCreate,AttendanceResponse
from models.attendance import Attendance
from database.database import Base, engine, get_db
from services import attendance_service

router=APIRouter(prefix="/attendances",tags=["Attendance"])

@router.get("/")
def get_attedances(db: Session = Depends(get_db)):
    return attendance_service.get_attendances(db)

@router.get("/{id}",response_model=AttendanceResponse)
def get_attendance(id:int,db:Session=Depends(get_db)):
    return attendance_service.get_attendance(id,db)

@router.post("/",response_model=AttendanceResponse)
def create_attendance(attendance :AttendanceCreate,db:Session=Depends(get_db)):
    return attendance_service.create_attendance(db,attendance)
    
@router.put("/{id}",response_model=AttendanceResponse)
def update_attendance(id :int,attendance:AttendanceCreate,db: Session=Depends(get_db)):
    return attendance_service.update_attendance(id,attendance,db)

@router.delete("/{id}")
def remove_attendance(id:int, db:Session=Depends(get_db)):
    return attendance_service.delete_attendance(id,db)
