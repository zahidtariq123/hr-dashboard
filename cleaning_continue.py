import pandas as pd
'''
data = {
    'Name': [' alice ', 'BOB', 'Charlie', ' dave ', 'Eve', None],
    'DOB': ['01-02-1990', '1991/03/04', 'March 5, 1992', '19930406', 'not a date', ''],
    'Salary': ['$50,000', '60000', '70k', 'Not Available', '85,000', '55.000'],
    'Department': ['HR', 'hr', 'Finance', 'FINANCE', 'marketing', 'Marketing'],
    'Phone': ['+1 (555) 123-4567', '555-234-5678', '(555)345-6789', '555.456.7890', '555 567 8901', 'missing']
}

df = pd.DataFrame(data)
print('before cleaning',df)
# print("Original DataFrame:\n", df)
# Clean 'Name' column: strip and title-case
# df['Name'] = df['Name'].str.strip().str.title().fillna('Unknown')


# Clean 'DOB' column: convert to datetime
df['DOB'] = pd.to_datetime(df['DOB'], errors='coerce')

# Clean 'Salary': remove non-numeric characters, convert to float
df['Salary'] = df['Salary'].str.replace(r'[^0-9.]', '', regex=True)
df['Salary'] = pd.to_numeric(df['Salary'], errors='coerce')


# Clean 'Department': normalize to title-case
df['Department'] = df['Department'].str.strip().str.lower().str.title()

# Clean 'Phone': remove all non-digits
# df['Phone'] = df['Phone'].str.replace(r'\D', '', regex=True)
df['Phone'] = df['Phone'].replace('', pd.NA)

print('after cleaning',df)
'''
data = {
    'name' : ['zahid','atiq','wassi','tajamul'],
    'department' : ['alpha','techguy','joker','hacker'],
    'phone' : ['1622344','234445','33445','0003546'],
}
df = pd.DataFrame(data)
print(df)