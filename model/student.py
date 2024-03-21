from pydantic import BaseModel
from datetime import date


class Student(BaseModel):
    id: str  # Unique identification manually generated
    first_name: str  # First name provided by the user
    last_name: str  # Last name provided by the user
    registration_date: date  # Date of registration
    graduation_date: date | None = None  # Graduation date (if applicable)
    average: float  # Average score provided by the user
