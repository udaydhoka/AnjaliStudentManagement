# FastAPI Project Assignment

## Student Management System API

**Duration:** 4 Days\
**Tech Stack:** Python, FastAPI, SQLite, SQLAlchemy/SQLModel

Build a REST API to manage **students, courses, and enrollments**.

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

