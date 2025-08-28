import mysql.connector
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(
    page_title='HR Performance Dashboard',
    page_icon='🧑‍💼',
    layout='wide',
    initial_sidebar_state='expanded'
)
st.title('📊HR Performance Dashboard')
st.markdown('Live dashboard reading from MYSQL: monitor, headcount, churn, salaries and trends.')
st.markdown('____')

@st.cache_data(show_spinner=True)
def load_hr_data(
        host: str='localhost',
        user: str='root',
        password: str='',
        database: str='hr_db'
) -> pd.DataFrame:
    "connect to MYSQL and return a tidy employees x departments dataframe."
    conn = mysql.connector.connect(host=host, user=user, password=password, database=database)
    querry = """
    select
        e.id as employee_id,
        e.name as employee_name,
        e.salary as salary,
        e.gender as gender,
        e.date_joined as date_joined,
        e.date_left as date_left,
        d.name as department
    from employees e
    left join departments d on d.id = e.dept_id;
    """
    df = pd.read_sql_query(querry, conn)
    conn.close()
    df.columns = df.columns.str.strip()
    df['gender'] = df['gender'].astype(str).str.strip().str.lower()
    df['department'] = df['department'].astype(str).str.strip().str.title()
    df['date_joined'] = pd.to_datetime(df['date_joined'], errors='coerce')
    df['date_left'] = pd.to_datetime(df['date_left'], errors='coerce')
    df['Status'] = np.where(df['date_left'].notna(), 'Former', 'Current')
    today = pd.Timestamp.today().normalize()
    df['TenureMonths'] = ((df['date_left'].fillna(today) - df['date_joined']).dt.days // 30)
    return df

try:
    df = load_hr_data()
except Exception as e:
    st.error(f"❌ Could not load data from MySQL: {e}")
    st.stop()

st.sidebar.header('Filter Options')
dept_options = sorted(df['department'].dropna().unique().tolist())
status_options = ['Current', 'Former']
gender_options = sorted(df['gender'].dropna().unique().tolist())
dept_filter = st.sidebar.multiselect('Department', options=dept_options, default=dept_options)
status_filter = st.sidebar.multiselect('Employee Status', options=status_options, default=status_options)
gender_filter = st.sidebar.multiselect('Gender', options=gender_options, default=gender_options)

min_date = pd.to_datetime(df['date_joined'].min())
max_date = pd.to_datetime(df['date_joined'].max())

if pd.isna(min_date):
    min_date = pd.Timestamp.today() - pd.Timedelta(days=365*3)
if pd.isna(max_date):
    max_date = pd.Timestamp.today()
date_range = st.sidebar.date_input('Joined Between', value=(min_date.date(), max_date.date()))
start_date, end_date = pd.to_datetime(date_range[0]), pd.to_datetime(date_range[1])


show_raw = st.sidebar.checkbox('Show Raw Filtered Data', value=False, key='show_raw')

filtered_df = df[
    (df['department'].isin(dept_filter)) &
    (df['Status'].isin(status_filter)) &
    (df['gender'].isin(gender_filter)) &
    (df['date_joined'].between(start_date, end_date))
].copy()

tab1, tab2, tab3 = st.tabs(['KPIs', 'Charts', 'Data'])

with tab1:
    st.subheader('Key HR Metrics')
    total_employees = len(filtered_df)
    current_employees = (filtered_df['Status'] == 'Current').sum()
    former_employees = (filtered_df['Status'] == 'Former').sum()
    avg_salary = filtered_df['salary'].mean() if 'salary' in filtered_df.columns else np.nan
    avg_tenure = filtered_df['TenureMonths'].mean() if 'TenureMonths' in filtered_df.columns else np.nan
    k1, k2, k3, k4, k5 = st.columns(5)
    k1.metric('Total Employees', int(total_employees))
    k2.metric('Current', int(current_employees))
    k3.metric('Former', int(former_employees))
    k4.metric('Avg Salary', f"{avg_salary:,.0f}" if pd.notna(avg_salary) else '__')
    k5.metric('Avg Tenure (months)', f"{avg_tenure:,.1f}" if pd.notna(avg_tenure) else '__')

with tab2:
    st.subheader('Visualization')
    st.markdown('### Employment Status Distribution')
    if not filtered_df.empty:
        status_counts = filtered_df['Status'].value_counts()
        fig1, ax1 = plt.subplots()
        ax1.pie(status_counts.values, labels=status_counts.index, autopct='%1.1f%%', startangle=90)
        ax1.axis('equal')
        st.pyplot(fig1)
    else:
        st.info('No data for selected filters')


    st.markdown('Employees per department')
    if not filtered_df.empty:
        dept_count = filtered_df['department'].value_counts()
        fig2, ax2 = plt.subplots()
        ax2.bar(dept_count.index, dept_count.values)
        ax2.set_xlabel('department')
        ax2.set_ylabel('employees')
        plt.xticks(rotation=45, ha='right')
        st.pyplot(fig2)
    else:
        st.info('No department data for selected filters')


    st.markdown('Monthly Joins Trend')
    if not filtered_df.empty:
        joins = (
            filtered_df
            .dropna(subset=['date_joined'])
            .assign(month=lambda d: d['date_joined'].dt.to_period('M').astype(str))
            .groupby('month').size().reset_index(name='count')
        )
        if not joins.empty:
            fig3, ax3 = plt.subplots()
            ax3.plot(joins['month'], joins['count'], marker='o')
            ax3.set_xlabel('Months')
            ax3.set_ylabel('Joins')
            ax3.set_title('Employees joined per month')
            ax3.grid(True)
            plt.xticks(rotation=25, ha='right')
            st.pyplot(fig3)
        else:
            st.info('No Join date in selected range')
    else:
        st.info('No join data for selected filters')


    st.markdown('### Average Salary By department')
    if 'salary' in filtered_df.columns and not filtered_df['salary'].dropna().empty:
        avg_salary = filtered_df.groupby('department')['salary'].mean().round(2).sort_values(ascending=False)
        fig4, ax4 = plt.subplots()
        ax4.bar(avg_salary.index, avg_salary.values)
        ax4.set_xlabel('Department')
        ax4.set_ylabel('Average salary')
        plt.xticks(rotation=45, ha='right')
        st.pyplot(fig4)
    else:
        st.info('No salary data available')


    st.markdown('Tenure (months) Distribution')
    if 'TenureMonths' in filtered_df.columns and not filtered_df['TenureMonths'].dropna().empty:
        fig5, ax5 = plt.subplots()
        ax5.hist(filtered_df['TenureMonths'].dropna(), bins=10, edgecolor='black')
        ax5.set_xlabel('Tenure Months')
        ax5.set_ylabel('Employees')
        ax5.set_title('Distribution of Employee tenure')
        st.pyplot(fig5)
    else:
        st.info('no tenure data to plot')

with tab3:
    st.subheader('Filtered Data')
    st.dataframe(filtered_df, use_container_width=True)

    csv = filtered_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label='download csv',
        data=csv,
        file_name='filtered_hr_data.csv',
        mime='text/csv'
    )
    if show_raw:
        st.subheader('Raw Filtered Table')
        st.dataframe(filtered_df, use_container_width=True)
