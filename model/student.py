from pydantic import BaseModel
from datetime import date

from sqlmodel import Field, SQLModel


class Student(SQLModel, table=True):
    id: str = Field(default=None, primary_key=True)  # Unique identification manually generated
    first_name: str  # First name provided by the user
    last_name: str  # Last name provided by the user
    registration_date: date  # Date of registration
    graduation_date: date | None = None  # Graduation date (if applicable)
    average: float  # Average score provided by the user

