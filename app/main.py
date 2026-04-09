from  fastapi import FastAPI
from .database import engine, Base
from .routers import students

Base.metadata.create_all(bind=engine)

app = FastAPI()

# --- SIMPLE API TRACER ---
@app.middleware("http")
async def simple_trace_api(request, call_next):
    # 1. Print what API is being called (BEFORE PROCESSING)
    print(f"👉 NEW REQUEST: {request.method} {request.url.path}")
    
    # 2. Let the API do its normal work
    response = await call_next(request)
    
    # 3. Print the result (AFTER PROCESSING)
    print(f"✅ FINISHED: Sent response code {response.status_code}\n")
    
    return response
# -------------------------

app.include_router(students.router)

@app.get("/")
def read():
    return{"message":"Welcome to Student Management System"}

