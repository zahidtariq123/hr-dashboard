import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
st.title('Hr Dashboard')
df = pd.read_csv('hr_data.csv')
df['Status'] = df['DateLeft'].apply(lambda x: 'Former' if pd.notnull(x) else 'Current')
if st.checkbox('Show Raw Data'):
    st.write(df)
total =len(df)
current = df['Status'].value_counts().get("Current", 0)
former = df['Status'].value_counts().get("Former", 0)
st.metric('Total Employees',total)
st.metric('Current Employees',current)
st.metric('Former Employees',former)
status_count =df['Status'].value_counts()
fig, ax = plt.subplots()
status_count.plot(kind='bar',color=['green','red'],ax=ax)
plt.title('Employee Status count')
plt.xlabel('Status')
plt.ylabel('Number of Employees')
st.pyplot(fig)
dept_satatus_count=df.groupby(['Department', 'Status']).size().unstack(fill_value=0)
fig2,ax2=plt.subplots()
dept_satatus_count.plot(kind='bar',stacked=True,color=['green','red'],ax=ax2)
plt.title('Current vs Former Employees by Department')
plt.xlabel('Department')
plt.ylabel('Number of Employees')
st.pyplot(fig2)



