import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title='HR Dashboard',
    page_icon='📊',
    layout='wide',
    initial_sidebar_state='expanded'
)

@st.cache_data
def load_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    df.columns = df.columns.str.strip()
    required = {'Department', 'Gender', 'DateJoined', 'DateLeft'}
    missing = required - set(df.columns)
    if missing:
        st.error(f"Your CSV is missing columns: {', '.join(sorted(missing))}")
        st.stop()
    df['Department'] = df['Department'].astype(str).str.strip().str.title()
    df['Gender'] = df['Gender'].astype(str).str.strip().str.lower()
    df['DateJoined'] = pd.to_datetime(df['DateJoined'], errors='coerce')
    df['DateLeft'] = pd.to_datetime(df['DateLeft'], errors='coerce')
    if 'Salary' in df.columns:
        df['Salary'] = pd.to_numeric(df['Salary'], errors='coerce')
    df['Status'] = df['DateLeft'].apply(lambda x: 'Former' if pd.notnull(x) else 'Current')
    today = pd.Timestamp.today().normalize()
    df['TenureMonths'] = ((df['DateLeft'].fillna(today) - df['DateJoined']).dt.days // 30)
    df = df.dropna(subset=['DateJoined'])
    return df

df = load_data('new_hr_data.csv')

st.sidebar.header('Filters')
departments = st.sidebar.multiselect('Select Departments', options=df['Department'].unique(), default=df['Department'].unique())
status_filter = st.sidebar.multiselect('Select Status', options=df['Status'].unique(), default=df['Status'].unique())

df_filtered = df[(df['Department'].isin(departments)) & (df['Status'].isin(status_filter))]

st.title('📊 HR Dashboard')
st.markdown('---')

col1, col2, col3 = st.columns(3)
col1.metric("Total Employees", len(df_filtered))
col2.metric("Current Employees", len(df_filtered[df_filtered['Status'] == 'Current']))
col3.metric("Former Employees", len(df_filtered[df_filtered['Status'] == 'Former']))

st.markdown("### Gender Distribution")
gender_counts = df_filtered['Gender'].value_counts()
fig1, ax1 = plt.subplots()
ax1.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')
st.pyplot(fig1)

st.markdown("### Department-wise Employee Count")
dept_counts = df_filtered['Department'].value_counts()
fig2, ax2 = plt.subplots()
ax2.bar(dept_counts.index, dept_counts.values)
plt.xticks(rotation=45)
st.pyplot(fig2)

st.markdown("### Average Salary by Department")
if 'Salary' in df_filtered.columns:
    avg_salary = df_filtered.groupby('Department')['Salary'].mean().sort_values(ascending=False)
    fig3, ax3 = plt.subplots()
    avg_salary.plot(kind='bar', ax=ax3)
    plt.xticks(rotation=45)
    st.pyplot(fig3)
