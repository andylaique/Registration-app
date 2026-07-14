from database import get_db_connection;



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
        