import sqlite3
from contextlib import contextmanager

sqlite_file_name = "school.db"

@contextmanager
def get_db_connection():
    connection = sqlite3.connect(sqlite_file_name)
    connection.row_factory = sqlite3.Row
    try:
        yield connection
    finally:
        connection.close()

def create_table():
    with get_db_connection() as connection:
        connection.execute('''CREATE TABLE IF NOT EXISTS students (
                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                           name TEXT NOT NULL,
                           age INTEGER NOT NULL,
                           email TEXT NOT NULL,
                           country TEXT NOT NULL,
                           id_number INTEGER NOT NULL)''')

        connection.execute('''CREATE TABLE IF NOT EXISTS teachers (
                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                           name TEXT NOT NULL,
                           email TEXT NOT NULL,
                           department TEXT NOT NULL,
                           employee_number INTEGER NOT NULL)''')

        connection.execute('''CREATE TABLE IF NOT EXISTS courses (
                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                           title TEXT NOT NULL,
                           code TEXT NOT NULL,
                           credits INTEGER NOT NULL,
                           description TEXT NOT NULL)''')
        connection.commit()

def add_student(name, age, email, country, id_number):
    with get_db_connection() as connection:
        connection.execute('INSERT INTO students (name, age, email, country, id_number) VALUES (?, ?, ?, ?, ?)',
                           (name, age, email, country, id_number))
        connection.commit()

def get_students():
    with get_db_connection() as connection:
        rows = connection.execute('SELECT * FROM students').fetchall()
        return rows

def update_student(student_id, name, age, email, country, id_number):
    with get_db_connection() as connection:
        connection.execute('UPDATE students SET name=?, age=?, email=?, country=?, id_number=? WHERE id=?',
                           (name, age, email, country, id_number, student_id))
        connection.commit()

def delete_student(student_id):
    with get_db_connection() as connection:
        connection.execute('DELETE FROM students WHERE id=?', (student_id,))
        connection.commit()

def add_teacher(name, email, department, employee_number):
    with get_db_connection() as connection:
        connection.execute('INSERT INTO teachers (name, email, department, employee_number) VALUES (?, ?, ?, ?)',
                           (name, email, department, employee_number))
        connection.commit()

def get_teachers():
    with get_db_connection() as connection:
        rows = connection.execute('SELECT * FROM teachers').fetchall()
        return rows

def update_teacher(teacher_id, name, email, department, employee_number):
    with get_db_connection() as connection:
        connection.execute('UPDATE teachers SET name=?, email=?, department=?, employee_number=? WHERE id=?',
                           (name, email, department, employee_number, teacher_id))
        connection.commit()

def delete_teacher(teacher_id):
    with get_db_connection() as connection:
        connection.execute('DELETE FROM teachers WHERE id=?', (teacher_id,))
        connection.commit()

def add_course(title, code, credits, description):
    with get_db_connection() as connection:
        connection.execute('INSERT INTO courses (title, code, credits, description) VALUES (?, ?, ?, ?)',
                           (title, code, credits, description))
        connection.commit()

def get_courses():
    with get_db_connection() as connection:
        rows = connection.execute('SELECT * FROM courses').fetchall()
        return rows

def update_course(course_id, title, code, credits, description):
    with get_db_connection() as connection:
        connection.execute('UPDATE courses SET title=?, code=?, credits=?, description=? WHERE id=?',
                           (title, code, credits, description, course_id))
        connection.commit()

def delete_course(course_id):
    with get_db_connection() as connection:
        connection.execute('DELETE FROM courses WHERE id=?', (course_id,))
        connection.commit()
