import random
import time

from db.student import StudentTable
from sqlmodel import Session, SQLModel, create_engine, select

from model.student import Student


class PostgresDB(StudentTable):
    engine = create_engine("postgresql+psycopg2://postgres:1378@localhost", echo=True)

    # time.sleep(random.randint(0, 10))

    SQLModel.metadata.create_all(engine)

    def read_table(self):
        with Session(self.engine) as session:
            statement = select(Student)
            students = session.exec(statement)
            return list(students)

    def read_row(self, id):
        with Session(self.engine) as session:
            student = session.get(Student, id)
            session.commit()
            return student

    def add_row(self, student):
        with Session(self.engine) as session:
            session.add(student)
            session.commit()

    def delete_row(self, id):
        with Session(self.engine) as session:
            student = session.get(Student, id)
            session.delete(student)
            session.commit()
