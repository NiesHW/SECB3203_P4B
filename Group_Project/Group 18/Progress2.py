import numpy as np # linear algebra
import pandas as pd # data processing, CSV file 
from sklearn.preprocessing import StandardScaler

# Importing dataset
path = 'D:\\Python\\diabetes.csv'
df = pd.read_csv(path)

# Display first few rows of DataFrame
print(df.head())

print(df.info())

# Check for missing values
print(df.isnull())

# Check missing values in each columns
print(df.isnull().sum())

# Check for duplicate rows
duplicate_rows = df[df.duplicated()]
print(duplicate_rows)

# Display data types
print(df.dtypes)

numeric_data = df.select_dtypes(include=['float64', 'int64'])

# Data Normalization (Z-Score)
scaler = StandardScaler()
df_normalized = pd.DataFrame(scaler.fit_transform(numeric_data), columns = df.columns)

print("Normalized DataFrame: ")
print(df_normalized) 

# Binning the 'age' columns
bins = [20, 30, 40, 50, 60, 70, 80, 90]
labels = ['20-30', '31-40', '41-50', '51-60', '61-70', '71-80', '81-90']
df['age_grouop'] = pd.cut(df['Age'], bins=bins, labels=labels, right=False)
print(df['age_grouop'])
