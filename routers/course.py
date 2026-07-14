from fastapi import APIRouter
from schemas.course import Course
from repositories.course import(
    add_course,
    get_courses,
    update_course,
    delete_course

)
router = APIRouter(prefix= "/courses", tags=["courses"])


@router.post("")
def create_course(course: Course):
    add_course(course.title, course.code, course.credits, course.description)
    return {"message": "Course created successfully"}

@router.get("")
def read_courses():
    rows = get_courses()
    return [dict(row) for row in rows]

@router.put("/{course_id}")
def edit_course(course_id: int, course: Course):
    update_course(course_id, course.title, course.code, course.credits, course.description)
    return {"message": "Course updated successfully"}

@router.delete("/{course_id}")
def remove_course(course_id: int):
    delete_course(course_id)
    return {"message": "Course deleted successfully"}