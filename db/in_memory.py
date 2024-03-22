from fastapi import FastAPI, HTTPException
from db.student import StudentTable


class InMemoryDB(StudentTable):
    students = {}

    def read_table(self):
        return self.students

    def read_row(self, id):
        if id not in self.students:
            return HTTPException(status_code=404, detail="Student with given id does not exist")
        return self.students.get(id)

    def add_row(self, student):
        if id in self.students:
            return HTTPException(status_code=409, detail="Student with given id already exists")
        self.students[student.id] = student

    def delete_row(self, id):
        del self.students[id]
