from database import get_db_connection;

def add_student(name, age, email, country, id_number):
    with get_db_connection() as connection:
        connection.execute('INSERT INTO students (name, age, email, country, id_number) VALsUES (?, ?, ?, ?, ?)',
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