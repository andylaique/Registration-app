from fastapi import FastAPI
from pydantic import BaseModel
import database

app = FastAPI()



database.create_table()



class Student(BaseModel):
    name: str
    age: int
    email: str
    country: str
    id_number: int

class Teacher(BaseModel):
    name: str
    email: str
    department: str
    employee_number: int

class Course(BaseModel):
    title: str
    code: str
    credits: int
    description: str

@app.get("/")
def home():
    return {"message": "Welcome to the school registration system"}

@app.post("/students")
def create_student(student: Student):
    database.add_student(student.name, student.age, student.email, student.country, student.id_number)
    return {"message": "Student registered successfully"}

@app.get("/students")
def read_students():
    rows = database.get_students()
    return [dict(row) for row in rows]

@app.put("/students/{student_id}")
def edit_student(student_id: int, student: Student):
    database.update_student(student_id, student.name, student.age, student.email, student.country, student.id_number)
    return {"message": "Student updated successfully"}

@app.delete("/students/{student_id}")
def remove_student(student_id: int):
    database.delete_student(student_id)
    return {"message": "Student deleted successfully"}



@app.post("/teachers")
def create_teacher(teacher: Teacher):
    database.add_teacher(teacher.name, teacher.email, teacher.department, teacher.employee_number)
    return {"message": "Teacher registered successfully"}

@app.get("/teachers")
def read_teachers():
    rows = database.get_teachers()
    return [dict(row) for row in rows]

@app.put("/teachers/{teacher_id}")
def edit_teacher(teacher_id: int, teacher: Teacher):
    database.update_teacher(teacher_id, teacher.name, teacher.email, teacher.department, teacher.employee_number)
    return {"message": "Teacher updated successfully"}

@app.delete("/teachers/{teacher_id}")
def remove_teacher(teacher_id: int):
    database.delete_teacher(teacher_id)
    return {"message": "Teacher deleted successfully"}





@app.post("/courses")
def create_course(course: Course):
    database.add_course(course.title, course.code, course.credits, course.description)
    return {"message": "Course created successfully"}

@app.get("/courses")
def read_courses():
    rows = database.get_courses()
    return [dict(row) for row in rows]

@app.put("/courses/{course_id}")
def edit_course(course_id: int, course: Course):
    database.update_course(course_id, course.title, course.code, course.credits, course.description)
    return {"message": "Course updated successfully"}

@app.delete("/courses/{course_id}")
def remove_course(course_id: int):
    database.delete_course(course_id)
    return {"message": "Course deleted successfully"}
