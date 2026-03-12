from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from ..database import get_db
from .. import schemas, crud

router = APIRouter(prefix="/students", tags=["Students"])

# Create Student
@router.post("/", response_model=schemas.StudentResponse, status_code=201)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    db_student = crud.get_student_by_email(db, email=student.email)
    if db_student:
        raise HTTPException(status_code=409, detail="Email already registered")
    return crud.create_student(db=db, student=student)


# Get All Students (with Search and Pagination)
@router.get("/", response_model=list[schemas.StudentResponse])
def read_students(
    name: str = Query(None, description="Search students by name"),
    skip: int = 0, 
    limit: int = 10, 
    db: Session = Depends(get_db)
):
    students = crud.get_students(db, skip=skip, limit=limit, name=name)
    return students


# Get Student By ID
@router.get("/{student_id}", response_model=schemas.StudentResponse)
def read_student(student_id: int, db: Session = Depends(get_db)):
    db_student = crud.get_student(db, student_id=student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student


# Fetch Student Courses
@router.get("/{student_id}/courses", response_model=list[schemas.CourseResponse])
def get_student_courses(student_id: int, db: Session = Depends(get_db)):
    db_student = crud.get_student(db, student_id=student_id)
    if not db_student:
        raise HTTPException(status_code=404, detail="Student not found")
    
    # Get all enrollments for the student and extract courses
    courses = [enrollment.course for enrollment in db_student.enrollments]
    return courses


# Update Student
@router.put("/{student_id}", response_model=schemas.StudentResponse)
def update_student(student_id: int, student: schemas.StudentUpdate, db: Session = Depends(get_db)):
    db_student = crud.get_student(db, student_id=student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    
    # Check if new email conflicts with another student
    if student.email != db_student.email:
        email_check = crud.get_student_by_email(db, email=student.email)
        if email_check:
            raise HTTPException(status_code=409, detail="Email already exists")

    return crud.update_student(db=db, student_id=student_id, student=student)


# Delete Student
@router.delete("/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    db_student = crud.get_student(db, student_id=student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    crud.delete_student(db, student_id=student_id)
    return {"message": "Student deleted successfully"}