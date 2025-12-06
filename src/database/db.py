# src/database/db.py
import sqlite3

def create_tables(db: str = "users.db"):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()

    # Удаляем старую таблицу Starosta если существует
    cursor.execute("DROP TABLE IF EXISTS Starosta")

    # Создаем таблицы
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Room (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name_room VARCHAR(50),
            Size VARCHAR(50),
            Status VARCHAR(50),
            Number_ob VARCHAR(50)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Student_room (
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

    # Создаем таблицу Starosta с ПРОСТЫМИ названиями колонок
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Starosta (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name VARCHAR(50),
            Zadacha VARCHAR(50)
        )
    ''')

    conn.commit()
    conn.close()


def insert_sample_data(db: str = "users.db"):
    """Добавить тестовые данные"""
    conn = sqlite3.connect(db)
    cursor = conn.cursor()

    # Студенты
    cursor.execute("SELECT COUNT(*) FROM Student")
    if cursor.fetchone()[0] == 0:
        students = [
            ("Мария Забродина", "25-ИВТ-2-1"),
            ("Дарья Демидова", "25-ИСТ-2")
        ]
        cursor.executemany("INSERT INTO Student (Name, Numbergroop) VALUES (?, ?)", students)

    # Комнаты
    cursor.execute("SELECT COUNT(*) FROM Room")
    if cursor.fetchone()[0] == 0:
        rooms = [
            ("175", "1-2 человека", "Частично занята", "1"),
            ("176", "0 человек", "Свободна", "1"),
            ("177", "3 человека", "Занята", "1")
        ]
        cursor.executemany("INSERT INTO Room (Name_room, Size, Status, Number_ob) VALUES (?, ?, ?, ?)", rooms)

    # Заселение
    cursor.execute("SELECT COUNT(*) FROM Student_room")
    if cursor.fetchone()[0] == 0:
        student_rooms = [
            ("Мария Забродина", "175"),
            ("Дарья Демидова", "176")
        ]
        cursor.executemany("INSERT INTO Student_room (Name, Numberoom) VALUES (?, ?)", student_rooms)

    # Старосты - используем Name и Zadacha
    cursor.execute("SELECT COUNT(*) FROM Starosta")
    if cursor.fetchone()[0] == 0:
        starosta = [
            ("Дима Дмитриев", "обновление данных о проживающих студентах"),
            ("Иван Иванов", "внесение информации о состоянии комнат")
        ]
        cursor.executemany("INSERT INTO Starosta (Name, Zadacha) VALUES (?, ?)", starosta)

    conn.commit()
    conn.close()