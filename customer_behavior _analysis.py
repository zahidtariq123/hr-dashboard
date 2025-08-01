
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('sales_data.csv')
df['Date'] = pd.to_datetime(df['Date'])
order_count = df.groupby('SalesPerson')['OrderID'].count().sort_values(ascending=False)
sales_by_person = df.groupby('SalesPerson')['Total'].sum().sort_values(ascending=False)
print('Top 5 SalesPeople by Order Handled:')
print(order_count.head())
print('Top 5 SalesPeople by Sales Amount:')
print(sales_by_person.head())
