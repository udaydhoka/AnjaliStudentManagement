from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from .. import schemas,models,database
from ..database import get_db

router = APIRouter(prefix="/students",tags=["students"])


#create student 

@router.post("/")
def create_student(student: schemas.studentcreate, db: Session = Depends(get_db)):

    existing = db.query(models.Student).filter(models.Student.email == student.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already exists")

    new_student = models.Student(**student.dict())

    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return new_student



# get all students

@router.get("/")
def get_all_students(db:Session=Depends(get_db)):
    return db.query(models.Student).all()


# get student by id
@router.get("/{student_id}")
def get_student_by_id(student_id:int,db:Session=Depends(get_db)):
    student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404,detail="student not found")
    return student


# update student 
@router.put("/{student_id}")
def update_student(student_id:int,student:schemas.studentcreate,db:Session=Depends(get_db)):
    db_student = db.query(models.Student).filter(models.Student.id==student_id).first()
    if not db_student:
        raise HTTPException(status_code=404, detail="student not found")
    for key, value in student.dict().items():
        setattr(db_student,key,value)
    db.commit()
    db.refresh(db_student)
    return db_student

# delete student

@router.delete("/{student_id}")
def delete_student(student_id:int,db:Session=Depends(get_db)):
    student = db.query(models.Student).filter(models.Student.id==student_id).first()
    if not student:
        raise HTTPException(status_code=404,detail="student not found")
    db.delete(student)
    db.commit()
    return {"message":"student deleted successfully"}
