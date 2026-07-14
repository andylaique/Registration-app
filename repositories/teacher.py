from database import get_db_connection;

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
