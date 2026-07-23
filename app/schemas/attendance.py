from pydantic import BaseModel,ConfigDict
from datetime import date 
from enum import Enum
class AttendanceStatus(str,Enum):
    PRESENT ="Present"
    ABSENT ="Absent"
    LATE ="Late"
class AttendanceCreate(BaseModel):
    student_id:int
    date: date
    status:AttendanceStatus

class AttendanceResponse(BaseModel):
    id:int
    student_id: int
    date:date
    status: AttendanceStatus

    model_config=ConfigDict(from_attributes=True)
