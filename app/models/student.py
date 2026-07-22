from sqlalchemy import Column, Integer, String, Date, DECIMAL
from database.database import Base


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, autoincrement=True)

    roll_no = Column(Integer, unique=True, nullable=False)

    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)

    email = Column(String(100), unique=True, nullable=False)
    phone = Column(String(15), nullable=False)

    branch = Column(String(20), nullable=False)
    semester = Column(Integer, nullable=False)
    division = Column(String(10), nullable=False)

    dob = Column(Date, nullable=False)
    cgpa = Column(DECIMAL(3, 2), nullable=False)