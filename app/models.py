from sqlalchemy import Column,Integer,String,DateTime
from DateTime import datetime
from .database import  Base

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String,nullable=False)
    email = Column(String,Unique=True,index=True)
    age = Column(Integer)
    created_at = Column(DateTime,default=datetime.utcnow)

