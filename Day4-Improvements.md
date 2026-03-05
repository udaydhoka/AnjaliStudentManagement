# FastAPI Project Assignment

## Student Management System API

**Duration:** 4 Days\
**Tech Stack:** Python, FastAPI, SQLite, SQLAlchemy/SQLModel

Build a REST API to manage **students, courses, and enrollments**.

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
