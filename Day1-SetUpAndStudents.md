# FastAPI Project Assignment

## Student Management System API

**Duration:** 4 Days\
**Tech Stack:** Python, FastAPI, SQLite, SQLAlchemy/SQLModel

Build a REST API to manage **students, courses, and enrollments**.

------------------------------------------------------------------------

# Day 1 -- Project Setup & Student APIs

## Objectives

Set up the FastAPI project and implement **Student CRUD APIs**.

## Tasks

### 1. Setup Project

Create project structure:

    app/
     ├── main.py
     ├── database.py
     ├── models.py
     ├── schemas.py
     ├── routers/
     │    └── students.py

Install required packages:

    fastapi
    uvicorn
    sqlalchemy (or sqlmodel)
    pydantic

Setup: - SQLite database - Database connection - Base model
configuration

------------------------------------------------------------------------

### 2. Create Student Model

Fields:

    id
    name
    email
    age
    created_at

Rules:

-   Email must be **unique**
-   Age must be between **16--60**
-   Name is required

------------------------------------------------------------------------

### 3. Implement Student APIs

Endpoints:

    POST /students
    GET /students
    GET /students/{student_id}
    PUT /students/{student_id}
    DELETE /students/{student_id}

------------------------------------------------------------------------

### Deliverables (End of Day 1)

Working APIs:

-   Create student
-   Get all students
-   Get student by ID
-   Update student
-   Delete student

Test using: - Swagger UI - Postman

------------------------------------------------------------------------
