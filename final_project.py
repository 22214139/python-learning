import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data = {
    "Name": ["Ali", "Sara", "Reza", "Mina", "John", "Emma", "Liam", "Zara"],
    "Math": [85, 92, 78, 95, 60, 88, 73, 91],
    "Science": [78, 88, 82, 90, 55, 92, 68, 87],
    "English": [90, 85, 70, 88, 65, 79, 80, 93]
}

df = pd.DataFrame(data)
print(df)
grades = np.array([df["Math"], df["Science"], df["English"]])

print("Math average:", np.mean(df["Math"]))
print("Science average:", np.mean(df["Science"]))
print("English average:", np.mean(df["English"]))
print("Best student:", df.loc[df["Math"].idxmax(), "Name"])
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
fig.suptitle("Student Performance Dashboard")

# chart 1 - math grades
axes[0].bar(df["Name"], df["Math"])
axes[0].set_title("Math Grades")
axes[0].set_xlabel("Student")
axes[0].set_ylabel("Grade")

# chart 2 - average per subject
subjects = ["Math", "Science", "English"]
averages = [np.mean(df["Math"]), np.mean(df["Science"]), np.mean(df["English"])]
axes[1].bar(subjects, averages, color="green")
axes[1].set_title("Subject Averages")
axes[1].set_xlabel("Subject")
axes[1].set_ylabel("Average")

# chart 3 - Mina vs John (best vs worst)
axes[2].plot(subjects, [95, 90, 88], marker="o", label="Mina")
axes[2].plot(subjects, [60, 55, 65], marker="o", label="John")
axes[2].set_title("Best vs Worst")
axes[2].legend()

plt.tight_layout()
plt.show()