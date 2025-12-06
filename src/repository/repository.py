import sqlite3
from typing import List, Tuple


class Repository:
    def __init__(self, db_file: str = "users.db"):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def search_students(self, name: str = "") -> List[Tuple]:
        try:
            if name:
                self.cursor.execute("SELECT ID, Name, Numbergroop FROM Student WHERE Name LIKE ?", (f"%{name}%",))
            else:
                self.cursor.execute("SELECT ID, Name, Numbergroop FROM Student")
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Ошибка при поиске студентов: {e}")
            return []

    def get_all_students(self) -> List[Tuple]:
        """Получить всех студентов"""
        try:
            self.cursor.execute("SELECT ID, Name, Numbergroop FROM Student")
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Ошибка при получении студентов: {e}")
            return []

    def add_student(self, name: str, group: str, room: str = None) -> bool:
        """Добавить студента"""
        try:
            self.cursor.execute("INSERT INTO Student (Name, Numbergroop) VALUES (?, ?)", (name, group))
            if room:
                self.cursor.execute("INSERT INTO Student_room (Name, Numberoom) VALUES (?, ?)", (name, room))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Ошибка при добавлении студента: {e}")
            self.conn.rollback()
            return False

    def update_student(self, student_id: int, name: str, group: str, room: str = None, status: str = None) -> bool:
        """Обновить данные студента"""
        try:
            # Получаем старое имя студента
            self.cursor.execute("SELECT Name FROM Student WHERE ID = ?", (student_id,))
            old_name_row = self.cursor.fetchone()
            if not old_name_row:
                return False

            old_name = old_name_row[0]

            # Обновляем студента
            self.cursor.execute("UPDATE Student SET Name = ?, Numbergroop = ? WHERE ID = ?",
                                (name, group, student_id))

            # Обновляем комнату
            if room:
                self.cursor.execute("SELECT * FROM Student_room WHERE Name = ?", (old_name,))
                if self.cursor.fetchone():
                    self.cursor.execute("UPDATE Student_room SET Name = ?, Numberoom = ? WHERE Name = ?",
                                        (name, room, old_name))
                else:
                    self.cursor.execute("INSERT INTO Student_room (Name, Numberoom) VALUES (?, ?)",
                                        (name, room))

            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Ошибка при обновлении студента: {e}")
            self.conn.rollback()
            return False

    def get_student_room(self, student_id: int) -> Tuple:
        """Получить комнату студента"""
        try:
            self.cursor.execute("SELECT Name FROM Student WHERE ID = ?", (student_id,))
            student_row = self.cursor.fetchone()
            if student_row:
                student_name = student_row[0]
                self.cursor.execute("SELECT * FROM Student_room WHERE Name = ?", (student_name,))
                row = self.cursor.fetchone()
                if row:
                    return row
        except:
            pass
        return None

    # ========== МЕТОДЫ ДЛЯ СТАРОСТ ==========

    def search_starosta(self, name: str = "") -> List[Tuple]:
        """Поиск старост по имени"""
        try:
            # Сначала пробуем с Name и Zadacha
            if name:
                self.cursor.execute("SELECT ID, Name, Zadacha FROM Starosta WHERE Name LIKE ?", (f"%{name}%",))
            else:
                self.cursor.execute("SELECT ID, Name, Zadacha FROM Starosta")
            return self.cursor.fetchall()
        except sqlite3.Error:
            # Если не получилось, пробуем другие варианты
            try:
                if name:
                    self.cursor.execute(
                        "SELECT ID, Name_starost, Zadacha_starost FROM Starosta WHERE Name_starost LIKE ?",
                        (f"%{name}%",))
                else:
                    self.cursor.execute("SELECT ID, Name_starost, Zadacha_starost FROM Starosta")
                return self.cursor.fetchall()
            except:
                return []

    def get_all_starosta(self) -> List[Tuple]:
        """Получить всех старост"""
        try:
            # Сначала пробуем с Name и Zadacha
            self.cursor.execute("SELECT ID, Name, Zadacha FROM Starosta")
            return self.cursor.fetchall()
        except sqlite3.Error:
            # Если не получилось, пробуем другие варианты
            try:
                self.cursor.execute("SELECT ID, Name_starost, Zadacha_starost FROM Starosta")
                return self.cursor.fetchall()
            except:
                return []

    def add_starosta(self, name: str, zadacha: str) -> bool:
        """Добавить старосту"""
        try:
            # Пробуем разные варианты названий колонок
            try:
                # Вариант 1: Name, Zadacha
                self.cursor.execute("INSERT INTO Starosta (Name, Zadacha) VALUES (?, ?)", (name, zadacha))
            except sqlite3.Error:
                # Вариант 2: Name_starost, Zadacha_starost
                self.cursor.execute("INSERT INTO Starosta (Name_starost, Zadacha_starost) VALUES (?, ?)",
                                    (name, zadacha))

            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Ошибка при добавлении старосты: {e}")
            self.conn.rollback()
            return False

    def update_starosta(self, starosta_id: int, name: str, zadacha: str) -> bool:
        """Обновить данные старосты"""
        try:
            # Пробуем разные варианты названий колонок
            try:
                self.cursor.execute("UPDATE Starosta SET Name = ?, Zadacha = ? WHERE ID = ?",
                                    (name, zadacha, starosta_id))
            except sqlite3.Error:
                self.cursor.execute("UPDATE Starosta SET Name_starost = ?, Zadacha_starost = ? WHERE ID = ?",
                                    (name, zadacha, starosta_id))

            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Ошибка при обновлении старосты: {e}")
            self.conn.rollback()
            return False

    def close(self):
        """Закрыть соединение"""
        self.conn.close()