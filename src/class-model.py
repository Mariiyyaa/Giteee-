class Student:
    def __init__(self, id, name, numbergroop):
        self.id = id
        self.name = name
        self.numbergroop = numbergroop

class Room:
    def __init__(self, id, name student, size, status, Number_ob):
        self.id = id
        self.name = name
        self.size = size
        self.status = status
        self.number_ob = Number_ob

class Student_room:
    def __init__(self, id, name, number_room):
        self.id = id
        self.name = name
        self.number_room = number_room

class Starosta:
    def __init__(self, id, name_starost, zadacha_starost):
        self.id = id
        self.name_starost = name_starost
        self.zadacha_starost = zadacha_starost
