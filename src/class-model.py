class Student:
    def __init__(self, id, name, numbergroop):
        self.id = id
        self.name = name
        self.numbergroop = numbergroop

class Room:
    def __init__(self, id, name,size, status, id_obsh):
        self.id = id
        self.name = name
        self.size = size
        self.status = status
        self.id_obsh = id_obsh

class Student_room:
    def __init__(self, id, id_students, id_room):
        self.id = id
        self.id_students = id_students
        self.id_room = id_room

class House_student:
    def __init__(self, id, name, numberoom):
        self.id = id
        self.name = name
        self.numberoom = numberoom

class Student_doc:
    def __init__(self, id, name, number):
        self.id = id
        self.name = name
        self.number = number
