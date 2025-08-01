import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('sales_data.csv')
'''
print('columns in your file:', df.columns)
df['Date'] = pd.to_datetime(df['Date'])
monthly_sales = df.groupby(df['Date'].dt.to_period('M'))['Total'].sum()
monthly_sales.index = monthly_sales.index.to_timestamp()
'''
'''
# Step 4: Plot the monthly sales
plt.figure(figsize=(10, 6))
plt.plot(monthly_sales.index, monthly_sales.values, marker='o', linestyle='-', color='blue')
plt.title('Monthly Total Sales')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid(True)
plt.tight_layout()
plt.show()
'''

df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.to_period('M')
'''
monthly_avg_order_value = df.groupby('Month')['Total'].mean()
print(monthly_avg_order_value)
import matplotlib.pyplot as plt
monthly_avg_order_value.plot(kind='line', marker='o', color='green')
plt.title('Average Order Value per Month')
plt.xlabel('Month')
plt.ylabel('Average Order Value (₹)')
plt.grid(True)
plt.tight_layout()
plt.show()
'''
region_sales = df.groupby('Region')['Total'].sum().sort_values(ascending=False)
print(region_sales)
region_sales.plot(kind='bar', color='cornflowerblue')
plt.title('Total Sales by Region')
plt.xlabel('Region')
plt.ylabel('Total Sales')
plt.grid(True,axis="y")
plt.tight_layout()
plt.show()