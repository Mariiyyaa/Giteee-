import sqlite3
from sqlite3 import Connection

def get_connection(db: str = "users.db") -> Connection:
    return sqlite3.connect(db)

def create_tables(db: str = "users.db"):
    conn = get_connection(db)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE Room (
            ID INTEGER PRIMARY KEY AUTOINCREMENT
            Name VARCHAR(50)
            Size VARCHAR(50)
            Status VARCHAR(50)
            id_obsh VARCHAR(50)
    )
    ''')
    cursor.execute('''
        CREATE TABLE Student_room (
            ID INTEGER PRIMARY KEY AUTOINCREMENT
            id_students VARCHAR(50)
            id_room VARCHAR(50)
    )
    ''')
    cursor.execute('''
        CREATE TABLE House_student (
            ID INTEGER PRIMARY KEY AUTOINCREMENT
            Name VARCHAR(50)
            Numberoom VARCHAR(50)
    )
    ''')
    cursor.execute('''
        CREATE TABLE Student (
            ID INTEGER PRIMARY KEY AUTOINCREMENT
            Name VARCHAR(50)
            Numbergroop VARCHAR(50)
    )
    ''')

    cursor.execute('''
        CREATE TABLE Student_doc (
            ID INTEGER PRIMARY KEY AUTOINCREMENT
            Name VARCHAR(50)
            Number VARCHAR(50)
    )
    ''')
    conn.commit()
    conn.close()

def insert_sample_data(db: str = "users.db"):
    conn = get_connection(db)
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM Students")
    if cursor.fetchone()[0] == 0:
        students = [
            ("Мария Забродина",),
            ("Дарья Демидова")
        ]
        cursor.executemany("INSERT INTO Students(Name) VALUES (?)", students)
        print("Добавлен студент.")
    if cursor.fetchone()[0] == 0:
        Numbergroop = [
            ("25-ИВТ-2-1",),
            ("25-ИСТ-2")
        ]
        cursor.executemany("INSERT INTO Students(Numbergroop) VALUES (?)",Numbergroop)
        print("Добавлен номер группы. ")


    cursor.execute("SELECT COUNT(*) FROM Room")
    if cursor.fetchone()[0] == 0:
        students = [
            ("Мария Забродина",),
            ("Дарья Демидова")
        ]
        cursor.executemany("INSERT INTO Room(Name) VALUES (?)", students)
        print("Добавлен студент.")
    if cursor.fetchone()[0] == 0:
        Size = [
            ("3 человека",),
            ("2 человека")
        ]
        cursor.executemany("INSERT INTO Room(Size) VALUES (?)", Size)
        print("Добавлен размер комнаты проживания.")
    if cursor.fetchone()[0] == 0:
        Status = [
            ("Частично занята",),
            ("Занята",),
            ("Свообдна")
        ]
        cursor.executemany("INSERT INTO Room(Status) VALUES (?)", Status)
        print("Добавлен статус комнаты.")
    if cursor.fetchone()[0] == 0:
        id_obsh = [
            ("1")
        ]
        cursor.executemany("INSERT INTO Room(id_obsh) VALUES (?)", id_obsh)
        print("Добавлен ID общежития.")

    cursor.execute("SELECT COUNT(*) FROM Student_room")
    if cursor.fetchone()[0] == 0:
        id_students = [
            ("1. Мария Забродина",),
            ("2. Дарья Демидова")
        ]
        cursor.executemany("INSERT INTO Student_room(id_students) VALUES (?)", id_students)
        print("Добавлен ID студента.")
    if cursor.fetchone()[0] == 0:
        id_room = [
            ("1. 175",),
            ("2. 176")
        ]
        cursor.executemany("INSERT INTO Student_room(id_room) VALUES (?)", id_room)
        print("Добавлен ID комнаты.")

    cursor.execute("SELECT COUNT(*) FROM House_student")
    if cursor.fetchone()[0] == 0:
        Name = [
            ("Мария Забродина",),
            ("Дарья Демидова")
        ]
        cursor.executemany("INSERT INTO House_student(Name) VALUES (?)", Name)
        print("Добавлен студент.")
    if cursor.fetchone()[0] == 0:
        Numberoom = [
            ("175",),
            ("176")
        ]
        cursor.executemany("INSERT INTO House_student(Numberoom) VALUES (?)", Numberoom)
        print("Добавлен номер комнаты.")

    cursor.execute("SELECT COUNT(*) FROM Student_doc")
    if cursor.fetchone()[0] == 0:
        Name = [
            ("Мария Забродина",),
            ("Дарья Демидова")
        ]
        cursor.executemany("INSERT INTO Student_doc(Name) VALUES (?)", Name)
        print("Добавлен студент.")
    if cursor.fetchone()[0] == 0:
        Number = [
            ("1",),
            ("2")
        ]
        cursor.executemany("INSERT INTO Student_doc(Number) VALUES (?)", Number)
        print("Добавлен номер.")

    conn.commit()
    conn.close()

