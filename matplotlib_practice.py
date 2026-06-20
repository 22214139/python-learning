import matplotlib.pyplot as plt
names = ["Ali", "Sara", "Reza", "Mina"]
grades = [85, 90, 75, 95]

plt.bar(names, grades)
plt.title("Student Grades")
plt.xlabel("Name")
plt.ylabel("Grade")
plt.show()
months = [1, 2, 3, 4, 5]
sales = [100, 150, 120, 180, 160]

plt.plot(months, sales)
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()
subjects = ["Math", "Science", "English"]
scores = [40, 35, 25]

plt.pie(scores, labels=subjects)
plt.title("Score Distribution")
plt.show()