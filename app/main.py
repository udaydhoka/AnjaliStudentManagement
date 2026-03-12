from fastapi import FastAPI
from .database import engine, Base
from .routers import students, courses,enrollments
from . import models

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Student Management System")

app.include_router(students.router)
app.include_router(courses.router)
app.include_router(enrollments.router)

@app.get("/")
def home():
    return {"message": "FastAPI Student Management API"}