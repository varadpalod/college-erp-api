from pydantic import BaseModel,EmailStr
from datetime import date 
class StudentPydantic(BaseModel):
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