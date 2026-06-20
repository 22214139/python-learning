import pandas as pd
data = {
    "Name": ["Ali", "Sara", "Reza", "Mina"],
    "Grade": [85, 90, 75, 95],
    "Age": [20, 22, 21, 23]
}

df = pd.DataFrame(data)
print(df)
print(df["Grade"])
print("---")
print(df["Grade"].mean())
print(df["Grade"].max())
high_grades = df[df["Grade"] > 85]
print(high_grades)
df.to_csv("grades.csv", index=False)
print("saved!")

df2 = pd.read_csv("grades.csv")
print(df2)