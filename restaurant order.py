import streamlit as st
import pandas as pd
import numpy as np

# ---- App Title ----
st.set_page_config(page_title="Order Analysis Dashboard", layout="wide")
st.title("🍕 Order Analysis Dashboard")

# ---- Create Data ----
data = {
    'Order_ID': [201, 202, 203, 204, 205, 206],
    'Customer': ['VANSHIKA', 'SNEHA', 'BUBLY', 'NEHA', 'SAKSHI', 'IQRA'],
    'Item': ['Pizza', 'Burger', 'Pasta', 'Pizza', 'Sandwich', 'Burger'],
    'Quantity': [2, 1, 3, 1, 2, 2],
    'Price': [250, 120, 180, 250, 150, 120],
    'Date': ['2025-01-02', '2025-01-03', '2025-01-03', '2025-01-04', '2025-01-04', '2025-01-05']
}

df = pd.DataFrame(data)
df['Total'] = df['Quantity'] * df['Price']

# ---- Display Data ----
st.subheader("📋 Orders Data")
st.dataframe(df, use_container_width=True)

# ---- Key Metrics ----
amounts = np.array(df['Total'])
total_revenue = np.sum(amounts)
avg_order_value = np.mean(amounts)
highest_order = np.max(amounts)
lowest_order = np.min(amounts)
avg_qty = np.mean(df['Quantity'])

col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("💰 Total Revenue", f"₹{total_revenue:,.0f}")
col2.metric("📦 Avg Order Value", f"₹{avg_order_value:,.0f}")
col3.metric("⬆️ Highest Order", f"₹{highest_order:,.0f}")
col4.metric("⬇️ Lowest Order", f"₹{lowest_order:,.0f}")
col5.metric("📊 Avg Quantity", f"{avg_qty:.2f}")

# ---- Top-Selling Items ----
st.subheader("🍔 Top-Selling Items")
top_items = df.groupby('Item')['Quantity'].sum().sort_values(ascending=False)
st.bar_chart(top_items)

# ---- Revenue by Item ----
st.subheader("💵 Revenue by Item")
revenue_by_item = df.groupby('Item')['Total'].sum().sort_values(ascending=False)
st.bar_chart(revenue_by_item)

# ---- Customer Spending ----
st.subheader("👥 Customer-wise Spending")
orders_by_customer = df.groupby('Customer')['Total'].sum().sort_values(ascending=False)
st.bar_chart(orders_by_customer)

# ---- Most Valuable Customer ----
top_customer = orders_by_customer.idxmax()
st.success(f"🏆 **Most Valuable Customer:** {top_customer}")

# ---- Summary Table ----
st.subheader("📈 Summary")
summary = pd.DataFrame({
    'Metric': ['Total Revenue', 'Average Order Value', 'Highest Order', 'Lowest Order', 'Average Quantity per Order', 'Top Customer'],
    'Value': [f"₹{total_revenue:,.0f}", f"₹{avg_order_value:,.0f}", f"₹{highest_order:,.0f}", f"₹{lowest_order:,.0f}", f"{avg_qty:.2f}", top_customer]
})
st.table(summary)

