from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models, schemas

router = APIRouter(prefix="/students", tags=["Students"])

# Create Student
@router.post("/")
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):

    existing = db.query(models.Student).filter(models.Student.email == student.email).first()

    if existing:
        raise HTTPException(status_code=400, detail="Email already exists")

    new_student = models.Student(**student.dict())

    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return new_student


# Get All Students
@router.get("/")
def get_students(db: Session = Depends(get_db)):
    students = db.query(models.Student).all()
    return students


# Get Student By ID
@router.get("/{student_id}")
def get_student(student_id: int, db: Session = Depends(get_db)):

    student = db.query(models.Student).filter(models.Student.id == student_id).first()

    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    return student


# Update Student
@router.put("/{student_id}")
def update_student(student_id: int, student: schemas.StudentUpdate, db: Session = Depends(get_db)):

    db_student = db.query(models.Student).filter(models.Student.id == student_id).first()

    if not db_student:
        raise HTTPException(status_code=404, detail="Student not found")

    db_student.name = student.name
    db_student.email = student.email
    db_student.age = student.age

    db.commit()
    db.refresh(db_student)

    return db_student


# Delete Student
@router.delete("/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):

    student = db.query(models.Student).filter(models.Student.id == student_id).first()

    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    db.delete(student)
    db.commit()

    return {"message": "Student deleted successfully"}