import csv
import os
class Student:
    def __init__(self, name, student_id, grade):
        self.name = name
        self.student_id = student_id
        self.grade = grade

    def show(self):
        print("Name:", self.name)
        print("ID:", self.student_id)
        print("Grade:", self.grade)
        print("---")
students = []
FILE = "students.csv"
def add_student():
    name = input("Name: ")
    student_id = input("ID: ")
    grade = float(input("Grade: "))
    s = Student(name, student_id, grade)
    students.append(s)
    print("Student added!")
def show_all():
    if len(students) == 0:
        print("No students!")
        return
    for s in students:
        s.show()
def save():
    with open(FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "ID", "Grade"])
        for s in students:
            writer.writerow([s.name, s.student_id, s.grade])
    print("Saved!")
def load():
    if not os.path.exists(FILE):
        return
    with open(FILE, "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            s = Student(row[0], row[1], float(row[2]))
            students.append(s)
    print("Loaded!")
load()

while True:
    print("1: add student")
    print("2: show all")
    print("3: save")
    print("q: exit")
    choice = input("choice: ")
    if choice == "q":
        break
    elif choice == "1":
        add_student()
    elif choice == "2":
        show_all()
    elif choice == "3":
        save()
    else:
        print("invalid choice!")