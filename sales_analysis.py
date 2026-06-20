import pandas as pd
import matplotlib.pyplot as plt
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Product": ["Laptop", "Phone", "Laptop", "Tablet", "Phone", "Laptop"],
    "Sales": [1200, 800, 1500, 600, 950, 1800],
    "Units": [10, 20, 12, 8, 25, 15]
}

df = pd.DataFrame(data)
print(df)
print("Total Sales:", df["Sales"].sum())
print("Average Sales:", df["Sales"].mean())
print("Best Month:", df.loc[df["Sales"].idxmax(), "Month"])
product_sales = df.groupby("Product")["Sales"].sum()
print(product_sales)
plt.bar(product_sales.index, product_sales.values)
plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.show()
plt.plot(df["Month"], df["Sales"], marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()