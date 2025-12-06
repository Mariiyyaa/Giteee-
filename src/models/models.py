class Student:
    def __init__(self, id: int, name: str, numbergroop: str):
        self.id = id
        self.name = name
        self.numbergroop = numbergroop

    def __repr__(self):
        return f"Student(id={self.id}, name='{self.name}', numbergroop='{self.numbergroop}')"


class Starosta:
    def __init__(self, id: int, name_starost: str, zadacha_starost: str):
        self.id = id
        self.name_starost = name_starost
        self.zadacha_starost = zadacha_starost

    def __repr__(self):
        return f"Starosta(id={self.id}, name_starost='{self.name_starost}', zadacha_starost='{self.zadacha_starost}')"

    def __repr__(self):
        return f"Starosta(id={self.id}, name_starost='{self.name_starost}', zadacha_starost='{self.zadacha_starost}')"