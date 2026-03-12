from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from ..database import get_db
from .. import schemas, crud

router = APIRouter(prefix="/courses", tags=["Courses"])

# Create Course
@router.post("/", response_model=schemas.CourseResponse, status_code=201)
def create_course(course: schemas.CourseCreate, db: Session = Depends(get_db)):
    db_course = crud.get_course_by_name(db, name=course.name)
    if db_course:
        raise HTTPException(status_code=409, detail="Course already exists")
    return crud.create_course(db=db, course=course)


# Get All Courses (with Pagination)
@router.get("/", response_model=list[schemas.CourseResponse])
def read_courses(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    courses = crud.get_courses(db, skip=skip, limit=limit)
    return courses


# Get Course By ID
@router.get("/{course_id}", response_model=schemas.CourseResponse)
def read_course(course_id: int, db: Session = Depends(get_db)):
    db_course = crud.get_course(db, course_id=course_id)
    if db_course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return db_course


# List Students in a Course
@router.get("/{course_id}/students", response_model=list[schemas.StudentResponse])
def get_course_students(course_id: int, db: Session = Depends(get_db)):
    db_course = crud.get_course(db, course_id=course_id)
    if not db_course:
        raise HTTPException(status_code=404, detail="Course not found")
    
    # Extract students from enrollments
    students = [enrollment.student for enrollment in db_course.enrollments]
    return students


# Update Course
@router.put("/{course_id}", response_model=schemas.CourseResponse)
def update_course(course_id: limint, course: schemas.CourseUpdate, db: Session = Depends(get_db)):
    db_course = crud.get_course(db, course_id=course_id)
    if db_course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return crud.update_course(db=db, course_id=course_id, course=course)


# Delete Course
@router.delete("/{course_id}")
def delete_course(course_id: int, db: Session = Depends(get_db)):
    db_course = crud.get_course(db, course_id=course_id)
    if db_course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    crud.delete_course(db, course_id=course_id)
    return {"message": "Course deleted successfully"}