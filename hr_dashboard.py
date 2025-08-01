import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
st.title('Hr Dashboard')
df = pd.read_csv('hr_data.csv')
df.columns = df.columns.str.strip().str.replace(' ','')
df['Status'] = df['DateLeft'].apply(lambda x: "Former" if pd.notnull(x) else 'Current')
df["DateJoined"] = pd.to_datetime(df['DateJoined'])
df['DateLeft'] = pd.to_datetime(df['DateLeft'],errors='coerce')
if st.checkbox('Show Raw Data'):
    st.write(df)

total_employees = len(df)
current_employees = df['Status'].value_counts().get('Current',0)
former_employees = df['Status'].value_counts().get('Former',0)
col1,col2,col3 = st.columns(3)
col1.metric('Total_Employees',total_employees)
col2.metric('Current_Employees',current_employees)
col3.metric('Former_Employees',former_employees)
avg_salary = df[df['Status'] == 'Current'].groupby('Department')['Salary'].mean().reset_index()
fig, ax = plt.subplots()
ax.bar(avg_salary['Department'], avg_salary['Salary'],color="skyblue")
ax.set_title('Average Salary by Department')
ax.set_xlabel('Department')
ax.set_ylabel('Average Salary')
plt.xticks(rotation=45)
st.pyplot(fig)