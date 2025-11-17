import sqlite3

from src.models.models import Room, Student_room, House_student, Student,Student_doc

class Repository:
    def __init__(self, db_file: str = "users.db"):
        self.conn = sqlite3.connect(db_file)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()

    #Student
    def get_students(self):
        self.cursor.execute("SELECT * FROM Student")
        return self.cursor.fetchall()

    def search_students(self, search: str):
        self.cursor.execute("SELECT * FROM Student WHERE Name LIKE ?")
        return self.cursor.fetchall()

    def add_student(self, name: str, number_group: str):
        self.cursor.execute("INSERT INTO Student (Name, Numbergroop) VALUES (?, ?)",(name, number_group))
        self.conn.commit()
        return self.cursor.lastrowid

    def update_student(self, student_id: int, name: str, number_group: str):
        self.cursor.execute("UPDATE Student SET Name = ?, Numbergroop = ? WHERE ID = ?",(name, number_group, student_id))
        self.conn.commit()
        return self.cursor.rowcount > 0

    #Room
    def get_all_rooms(self):
        self.cursor.execute("SELECT * FROM Room")
        return self.cursor.fetchall()

    def get_free_rooms(self):
        self.cursor.execute("SELECT * FROM Room WHERE Status = 'Свободна'")
        return self.cursor.fetchall()

    def get_rooms(self):
        self.cursor.execute("SELECT * FROM Room")
        return self.cursor.fetchall()

    def get_sizeroom(self):
        self.cursor.execute("SELECT * FROM Room")
        return self.cursor.fetchall()

    def update_room_status(self, room_id: int, status: str):
        self.cursor.execute("UPDATE Room SET Status = ? WHERE ID = ?",(status, room_id))
        self.conn.commit()
        return self.cursor.rowcount > 0

    def add_room(self, name: str, size: str, status: str, id_obsh: str):
        self.cursor.execute("INSERT INTO Room (Name, Size, Status, id_obsh) VALUES (?, ?, ?, ?)",(name, size, status, id_obsh))
        self.conn.commit()
        return self.cursor.lastrowid

    #Student_room
    def assign_student_to_room(self, student_id: str, room_id: str):
        self.cursor.execute("INSERT INTO Student_room (id_students, id_room) VALUES (?, ?)",(student_id, room_id))
        self.conn.commit()
        return self.cursor.lastrowid

    def get_students_in_room(self, room_id: str):
        self.cursor.execute("SELECT s.* FROM Student s ","JOIN Student_room sr ON s.ID = sr.id_students ", "WHERE sr.id_room = ?", (room_id,))
        return self.cursor.fetchall()

    #House_student
    def get_all_house_students(self):
        self.cursor.execute("SELECT * FROM House_student")
        return self.cursor.fetchall()

    def add_house_student(self, name: str, number_room: str):
        self.cursor.execute("INSERT INTO House_student (Name, Numberoom) VALUES (?, ?)",(name, number_room))
        self.conn.commit()
        return self.cursor.lastrowid

    #Student_doc
    def get_all_student_docs(self):
        self.cursor.execute("SELECT * FROM Student_doc")
        return self.cursor.fetchall()

    def add_student_doc(self, name: str, number: str):
        self.cursor.execute("INSERT INTO Student_doc (Name, Number) VALUES (?, ?)",(name, number))
        self.conn.commit()
        return self.cursor.lastrowid

    def close(self):
        self.conn.close()
