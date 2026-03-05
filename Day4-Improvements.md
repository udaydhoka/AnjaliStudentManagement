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

# Day 2 -- Course APIs

## Objectives

Add **Course management** functionality.

------------------------------------------------------------------------

### 1. Create Course Model

Fields:

    id
    name
    description
    created_at

Rules:

-   Course name must not be empty

------------------------------------------------------------------------

### 2. Implement Course APIs

Endpoints:

    POST /courses
    GET /courses
    GET /courses/{course_id}
    PUT /courses/{course_id}
    DELETE /courses/{course_id}

------------------------------------------------------------------------

### 3. Pagination

Add pagination to:

    GET /students
    GET /courses

Example:

    GET /students?page=1&limit=10

------------------------------------------------------------------------

### Deliverables (End of Day 2)

Working APIs:

-   Create course
-   Get all courses
-   Get course by ID
-   Update course
-   Delete course
-   Pagination for students and courses

------------------------------------------------------------------------

# Day 3 -- Student Course Enrollment

## Objectives

Implement **many-to-many relationship** between students and courses.

------------------------------------------------------------------------

### 1. Create Enrollment Model

Fields:

    id
    student_id
    course_id
    enrolled_at

Relationship:

    Student  ↔  Course
    many-to-many

------------------------------------------------------------------------

### 2. Implement Enrollment API

Endpoint:

    POST /enrollments

Example request:

``` json
{
  "student_id": 1,
  "course_id": 2
}
```

------------------------------------------------------------------------

### 3. Prevent Duplicate Enrollments

A student **cannot enroll in the same course twice**.

Return a proper error message if attempted.

------------------------------------------------------------------------

### 4. Fetch Student Courses

Endpoint:

    GET /students/{student_id}/courses

Return all courses the student is enrolled in.

------------------------------------------------------------------------

### Deliverables (End of Day 3)

Working APIs:

-   Enroll student in course
-   Fetch courses for a student
-   Duplicate enrollment prevention

------------------------------------------------------------------------

# Day 4 -- Improvements & Additional Features

## Objectives

Add search, additional endpoints, and improve project structure.

------------------------------------------------------------------------

### 1. Search Students

    GET /students?name=rahul

Return matching students.

------------------------------------------------------------------------

### 2. List Students in a Course

    GET /courses/{course_id}/students

Return all students enrolled in the course.

------------------------------------------------------------------------

### 3. Error Handling

Handle the following cases:

-   Student not found
-   Course not found
-   Invalid enrollment
-   Duplicate email

Return appropriate HTTP codes:

    404 Not Found
    400 Bad Request
    409 Conflict

------------------------------------------------------------------------

### 4. Refactor Project Structure

Final suggested structure:

    app/
     ├── main.py
     ├── database.py
     ├── models.py
     ├── schemas.py
     ├── crud.py
     ├── routers/
     │    ├── students.py
     │    ├── courses.py
     │    └── enrollments.py

------------------------------------------------------------------------

### 5. Documentation

Ensure **Swagger API documentation** works correctly.

------------------------------------------------------------------------

# Final Deliverables

The API should support:

-   Students CRUD
-   Courses CRUD
-   Enrollment system
-   Student course listing
-   Course student listing
-   Pagination
-   Student search
-   Proper validation and error handling

------------------------------------------------------------------------

# Evaluation Criteria

  Area              What to Check
  ----------------- --------------------------------
  Code structure    Proper modularization
  Database design   Correct relationships
  Validation        Proper Pydantic usage
  Error handling    Correct HTTP status codes
  API design        Clean and consistent endpoints
  Code quality      Readable and organized code
