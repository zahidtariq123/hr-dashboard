import streamlit as st
import pandas as pd
import matplotlib.pyplot as  plt
import io
st.set_page_config(page_title="Hr Dashboard",layout='wide')
df= pd.read_csv('hr_data.csv')
df['Gender'] = df['Gender'].str.strip().str.lower()
df['DateJoined']=pd.to_datetime(df['DateJoined'])
df['DateLeft'] = pd.to_datetime(df['DateLeft'])
df['Status'] = df['DateLeft'].apply(lambda x: 'Former'if pd.notnull(x) else 'Current')
today = pd.Timestamp.today()
df['TenureMonths'] = ((df['DateLeft'].fillna(today) - df['DateJoined']).dt.days // 30)
st.sidebar.header('Filter Options')
status_filter = st.sidebar.multiselect('Select Status',options=df['Status'].unique(),default=df['Status'].unique())
dept_filter = st.sidebar.multiselect("Select Department",options=df['Department'].unique(),default=df['Department'].unique())
filtered_df = df[(df['Status'].isin(status_filter)) & (df['Department'].isin(dept_filter))]
tab1, tab2, tab3 = st.tabs(['KPIs','Charts','Raw Data'])
with tab1:
    st.subheader('Key Metrics')
    total_employees = len(filtered_df)
    current_employees = filtered_df['Status'].value_counts().get('Current',0)
    former_employees = filtered_df['Status'].value_counts().get('Former',0)
    col1,col2,col3 = st.columns(3)
    col1.metric('Total Employees',total_employees)
    col2.metric('Current Employees',current_employees)
    col3.metric('Former Employees',former_employees)
    with tab2:
        st.subheader('Employee Charts')
        st.markdown('Status Distribution')
        status_counts = df['Status'].value_counts()
        fig1, ax1 = plt.subplots()
        ax1.pie(status_counts,labels=status_counts.index,autopct='%11f%%',startangle=90)
        ax1.axis('equal')
        st.pyplot(fig1)
        st.markdown('Employees Per Department')
        dept_counts = filtered_df['Department'].value_counts()
        fig2, ax2 = plt.subplots()
        ax2.bar(dept_counts.index,dept_counts.values,color='skyblue')
        ax2.set_xlabel('Departments')
        ax2.set_ylabel("Number of Employees")
        ax2.set_xticklabels(dept_counts.index,rotation=45)
        st.pyplot(fig2)
        st.markdown('Monthly Join Trend')
        monthly_join = filtered_df.groupby(filtered_df['DateJoined'].dt.to_period('M')).size()
        monthly_join.index = monthly_join.index.astype(str)
        fig3, ax3 = plt.subplots()
        ax3.plot(monthly_join.index,monthly_join.values,marker='o',color='green')
        ax3.set_xlabel('Months')
        ax3.set_ylabel('Joins')
        ax3.set_title('Employees Joined per month')
        plt.xticks(rotation=45)
        plt.grid(True)
        st.pyplot(fig3)
        st.markdown('Average Salary by Department')
        avg_salary = filtered_df.groupby('Department')['Salary'].mean().round(2)
        fig4, ax4 = plt.subplots()
        ax4.bar(avg_salary.index,avg_salary.values,color='orange')
        ax4.set_xlabel('Department')
        ax4.set_ylabel('Salary')
        ax4.set_xticklabels(avg_salary.index,rotation=45)
        st.pyplot(fig4)
        st.markdown('Gender Distribution')
        male_count = filtered_df['Gender'].value_counts().get('male',0)
        female_count = filtered_df['Gender'].value_counts().get('female',0)
        col1, col2 = st.columns(2)
        col1.metric('Total Males',male_count)
        col2.metric('Total females',female_count)
        gender_counts = filtered_df['Gender'].value_counts()
        fig_gender, ax_gender = plt.subplots()
        ax_gender.pie(gender_counts,labels=gender_counts.index.str.title(),autopct='%1.1f%%',startangle=90)
        ax_gender.axis('equal')
        st.pyplot(fig_gender)

        with tab3:
            st.subheader('Raw HR Data')
            st.dataframe(filtered_df)
            csv = filtered_df.to_csv(index=False)
            st.download_button(
                label="Download Filtered Data as csv",
                data=csv,
                file_name="filtered_hr_data.csv",
                mime='text/csv'


            )






