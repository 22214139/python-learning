class Student:
    def __init__(self, name, student_id, grade):
        self.name = name
        self.student_id = student_id
        self.grade = grade

    def show(self):    
        print("Name:", self.name)
        print("ID:", self.student_id)
        print("Grade:", self.grade)
s1 = Student("Ali", "001", 85)
s2 = Student("Sara", "002", 90)
s3 = Student("Reza", "003", 75)

students = [s1, s2, s3]

for s in students:
    s.show()
    print("---")
total = 0
for s in students:
    total = total + s.grade

average = round(total / len(students), 2)
print("Average grade:", average)