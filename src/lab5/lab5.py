import sqlite3
import json
import csv
import os

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS Student")
cursor.execute("DROP TABLE IF EXISTS Room")
cursor.execute("DROP TABLE IF EXISTS Student_room")

cursor.execute('''
    CREATE TABLE Student (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Name VARCHAR(50),
        Numbergroop VARCHAR(50)
    )
''')

cursor.execute('''
    CREATE TABLE Room (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Name_room VARCHAR(50),
        Size VARCHAR(50),
        Status VARCHAR(50),
        Number_ob VARCHAR(50)
    )
''')

cursor.execute('''
    CREATE TABLE Student_room (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Name VARCHAR(50),
        Numberoom VARCHAR(50)
    )
''')

students = [
    ("Мария Забродина", "25-ИВТ-2-1"),
    ("Дарья Демидова", "25-ИСТ-2")
]
cursor.executemany("INSERT INTO Student (Name, Numbergroop) VALUES (?, ?)", students)

rooms = [
    ("175", "1-2 человека", "Частично занята", "1"),
    ("176", "0 человек", "Свободна", "1"),
    ("177", "3 человека", "Занята", "1")
]
cursor.executemany("INSERT INTO Room (Name_room, Size, Status, Number_ob) VALUES (?, ?, ?, ?)", rooms)

student_rooms = [
    ("Мария Забродина", "175"),
    ("Дарья Демидова", "176")
]
cursor.executemany("INSERT INTO Student_room (Name, Numberoom) VALUES (?, ?)", student_rooms)

conn.commit()
conn.close()

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM Student")
students = cursor.fetchall()

all_data = []

# Для каждого студента ищем его комнату
for student in students:
    student_id, name, group_num = student

    # Ищем комнату студента
    cursor.execute("SELECT Numberoom FROM Student_room WHERE Name = ?", (name,))
    room_result = cursor.fetchone()

    student_info = {
        "ID": student_id,
        "Name": name,
        "Numbergroop": group_num
    }

    if room_result:
        room_number = room_result[0]
        cursor.execute("SELECT * FROM Room WHERE Name_room = ?", (room_number,))
        room_data = cursor.fetchone()

        if room_data:
            room_id, room_name, room_size, room_status, room_ob = room_data
            student_info["Room"] = {
                "ID": room_id,
                "Name_room": room_name,
                "Size": room_size,
                "Status": room_status,
                "Number_ob": room_ob
            }

    all_data.append(student_info)

conn.close()

#Создание папки out
if not os.path.exists("out"):
    os.makedirs("out")

#Сохранение в JSON
with open("out/data.json", "w", encoding="utf-8") as f:
    json.dump(all_data, f, indent=2, ensure_ascii=False)
#Сохранение в CSV
with open("out/data.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["ID", "Name", "Group", "Room_Number", "Room_Size", "Room_Status", "Room_Number_ob"])

    for student in all_data:
        if "Room" in student:
            room = student["Room"]
            writer.writerow([
                student["ID"],
                student["Name"],
                student["Numbergroop"],
                room["Name_room"],
                room["Size"],
                room["Status"],
                room["Number_ob"]
            ])
        else:
            writer.writerow([
                student["ID"],
                student["Name"],
                student["Numbergroop"],
                "", "", "", ""
            ])
#Сохранение в XML
xml_content = '<?xml version="1.0" encoding="UTF-8"?>\n<data>\n'
for student in all_data:
    xml_content += '  <student>\n'
    xml_content += f'    <ID>{student["ID"]}</ID>\n'
    xml_content += f'    <Name>{student["Name"]}</Name>\n'
    xml_content += f'    <Numbergroop>{student["Numbergroop"]}</Numbergroop>\n'

    if "Room" in student:
        xml_content += '    <Room>\n'
        room = student["Room"]
        xml_content += f'      <ID>{room["ID"]}</ID>\n'
        xml_content += f'      <Name_room>{room["Name_room"]}</Name_room>\n'
        xml_content += f'      <Size>{room["Size"]}</Size>\n'
        xml_content += f'      <Status>{room["Status"]}</Status>\n'
        xml_content += f'      <Number_ob>{room["Number_ob"]}</Number_ob>\n'
        xml_content += '    </Room>\n'

    xml_content += '  </student>\n'
xml_content += '</data>'

with open("out/data.xml", "w", encoding="utf-8") as f:
    f.write(xml_content)

#Сохранение в YAML
yaml_content = ""
for student in all_data:
    yaml_content += "- Student:\n"
    yaml_content += f"    ID: {student['ID']}\n"
    yaml_content += f"    Name: {student['Name']}\n"
    yaml_content += f"    Numbergroop: {student['Numbergroop']}\n"

    if "Room" in student:
        yaml_content += "    Room:\n"
        room = student["Room"]
        yaml_content += f"      ID: {room['ID']}\n"
        yaml_content += f"      Name_room: {room['Name_room']}\n"
        yaml_content += f"      Size: {room['Size']}\n"
        yaml_content += f"      Status: {room['Status']}\n"
        yaml_content += f"      Number_ob: {room['Number_ob']}\n"

    yaml_content += "\n"

with open("out/data.yaml", "w", encoding="utf-8") as f:
    f.write(yaml_content)
