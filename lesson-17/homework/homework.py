import pandas as pd
import numpy as np

# Step 1: Create the DataFrame
data = {
    'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)

# Step 2: Rename columns using a function
df.columns = ['first_name', 'age', 'city']

# Step 3: Print the first 3 rows
print("First 3 rows:")
print(df.head(3))

# Step 4: Find the mean age
mean_age = df['age'].mean()
print("\nMean age:", mean_age)

# Step 5: Select and print only the 'first_name' and 'city' columns
print("\nFirst Name and City columns:")
print(df[['first_name', 'city']])

# Step 7: Display summary statistics
print("\nSummary statistics:")
print(df.describe())
