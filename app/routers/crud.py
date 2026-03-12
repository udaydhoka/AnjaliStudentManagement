from sqlalchemy.orm import Session
from . import models, schemas

# Student CRUD
def get_student(db: Session, student_id: int):
    return db.query(models.Student).filter(models.Student.id == student_id).first()

def get_student_by_email(db: Session, email: str):
    return db.query(models.Student).filter(models.Student.email == email).first()

def get_students(db: Session, skip: int = 0, limit: int = 10, name: str = None):
    query = db.query(models.Student)
    if name:
        # Search students by name (case-insensitive search if possible, using contains for now)
        query = query.filter(models.Student.name.contains(name))
    return query.offset(skip).limit(limit).all()

def create_student(db: Session, student: schemas.StudentCreate):
    db_student = models.Student(
        name=student.name,
        email=student.email,
        age=student.age
    )
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def update_student(db: Session, student_id: int, student: schemas.StudentUpdate):
    db_student = get_student(db, student_id)
    if db_student:
        db_student.name = student.name
        db_student.email = student.email
        db_student.age = student.age
        db.commit()
        db.refresh(db_student)
    return db_student

def delete_student(db: Session, student_id: int):
    db_student = get_student(db, student_id)
    if db_student:
        db.delete(db_student)
        db.commit()
    return db_student

# Course CRUD
def get_course(db: Session, course_id: int):
    return db.query(models.Course).filter(models.Course.id == course_id).first()

def get_course_by_name(db: Session, name: str):
    return db.query(models.Course).filter(models.Course.name == name).first()

def get_courses(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Course).offset(skip).limit(limit).all()

def create_course(db: Session, course: schemas.CourseCreate):
    db_course = models.Course(
        name=course.name,
        description=course.description
    )
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course

def update_course(db: Session, course_id: int, course: schemas.CourseUpdate):
    db_course = get_course(db, course_id)
    if db_course:
        db_course.name = course.name
        db_course.description = course.description
        db.commit()
        db.refresh(db_course)
    return db_course

def delete_course(db: Session, course_id: int):
    db_course = get_course(db, course_id)
    if db_course:
        db.delete(db_course)
        db.commit()
    return db_course

# Enrollment CRUD
def get_enrollment(db: Session, enrollment_id: int):
    return db.query(models.Enrollment).filter(models.Enrollment.id == enrollment_id).first()

def get_enrollment_by_student_and_course(db: Session, student_id: int, course_id: int):
    return db.query(models.Enrollment).filter(
        models.Enrollment.student_id == student_id,
        models.Enrollment.course_id == course_id
    ).first()

def get_enrollments(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Enrollment).offset(skip).limit(limit).all()

def create_enrollment(db: Session, enrollment: schemas.EnrollmentCreate):
    db_enrollment = models.Enrollment(
        student_id=enrollment.student_id,
        course_id=enrollment.course_id
    )
    db.add(db_enrollment)
    db.commit()
    db.refresh(db_enrollment)
    return db_enrollment

def delete_enrollment(db: Session, enrollment_id: int):
    db_enrollment = get_enrollment(db, enrollment_id)
    if db_enrollment:
        db.delete(db_enrollment)
        db.commit()
    return db_enrollment
