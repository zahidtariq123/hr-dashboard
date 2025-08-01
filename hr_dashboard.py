import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
gender_counts = df[df["Status"] == 'Current']['Gender'].value_counts()
male_count = gender_counts.get('Male', 0)
female_count = gender_counts.get('Female', 0)
col1, col2 = st.columns(2)
col1.metric('Total Male Employees', male_count)
col2.metric('Total Female Employees', female_count)
fig2, ax2 = plt.subplots()
ax2.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', colors=['lightblue', 'lightpink'])
ax2.set_title('Gender Distribution (Current Employees)')
st.pyplot(fig2)

