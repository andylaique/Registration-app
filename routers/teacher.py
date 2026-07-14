from fastapi import APIRouter
from schemas.teacher import Teacher
from repositories.teacher import(
    add_teacher,
    get_teachers,
    update_teacher,
    delete_teacher

)
router = APIRouter(prefix= "/teachers", tags=["teachers"])

@router.post("")
def create_teacher(teacher: Teacher):
    add_teacher(teacher.name, teacher.email, teacher.department, teacher.employee_number)
    return {"message": "Teacher registered successfully"}

@router.get("")
def read_teachers():
    rows = get_teachers()
    return [dict(row) for row in rows]

@router.put("/{teacher_id}")
def edit_teacher(teacher_id: int, teacher: Teacher):
    update_teacher(teacher_id, teacher.name, teacher.email, teacher.department, teacher.employee_number)
    return {"message": "Teacher updated successfully"}

@router.delete("/{teacher_id}")
def remove_teacher(teacher_id: int):
    delete_teacher(teacher_id)
    return {"message": "Teacher deleted successfully"}