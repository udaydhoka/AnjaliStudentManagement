from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from .. import schemas, crud

router = APIRouter(prefix="/enrollments", tags=["Enrollments"])

# Create Enrollment
@router.post("/", response_model=schemas.EnrollmentResponse, status_code=201)
def create_enrollment(enrollment: schemas.EnrollmentCreate, db: Session = Depends(get_db)):
    # Check if student exists
    db_student = crud.get_student(db, student_id=enrollment.student_id)
    if not db_student:
        raise HTTPException(status_code=404, detail="Student not found")
    
    # Check if course exists
    db_course = crud.get_course(db, course_id=enrollment.course_id)
    if not db_course:
        raise HTTPException(status_code=404, detail="Course not found")

    existing = crud.get_enrollment_by_student_and_course(
        db, student_id=enrollment.student_id, course_id=enrollment.course_id
    )
    if existing:
        raise HTTPException(status_code=409, detail="Student already enrolled in this course")

    return crud.create_enrollment(db=db, enrollment=enrollment)


# Get All Enrollments (with Pagination)
@router.get("/", response_model=list[schemas.EnrollmentResponse])
def read_enrollments(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    enrollments = crud.get_enrollments(db, skip=skip, limit=limit)
    return enrollments


# Get Enrollment by ID
@router.get("/{enrollment_id}", response_model=schemas.EnrollmentResponse)
def read_enrollment(enrollment_id: int, db: Session = Depends(get_db)):
    db_enrollment = crud.get_enrollment(db, enrollment_id=enrollment_id)
    if not db_enrollment:
        raise HTTPException(status_code=404, detail="Enrollment not found")
    return db_enrollment


# Delete Enrollment
@router.delete("/{enrollment_id}")
def delete_enrollment(enrollment_id: int, db: Session = Depends(get_db)):
    db_enrollment = crud.get_enrollment(db, enrollment_id=enrollment_id)
    if not db_enrollment:
        raise HTTPException(status_code=404, detail="Enrollment not found")
    crud.delete_enrollment(db, enrollment_id=enrollment_id)
    return {"message": "Enrollment deleted successfully"}