import sqlite3
from src.models.models import Room, Student, Student_room, Starosta

class Repository:
    def __init__(self, db_file: str = "users.db"):
        self.conn = sqlite3.connect(db_file)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()

# Student
    def get_students(self):
        self.cursor.execute("SELECT ID, Name, Numbergroop FROM Student")
        rows = self.cursor.fetchall()
        return [Student(id = row["ID"], name = row["Name"], number_group = row["Numbergroop"]) for row in rows]

    def search_students(self, search: str):
        self.cursor.execute("SELECT ID, Name, Numbergroop FROM Student WHERE Name LIKE ?", (f'%{search}%',))
        rows = self.cursor.fetchall()
        return [Student(id = row["ID"], name = row["Name"], number_group = row["Numbergroop"]) for row in rows]

    def get_student(self, student_id: int):
        self.cursor.execute("SELECT ID, Name, Numbergroop FROM Student WHERE ID = ?", (student_id,))
        row = self.cursor.fetchone()
        if row:
            return Student(id = row["ID"], name = row["Name"], number_group = row["Numbergroop"])
        return None

    def add_student(self, name: str, number_group: str):
        self.cursor.execute("INSERT INTO Student (Name, Numbergroop) VALUES (?, ?)", (name, number_group))
        self.conn.commit()
        return self.cursor.lastrowid

    def update_student(self, student_id: int, name: str, number_group: str):
        self.cursor.execute("UPDATE Student SET Name = ?, Numbergroop = ? WHERE ID = ?", (name, number_group, student_id))
        self.conn.commit()
        return self.cursor.rowcount > 0

# Room
    def get_rooms(self):
        self.cursor.execute("SELECT ID, Name, Size, Status, id_obsh FROM Room")
        rows = self.cursor.fetchall()
        return [Room(id=row["ID"], name=row["Name"], size=row["Size"], status=row["Status"], id_obsh=row["id_obsh"]) for row in rows]

    def get_room(self, room_id: int):
        self.cursor.execute("SELECT ID, Name, Size, Status, id_obsh FROM Room WHERE ID = ?", (room_id,))
        row = self.cursor.fetchone()
        if row:
            return Room(id=row["ID"], name=row["Name"], size=row["Size"], status=row["Status"], id_obsh=row["id_obsh"])
        return None

    def get_free_rooms(self):
        self.cursor.execute("SELECT ID, Name, Size, Status, id_obsh FROM Room WHERE Status = 'Свободна'")
        rows = self.cursor.fetchall()
        return [Room(id=row["ID"], name=row["Name"], size=row["Size"], status=row["Status"], id_obsh=row["id_obsh"]) for row in rows]

    def update_room_status(self, room_id: int, status: str):
        self.cursor.execute("UPDATE Room SET Status = ? WHERE ID = ?", (status, room_id))
        self.conn.commit()
        return self.cursor.rowcount > 0

    def add_room(self, name: str, size: int, status: str, id_obsh: int):
        self.cursor.execute("INSERT INTO Room (Name, Size, Status, id_obsh) VALUES (?, ?, ?, ?)", (name, size, status, id_obsh))
        self.conn.commit()
        return self.cursor.lastrowid

# Student_room
    def assign_student_to_room(self, student_id: int, room_id: int):
        self.cursor.execute("INSERT INTO Student_room (id_students, id_room) VALUES (?, ?)", (student_id, room_id))
        self.conn.commit()
        return self.cursor.lastrowid

    def get_students_in_room(self, room_id: int):
        query = """
            SELECT s.ID, s.Name, s.Numbergroop 
            FROM Student s 
            JOIN Student_room sr ON s.ID = sr.id_students 
            WHERE sr.id_room = ?
        """
        self.cursor.execute(query, (room_id,))
        rows = self.cursor.fetchall()
        return [Student(id=row["ID"], name=row["Name"], number_group=row["Numbergroop"]) for row in rows]

    def get_rooms_with_student_count(self):
        query = """
            SELECT r.ID, r.Name, r.Size, r.Status, r.id_obsh, COUNT(sr.id_students) as student_count
            FROM Room r
            LEFT JOIN Student_room sr ON r.ID = sr.id_room
            GROUP BY r.ID
        """
        self.cursor.execute(query)
        return self.cursor.fetchall()

 # House_student
    def get_all_house_students(self):
        self.cursor.execute("SELECT ID, Name, Numberoom FROM House_student")
        rows = self.cursor.fetchall()
        return [House_student(id=row["ID"], name=row["Name"], number_room=row["Numberoom"]) for row in rows]

    def get_house_student(self, house_id: int):
        self.cursor.execute("SELECT ID, Name, Numberoom FROM House_student WHERE ID = ?", (house_id,))
        row = self.cursor.fetchone()
        if row:
            return House_student(id=row["ID"], name=row["Name"], number_room=row["Numberoom"])
        return None

    def add_house_student(self, name: str, number_room: str):
        self.cursor.execute("INSERT INTO House_student (Name, Numberoom) VALUES (?, ?)", (name, number_room))
        self.conn.commit()
        return self.cursor.lastrowid
