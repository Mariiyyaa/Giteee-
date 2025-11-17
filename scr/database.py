import sqlite3
from sqlite3 import Connection

def get_connection(db: str = "users.db") -> Connection:
    return sqlite3.connect(db)

def create_tables(db: str = "users.db"):
    conn = get_connection(db)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Room (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name VARCHAR(50),
            Size VARCHAR(50),
            Status VARCHAR(50),
            id_obsh VARCHAR(50)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Student_room (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            id_students VARCHAR(50),
            id_room VARCHAR(50)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS House_student (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name VARCHAR(50),
            Numberoom VARCHAR(50)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Student (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name VARCHAR(50),
            Numbergroop VARCHAR(50)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Student_doc (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name VARCHAR(50),
            Number VARCHAR(50)
        )
    ''')
    conn.commit()
    conn.close()


def insert_sample_data(db: str = "users.db"):
    conn = get_connection(db)
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM Student")
    if cursor.fetchone()[0] == 0:
        students = [
            ("Мария Забродина", "25-ИВТ-2-1"),
            ("Дарья Демидова", "25-ИСТ-2")
        ]
        cursor.executemany("INSERT INTO Student (Name, Numbergroop) VALUES (?, ?)", students)
        print("Добавлены студенты.")

    cursor.execute("SELECT COUNT(*) FROM Room")
    if cursor.fetchone()[0] == 0:
        rooms = [
            ("175", "1-2 человека", "Частично занята", "1"),
            ("176", "0 человек", "Свободна", "1"),
            ("177", "3 человека", "Занята", "1")
        ]
        cursor.executemany("INSERT INTO Room (Name, Size, Status, id_obsh) VALUES (?, ?, ?, ?)", rooms)
        print("Комната добавлена.")


    cursor.execute("SELECT COUNT(*) FROM Student_room")
    if cursor.fetchone()[0] == 0:
        student_rooms = [
            ("1", "175"),
            ("2", "176")
        ]
        cursor.executemany("INSERT INTO Student_room (id_students, id_room) VALUES (?, ?)", student_rooms)
        print("Студент заселен.")


    cursor.execute("SELECT COUNT(*) FROM House_student")
    if cursor.fetchone()[0] == 0:
        house_students = [
            ("Мария Забродина", "175"),
            ("Дарья Демидова", "176")
        ]
        cursor.executemany("INSERT INTO House_student (Name, Numberoom) VALUES (?, ?)", house_students)
        print("Студент заселён.")


    cursor.execute("SELECT COUNT(*) FROM Student_doc")
    if cursor.fetchone()[0] == 0:
        student_docs = [
            ("Мария Забродина", "1"),
            ("Дарья Демидова", "2")
        ]
        cursor.executemany("INSERT INTO Student_doc (Name, Number) VALUES (?, ?)", student_docs)
        print("Добавлены номера студентов.")

    conn.commit()
    conn.close()

