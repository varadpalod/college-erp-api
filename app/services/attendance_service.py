from sqlalchemy.orm import Session
from fastapi import HTTPException 
from schemas.attendance import AttendanceCreate
from models.attendance import Attendance
from models.student import Student 

def get_attendances(db:Session):
    attendances=db.query(Attendance).all()
    return attendances 

def get_attendance(id:int, db:Session):
    attendance=db.query(Attendance).filter(id==Attendance.id).first()
    if(attendance is None):
        raise HTTPException(status_code=404,detail="Student Not Found")

    return attendance

def create_attendance(db:Session,attendance:AttendanceCreate):
    student = db.query(Student).filter(Student.id == attendance.student_id).first()

    if student is None:
        raise HTTPException(status_code=404, detail="Attendance not found")

    existing_attendance= db.query(Attendance).filter(Attendance.student_id==attendance.student_id,Attendance.date==attendance.date).first()
    if(existing_attendance is not None):
        raise HTTPException(status_code=409,detail="Attendance Already Marked")
    
    db_attendance = Attendance(**attendance.model_dump())
    db.add(db_attendance)
    db.commit()
    db.refresh(db_attendance)
    
    return db_attendance

def update_attendance(id :int,attendance:AttendanceCreate,db: Session):
    existing_attendance=db.query(Attendance).filter(Attendance.id==id).first()
    if(existing_attendance is None):
        raise HTTPException(status_code=404,detail="ID not found")

    existing_attendance.student_id = attendance.student_id
    existing_attendance.date = attendance.date
    existing_attendance.status = attendance.status

    db.commit()
    db.refresh(existing_attendance)
    return existing_attendance

def delete_attendance(id:int, db:Session):
    existing_attendance=db.query(Attendance).filter(Attendance.id==id).first()
    
    if(existing_attendance is None):
        raise HTTPException(status_code=404,detail="ID not found")
    
    db.delete(existing_attendance)
    db.commit()
    return "deletion suucesfull"