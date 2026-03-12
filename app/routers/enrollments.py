from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models, schemas
from datetime import datetime

router = APIRouter(prefix="/enrollments", tags=["Enrollments"])

@router.post("/", response_model=schemas.EnrollmentResponse)
def enroll_student(enrollment: schemas.EnrollmentCreate, db: Session = Depends(get_db)):
    # 1. Check if student exists
    student = db.query(models.Student).filter(models.Student.id == enrollment.student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    
    # 2. Check if course exists
    course = db.query(models.Course).filter(models.Course.id == enrollment.course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    
    # 3. Check for duplicate enrollment
    existing_enrollment = db.query(models.Enrollment).filter(
        models.Enrollment.student_id == enrollment.student_id,
        models.Enrollment.course_id == enrollment.course_id
    ).first()
    
    if existing_enrollment:
        raise HTTPException(status_code=400, detail="Student is already enrolled in this course")
    
    # 4. Create enrollment
    new_enrollment = models.Enrollment(
        student_id=enrollment.student_id,
        course_id=enrollment.course_id,
        enrolled_at=datetime.utcnow()
    )
    
    db.add(new_enrollment)
    db.commit()
    db.refresh(new_enrollment)
    
    return new_enrollment
