# src/inter.py
import os
from src.database.db import create_tables, insert_sample_data
from src.repository.repository import Repository


def main():
    DB_FILE = "users.db"

    if not os.path.exists(DB_FILE):
        print("Создание базы данных...")
        create_tables(DB_FILE)
        insert_sample_data(DB_FILE)
        print(f"База '{DB_FILE}' создана")

    repo = Repository(DB_FILE)

    while True:
        print("\n" + "=" * 50)
        print("Учет заселенных студентов и старост")
        print("=" * 50)
        print("Выберите действие:")
        print("1. Поиск студента")
        print("2. Поиск старосты")
        print("3. Добавить студента")
        print("4. Добавить старосту")
        print("5. Обновить данные студента")
        print("6. Обновить данные старосты")
        print("7. Показать всех студентов")
        print("8. Показать всех старост")
        print("0. Выход из системы")
        print("-" * 50)

        choice = input("Выбранное действие: ")

        if choice == "1":  # Поиск студента
            name = input("Введите ФИО студента для поиска: ").strip()
            students = repo.search_students(name)
            if students:
                print("\nРезультаты поиска: ")
                for student in students:
                    room_info = repo.get_student_room(student[0])
                    if room_info:
                        room_number = room_info[2]
                    else:
                        room_number = "Не заселен"
                    print(f" ID:{student[0]}, ФИО:{student[1]}, Группа:{student[2]}, Комната:{room_number}")
            else:
                print("Студент не найден.")

        elif choice == "2":  # Поиск старосты
            name = input("Введите ФИО старосты для поиска: ").strip()
            starosti = repo.search_starosta(name)
            if starosti:
                print("\nРезультаты поиска старост: ")
                for starosta in starosti:
                    print(f" ID:{starosta[0]}, ФИО:{starosta[1]}, Задача:{starosta[2]}")
            else:
                print("Староста не найден.")

        elif choice == "3":  # Добавить студента
            name = input("ФИО студента: ")
            group = input("Группа: ")
            room = input("Номер комнаты: ")
            if repo.add_student(name, group, room):
                print("Студент добавлен.")
            else:
                print("Ошибка при добавлении студента.")

        elif choice == "4":  # Добавить старосту
            name = input("ФИО старосты: ")
            zadacha = input("Задача старосты: ")
            if repo.add_starosta(name, zadacha):
                print("Староста добавлен.")
            else:
                print("Ошибка при добавлении старосты.")

        elif choice == "5":  # Обновить данные студента
            id_student = input("ID студента: ")
            if id_student.isdigit():
                name = input("Обновленное ФИО: ")
                group = input("Обновленный номер группы: ")
                room = input("Обновленный номер комнаты: ")
                status = input("Обновленный статус студента: ")
                if repo.update_student(int(id_student), name, group, room, status):
                    print("Обновление данных произошло успешно.")
                else:
                    print("Ошибка при обновлении данных.")
            else:
                print("Неверный ID студента. Напишите правильный ID студента.")

        elif choice == "6":  # Обновить данные старосты
            id_starosta = input("ID старосты: ")
            if id_starosta.isdigit():
                name = input("Обновленное ФИО: ")
                zadacha = input("Обновленная задача: ")
                if repo.update_starosta(int(id_starosta), name, zadacha):
                    print("Данные старосты обновлены.")
                else:
                    print("Ошибка при обновлении данных старосты.")
            else:
                print("Неверный ID старосты.")

        elif choice == "7":  # Показать всех студентов
            students = repo.get_all_students()
            if students:
                print("\nВсе студенты:")
                print("-" * 60)
                print(f"{'ID':<5} {'ФИО':<25} {'Группа':<15} {'Комната':<10}")
                print("-" * 60)
                for student in students:
                    room_info = repo.get_student_room(student[0])
                    if room_info:
                        room_number = room_info[2]
                    else:
                        room_number = "Не заселен"
                    print(f"{student[0]:<5} {student[1]:<25} {student[2]:<15} {room_number:<10}")
            else:
                print("Студенты не найдены.")

        elif choice == "8":  # Показать всех старост
            starosti = repo.get_all_starosta()
            if starosti:
                print("\nВсе старосты:")
                print("-" * 70)
                print(f"{'ID':<5} {'ФИО':<25} {'Задача':<40}")
                print("-" * 70)
                for starosta in starosti:
                    print(f"{starosta[0]:<5} {starosta[1]:<25} {starosta[2]:<40}")
            else:
                print("Старосты не найдены.")

        elif choice == "0":  # Выход из системы
            print("Выход из программы...")
            repo.close()
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()