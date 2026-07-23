from pydantic import BaseModel,EmailStr,ConfigDict
from datetime import date 
class StudentCreate(BaseModel):
    roll_no: int
    first_name:str
    last_name: str
    email: EmailStr
    phone: str
    branch: str
    semester: int
    division: str
    cgpa:float 
    dob: date

class StudentResponse(BaseModel):
    id:int
    roll_no: int
    first_name:str
    last_name: str
    email: EmailStr
    phone: str
    branch: str
    semester: int
    division: str
    cgpa:float 
    dob: date
    model_config = ConfigDict(from_attributes=True)
