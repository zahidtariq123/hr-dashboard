import pandas as pd

# df = pd.DataFrame({
#     'id': [1, 2, 2, 3, 4, 4],
#     'name': ['Alice', 'Bob', 'Bob', 'Charlie', 'Dave', 'Dave']
# })
#
# print("Original:\n", df)
#
# df_cleaned = df.drop_duplicates()
# print("\nAfter drop_duplicates():\n", df_cleaned)

#df = pd.DataFrame({
    #'id': [1, 2, 3, 4, 5, 6],
    #'email': ['a@example.com', 'b@example.com', 'a@example.com', 'd@example.com', 'a@example.com', 'f@example.com'],
    #'name': ['Alice', 'Bob', 'Alice', 'Dave', 'Alice', 'Frank']
#})

# Remove duplicate emails, keep the first
# df_unique = df.drop_duplicates(subset='email', keep='first')
# df_unique = df.drop_duplicates(subset='email', keep='last')
# print(df_unique)

# df.drop_duplicates(inplace=True)
#
# print(df)
# df['is_duplicate'] = df.duplicated()
# df['is_duplicate_email'] = df.duplicated(subset='email', keep=False)
#duplicate_count = df.duplicated().sum()
#print(df)
#print(duplicate_count)
'''
df = pd.DataFrame({
    'id': [1, 2, 3, 4, 5],
    'name': ['Alice', 'Bob', 'Alice', 'Alice', 'Bob'],
    'email': ['a@example.com', 'b@example.com', 'a@example.com', 'a@example.com', 'b@example.com']
})

# Remove duplicates where both name and email match
df_unique = df.drop_duplicates(subset=['name', 'email'], keep='first')
print(df_unique)
# Keep only rows that are duplicated (excluding the first)
dups_only = df[df.duplicated(subset=['name', 'email'], keep=False)]
print(dups_only)
df = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'value': [None, None, 100, 100]
})

# Drop duplicates including NaNs (default behavior treats NaNs as unique)
df_dropna_false = df.drop_duplicates()

# Treat NaNs as equal by filling them first
df_equal_nulls = df.fillna('NULL').drop_duplicates()
'''
'''
df = pd.DataFrame({
    'id': [1, 2, 3, 3],
    'value': [None, None, 100, 100]
})

# Drop duplicates including NaNs (default behavior treats NaNs as unique)
df_dropna_false = df.drop_duplicates()
print(df)
print(df_dropna_false)

# Treat NaNs as equal by filling them first
#df_equal_nulls = df.fillna('NULL').drop_duplicates()
#print(df_equal_nulls)
'''
'''
df = pd.DataFrame({
    'id': [1,2,3,4,5],
    'employee': ['zahid','atiq','momin','zaid','none']
})
#correct = df.drop_duplicates()
#print(correct)
dup = df.drop_duplicates(subset='id', keep=False)
print(dup)
'''
df = pd.DataFrame({
    'id': [1,2,3,4,5],
    'name': ['lexi','damon','stephen','aleena','alark']
})
print(df)