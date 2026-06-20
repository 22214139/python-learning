import pandas as pd
import matplotlib.pyplot as plt
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Product": ["Laptop", "Phone", "Laptop", "Tablet", "Phone", "Laptop"],
    "Sales": [1200, 800, 1500, 600, 950, 1800],
    "Units": [10, 20, 12, 8, 25, 15]
}

df = pd.DataFrame(data)
product_sales = df.groupby("Product")["Sales"].sum()
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
fig.suptitle("Sales Dashboard")
axes[0].bar(product_sales.index, product_sales.values)
axes[0].set_title("Sales by Product")
axes[0].set_xlabel("Product")
axes[0].set_ylabel("Sales")
axes[1].plot(df["Month"], df["Sales"], marker="o", color="green")
axes[1].set_title("Monthly Trend")
axes[1].set_xlabel("Month")
axes[1].set_ylabel("Sales")
axes[2].pie(product_sales.values, labels=product_sales.index, autopct="%1.1f%%")
axes[2].set_title("Sales Share")
plt.tight_layout()
plt.show()