from sqlalchemy import Column, Integer, String, Date, DECIMAL,Enum,ForeignKey,UniqueConstraint
from database.database import Base
from sqlalchemy.orm import relationship

class Attendance(Base):
    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True, autoincrement=True)
    student_id=Column(Integer,ForeignKey("students.id"),nullable=False)
    date = Column(Date, nullable=False)
    status=Column(Enum("Present","Absent","Late"),nullable=False)

    student=relationship("Student",back_populates="attendances")
    __table_args__ = (UniqueConstraint("student_id", "date"),)