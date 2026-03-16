from  fastapi import FastAPI
from .database import engine, Base
from .routers import students

app = FastAPI()
app.include_router(students.router)
