from fastapi import FastAPI, HTTPException, Depends
import time
import asyncio

from db.in_memory import InMemoryDB
from db.postgres import PostgresDB
from db.student import StudentTable
from model.student import Student
from sqlmodel import Session, SQLModel, create_engine
import psycopg2

# students = {}
# db = InMemoryDB()

app = FastAPI()

# engine = create_engine("postgresql+psycopg2://postgres:1378@localhost")
#
# SQLModel.metadata.create_all(engine)

DB = PostgresDB


@app.get("/students")
async def get_students(db: StudentTable = Depends(DB)):
    """Retrieve a list of created students"""
    return db.read_table()


# Fetch the details of a student identified by the given ID
@app.get("/students/{id}")
async def get_student(id: int, db: StudentTable = Depends(DB)):
    return db.read_row(id)


# Create a student
@app.post("/students")
async def create_student(student: Student, db: StudentTable = Depends(DB)):
    # with Session(engine) as session:
    #     session.add(student)
    #     session.commit()

    # time.sleep(10)

    # await asyncio.sleep(10)

    db.add_row(student)


# Remove a student identified by the given ID
@app.delete("/students/{id}")
async def delete_student(id: int, db: StudentTable = Depends(DB)):
    db.delete_row(id)
