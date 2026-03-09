from pydantic import BaseModel, EmailStr, Field
from datetime import datetime


 #  student schema # 

class StudentCreate(BaseModel):
    name: str
    email: EmailStr
    age: int = Field(..., ge=16, le=60)

class StudentUpdate(BaseModel):
    name: str
    email: EmailStr
    age: int = Field(..., ge=16, le=60)

class StudentResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    age: int
    created_at: datetime

    class Config:
        from_attributes = True
    
    # course schema #

class CourseBase(BaseModel):
    name: str
    description: str

class CourseCreate(CourseBase):
    pass

class CourseResponse(CourseBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True