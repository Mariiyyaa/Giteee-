from src.database.db import create_tables, insert_sample_data
from src.repository.repository import Repository
import os

DB_FILE = "users.db"

def main():
    if not os.path.exists(DB_FILE):
        create_tables(DB_FILE)
        insert_sample_data(DB_FILE)

    repo = Repository(DB_FILE)

    while True:
        print("\nВыберите действие:")
        print("1. Поиск студента")
        print("2. Поиск свободной комнаты")
        print("3. Внесение информации о состоянии комнат")
        print("4. Просмотр вместимости комнаты")
        print("5. Добавить студента")
        print("6. Обновить данные студента")
        print("0. Выход из системы")
        choice = input("Выбранное действие: ")

        if choice == "1": #Поиск студента
            seach = repo.search_students()
            if students:
                print("\nРезультаты поиска: ")
                for student in students:
                    print(f" ID:{student[0]}, ФИО:{student[1]}, Группа:{student[2]}")
            else:
                print("Студент не найден.")

        elif choice == "2": #Поиск свободной комнаты
            free_rooms = repo.get_free_rooms()
            if free_rooms:
                print("\nСвободные комнаты: ")
            else:
                print("Свободная комната не найдена.")

        elif choice == "3": #Внесение информации о состоянии комнат
            rooms = repo.get_rooms()
            if rooms:
                print("\nСписок комнат: ")
                for room in rooms:
                    if room[1] == 0:
                        status = "Свободна"
                    else:
                        status = "Занята"
                    print("Комната {room[0]}: {room[1]} мест, {status}")
            else:
                print("Информация не внесена.")


        elif choice == "4": #Просмотр вместимости комнат
            sizeroom = repo.get_sizeroom()
            print("\nВывод вместимости всех комнат:")
            for room in sizeroom:
                if room[1] == 0:
                    status = "Свободна"
                if room[1] == 1 or room[1] == 2:
                    status = "Частично занята"
                if room[1] == 3:
                    status = "Занята"
                print("Комната {room[0]}: {status}")


        elif choice == "5": #Добавить студента
            name = input("ФИО студента: ")
            group = input("Группа: ")
            room = input("Номер комнаты: ")
            repo.add_student(name, group, room)
            print("Студент добавлен.")


        elif choice == "6": # Обновить данные студента
            id_student = input("ID студента: ")
            if id_student.isdigit():
                name = input("Обновленное ФИО: ")
                group = input("Обновленный номер группы: ")
                room = input("Обновленный номер комнаты: ")
                status = input ("Обновленный статус студента: ")
                repo.update_student(id_student, name, group, room, status)
                print("Обновление данных произошло успешно.")
            else:
                print("Неверный ID студента. Напишите правильный ID студента.")


        elif choice == "0": #Выход из системы
            print("Выход из программы...")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()

