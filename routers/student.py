from fastapi import APIRouter
from schemas.student import Student
from repositories.student import(
    add_student,
    get_students,
    update_student,
    delete_student
)
router = APIRouter(prefix= "/students", tags=["students"])

@router.post("")
def create_student(student: Student):
    add_student(student.name, student.age, student.email, student.country, student.id_number)
    return {"message": "Student registered successfully"}

@router.get("")
def read_students():
    rows = get_students()
    return [dict(row) for row in rows]

@router.put("/{student_id}")
def edit_student(student_id: int, student: Student):
    update_student(student_id, student.name, student.age, student.email, student.country, student.id_number)
    return {"message": "Student updated successfully"}

@router.delete("/{student_id}")
def remove_student(student_id: int):
    delete_student(student_id)
    return {"message": "Student deleted successfully"}