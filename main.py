import datetime

class Person:
    def __init__(self, surname, first_name, birth_date, nickname=None):
        self.surname = surname
        self.first_name = first_name
        self.nickname = nickname

        year, month, day = map(int, birth_date.split('-'))
        self.birth_date = datetime.date(year, month, day)

    def get_age(self):
        today = datetime.date.today()
        age = today.year - self.birth_date.year
        if (today.month, today.day) < (self.birth_date.month, self.birth_date.day):
            age -= 1
        return str(age)

    def get_fullname(self):
        return f"{self.surname} {self.first_name}"


person = Person("Ivanov", "Ivan", "1990-01-01")
print(person.get_fullname())
print(person.get_age())

import csv


def modifier(filename):
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]


    for row in data:
        person = Person(row['surname'], row['first_name'], row['birth_date'], row.get('nickname'))
        row['fullname'] = person.get_fullname()
        row['age'] = person.get_age()


    fieldnames = reader.fieldnames + ['fullname', 'age']


    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

