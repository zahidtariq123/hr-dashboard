import pandas as pd

# data = {
#   'name': ['sam', 'pam', 'tom'],
#    'marks': [None, 5.1, 6.2]
#}
# print(data)

#df = pd.DataFrame(data)
# print(df)
# print(df.name)
# print(df['name'])
# print(df.marks)
# print(df)
# print(df.info())
# print(df.head())
# print(df.tail(1))
'''
import pandas as pd

# Create some sample data
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

# Turn it into a DataFrame
df = pd.DataFrame(data)

# Save it as a CSV file
df.to_csv('my_data.csv', index=False)

print("CSV file created successfully!")
'''

#
# # Load a CSV file
# df = pd.read_csv('my_data.csv')
#
# # Look at the first few rows
# print(df.head())
#
# # Get basic info about data
# #print(df.info())
#
# # Quick summary stats
#  #print(df.describe())
#


df = pd.read_csv('employees.csv')
# print(df)

# print(df.info())

# print(df.head())
'''
import numpy as np

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "Age": [29, np.nan, 35, 40, np.nan],
    "Gender": ["Female", "Male", np.nan, "Male", "Female"],
    "Salary": [70000, 50000, 80000, np.nan, np.nan],
    "Department": ["HR", "Engineering", "Sales", "Marketing", np.nan]
}

df = pd.DataFrame(data)
# print(df.info())

# print(df.isnull())
# print(df.isnull().sum())

# df_cleaned = df.dropna()
# print(df_cleaned)
# print(df)

# Fill missing ages with the mean age
df["Age"].fillna(df["Age"].mean(), inplace=True)

# Fill missing salary with 0
df["Salary"].fillna(0, inplace=True)

# Fill missing gender with a placeholder
df["Gender"].fillna("Not Specified", inplace=True)

# Fill missing department with 'Unknown'
df["Department"].fillna("Unknown", inplace=True)
print(df)
'''
import pandas as pd

import numpy as np

# Example DataFrame
data = {
    'Id': [1,2,3,4,5,],
    'Name': ['Alice', 'Bob', None, 'dave', 'Eve'],
    'Age': [25, None, 22, 30, 29],
    'City': ['New York', 'Los Angeles', 'New York', None, 'Chicago'],
    'Salary': ['50000', '60000', '55000', '70000', 'not available']
}

df = pd.DataFrame(data)
#print(df)
#to find the missing data
#print(df.isnull().sum())
#df_cleaned = df.dropna()
#print(df_cleaned)
#df['Age'].fillna(df['Age'].mean(), inplace=True)
#print(df)
#df['City'].fillna('unknown',inplace = True)
#print(df)
#df['Salary'] = pd.to_numeric(df['Salary'], errors='coerce')  # 'not available' becomes NaN
#print(df)
#df.drop_duplicates(inplace=True)
#print(df)
#df.rename(columns={'Name' : 'fullname', 'City' : 'location'}, inplace=True)
#print(df)
# df['Name'] = df['Name'].fillna('unknown')
# print(df)