# FastAPI Project Assignment

## Student Management System API

**Duration:** 4 Days\
**Tech Stack:** Python, FastAPI, SQLite, SQLAlchemy/SQLModel

Build a REST API to manage **students, courses, and enrollments**.

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
