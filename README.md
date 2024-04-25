# Coursera

> Learn FastAPI by Building a Student Management API

## Introduction

This repository is a hands-on introduction to building APIs with FastAPI. Through a practical example, you'll gain experience with core FastAPI concepts like:

- **Creating Routes**: Define endpoints for creating new student records and retrieving existing ones.
- **Data Modeling**: Structure student data using FastAPI's data models.
- **Handling Requests**: Implement logic to handle HTTP requests for creating and retrieving student information.

This project guides you through building a simple student server application using FastAPI.
It's a perfect starting point for anyone who wants to learn the ropes of FastAPI development.

## How to Run

```bash
docker compose up

uvicorn main:app --workers=5
```

curl 127.0.0.1:8000/students

curl -d '{"id":"9631036", "first_name":"elahe", "last_name":"dastan", "registration_date":"1396-07-01", "average":"18.1"}' -H "Content-Type: application/json" -X POST 127.0.0.1:8000/students
