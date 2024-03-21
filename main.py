from fastapi import FastAPI, HTTPException
import time
import asyncio

from db.student import StudentTable
from model.student import Student

students = {}

app = FastAPI()


# Retrieve a list of created students
@app.get("/students")
async def get_students():
    return students


# Fetch the details of a student identified by the given ID
@app.get("/students/{id}")
async def get_student(id: int):
    if id not in students:
        return HTTPException(status_code=404, detail="Student with given id does not exist")

    return students.get(id)


# Create a student
@app.post("/students")
async def create_student(student: Student):
    # time.sleep(10)

    # await asyncio.sleep(10)

    if id in students:
        return HTTPException(status_code=409, detail="Student with given id already exists")

    students[student.id] = student

    return students


# Remove a student identified by the given ID
@app.delete("/students/{id}")
async def delete_student(id: int):
    del students[id]
