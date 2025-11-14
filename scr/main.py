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

    cursor.execute("SELECT COUNT(*) FROM Books")
    if cursor.fetchone()[0] == 0:
        books = [
            ("Война и мир", 1),
            ("Анна Каренина", 1),
            ("Идиот", 2),
            ("Преступление и наказание", 2),
            ("Братья Карамазовы", 2),
            ("Вишневый сад", 3),
            ("Чайка", 3),
            ("Отцы и дети", 4)
        ]
        cursor.executemany("INSERT INTO Books (Title, Author_ID) VALUES (?, ?)", books)
        print("Добавлены книги.")

    conn.commit()
    conn.close()



