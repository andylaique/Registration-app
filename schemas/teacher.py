from pydantic import BaseModel

class Teacher(BaseModel):
    name: str
    email: str
    department: str
    employee_number: int