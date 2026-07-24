from pydantic import BaseModel,EmailStr,ConfigDict
from datetime import date 
from enum import Enum
class UserRole(str,Enum):
    STUDENT ="Student"
    ADMIN ="Admin"
    FACULTY ="Faculty"
class UserCreate(BaseModel):
    username:str
    password:str
    role:UserRole

class UserResponse(BaseModel):
    id:int 
    username:str
    role:UserRole
    is_active:bool
    model_config=ConfigDict(from_attributes=True)