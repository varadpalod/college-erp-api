from sqlalchemy import Column, Integer, String, Boolean, Enum
from database.database import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)

    username=Column(String(50),unique=True,nullable=False)
    hashed_password = Column(String(255), nullable=False)
    role = Column(Enum("Admin", "Faculty", "Student"), nullable=False)
    is_active = Column(Boolean, default=True,nullable=False)