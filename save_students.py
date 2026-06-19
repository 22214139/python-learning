import csv

students = [
    ["Ali", "001", 85],
    ["Sara", "002", 90],
    ["Reza", "003", 75],
]

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "ID", "Grade"])
    for s in students:
        writer.writerow(s)

print("saved!")
with open("students.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)