import pandas as pd
data ={
    'name':['alice','jhon','aamir','brian','rafi'],
    'salary':[70000,55000,40000,60000,35000],
    'department':['HR','SALES','HR','IT','SALES']
}
df = pd.DataFrame(data)
print('oringinal_data')
print(df)
def grade(salary):
    if salary>=60000:
        return 'A'
    elif salary>=40000:
        return 'B'
    else:
        return 'C'
df['salary_grade']=df['salary'].apply(grade)
report = df.groupby(['department','salary_grade']).agg(
    total_employees=('name','count'),avg_salary=('salary','mean')
).reset_index()
print('\n wise Salary Grade Report:')
print(report)

