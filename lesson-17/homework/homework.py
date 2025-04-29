import pandas as pd
import numpy as np

data = {
    'First Name': ['Alice', 'Bob', 'Charlie', 'David'], 
'Age': [25, 30, 35, 40], 'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}

df = pd.DataFrame()


df.columns.re = ['first_name', 'age', 'city']


df.columns.re = ['first_name', 'age']
print("\nFirst Name and Age columns:")

print("First 3 rows:")
print(df.head(3))

mean_age = df['age'].mean()
print("\nMean age:", mean_age)

print("\nFirst Name and City columns:")
print(df[['first_name', 'city']])

print("\nSummary statistics:")
print(df.describe())
