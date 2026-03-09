from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import SessionLocal
from .. import models, schemas

router = APIRouter(prefix="/courses", tags=["Courses"])

# Database dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Create Course
@router.post("/", response_model=schemas.CourseResponse)
def create_course(course: schemas.CourseCreate, db: Session = Depends(get_db)):
    
    if not course.name:
        raise HTTPException(status_code=400, detail="Course name cannot be empty")

    new_course = models.Course(
        name=course.name,
        description=course.description
    )

    db.add(new_course)
    db.commit()
    db.refresh(new_course)

    return new_course


# Get All Courses (Pagination)
@router.get("/", response_model=list[schemas.CourseResponse])
def get_courses(page: int = 1, limit: int = 10, db: Session = Depends(get_db)):

    skip = (page - 1) * limit

    courses = db.query(models.Course).offset(skip).limit(limit).all()

    return courses


# Get Course by ID
@router.get("/{course_id}", response_model=schemas.CourseResponse)
def get_course(course_id: int, db: Session = Depends(get_db)):

    course = db.query(models.Course).filter(models.Course.id == course_id).first()

    if not course:
        raise HTTPException(status_code=404, detail="Course not found")

    return course


# Update Course
@router.put("/{course_id}", response_model=schemas.CourseResponse)
def update_course(course_id: int, course: schemas.CourseCreate, db: Session = Depends(get_db)):

    existing_course = db.query(models.Course).filter(models.Course.id == course_id).first()

    if not existing_course:
        raise HTTPException(status_code=404, detail="Course not found")

    existing_course.name = course.name
    existing_course.description = course.description

    db.commit()
    db.refresh(existing_course)

    return existing_course


# Delete Course
@router.delete("/{course_id}")
def delete_course(course_id: int, db: Session = Depends(get_db)):

    course = db.query(models.Course).filter(models.Course.id == course_id).first()

    if not course:
        raise HTTPException(status_code=404, detail="Course not found")

    db.delete(course)
    db.commit()

    return {"message": "Course deleted successfully"}