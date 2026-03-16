
from pydantic import BaseModel, EmailStr,Field
from datetime import datatime 

class studentcreate(BaseModel):
    name: str 
    Email: EmailStr
    age:int=Field(...,ge=16,le=60)

class studentresponse(BaseModel):
    id: int
    name:str
    Email:str
    age:int
    created_at:datatime

    class config:
        orm_mode = True
