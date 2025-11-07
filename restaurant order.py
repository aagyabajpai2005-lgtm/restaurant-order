import numpy as np
import pandas as pd
data = {
    'Order_ID': [201, 202, 203, 204, 205, 206],
    'Customer': ['VANSHIKA', 'SNEHA', 'BUBLY', 'NEHA', 'SAKSHI', 'IQRA'],
    'Item': ['Pizza', 'Burger', 'Pasta', 'Pizza', 'Sandwich', 'Burger'],
    'Quantity': [2, 1, 3, 1, 2, 2],
    'Price': [250, 120, 180, 250, 150, 120],
    'Date': ['2025-01-02', '2025-01-03', '2025-01-03', '2025-01-04', '2025-01-04', '2025-01-05']
}

df = pd.DataFrame(data)
print(df)

df['Total'] = df['Quantity'] * df['Price']
print("\nUpdated DataFrame:\n", df)
amounts = np.array(df['Total'])
print("\nTotal Revenue:", np.sum(amounts))
print("Average Order Value:", np.mean(amounts))
print("Highest Order Value:", np.max(amounts))
print("Lowest Order Value:", np.min(amounts))

# Top-Selling Item
top_item = df.groupby('Item')['Quantity'].sum().sort_values(ascending=False)
print("\nTop-Selling Items:\n", top_item)

# Revenue by Item
revenue_by_item = df.groupby('Item')['Total'].sum()
print("\nRevenue by Each Item:\n", revenue_by_item)

# Orders by Customer
orders_by_customer = df.groupby('Customer')['Total'].sum()
print("\nCustomer-wise Spending:\n", orders_by_customer)

# Find the most valuable customer
top_customer = orders_by_customer.idxmax()
print("\nMost Valuable Customer:", top_customer)

# Find average quantity per order
avg_qty = np.mean(df['Quantity'])
print("\nAverage Quantity per Order:", avg_qty)

