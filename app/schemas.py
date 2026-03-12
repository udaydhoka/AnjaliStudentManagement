from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import List, Optional


 #  student schema # 

class StudentCreate(BaseModel):
    name: str
    email: EmailStr
    age: int = Field(..., ge=16, le=60)

class StudentUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    age: Optional[int] = Field(None, ge=16, le=60)

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

# Enrollment schemas
class EnrollmentCreate(BaseModel):
    student_id: int
    course_id: int

class EnrollmentResponse(BaseModel):
    id: int
    student_id: int
    course_id: int
    enrolled_at: datetime

    class Config:
        from_attributes = True

# Schemas for nested relationships if needed
class StudentWithCourses(StudentResponse):
    courses: List[CourseResponse] = []

class CourseWithStudents(CourseResponse):
    students: List[StudentResponse] = []