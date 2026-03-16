from  fastapi import FastAPI
from .database import engine, Base
from .routers import students

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(students.router)

@app.get("/")
def read():
    return{"message":"Welcome to Student Management System"}

