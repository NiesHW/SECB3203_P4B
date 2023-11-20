import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

path = r"C:\Alzheimer's Prediction\alzheimer.csv"

df = pd.read_csv(path)

# Assuming df is your DataFrame
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Fill missing values with the mean of each numeric column
df.fillna(df.mean(numeric_only=True).round(1), inplace=True)

# Create a gender indicator column (1 for 'F', 0 for 'M')
df['Gender'] = (df['M/F'] == 'F').astype(int)

# Drop the original 'M/F' column
df.drop(columns=['M/F'], inplace=True)

# Create bins for age
bins = [60, 70, 80, 90, 100]
labels = ['60-70', '70-80', '80-90', '90-100']

# New column 'Age Group'
df['Age Group'] = pd.cut(df['Age'], bins=bins, labels=labels, right=False)

# Filter out rows where 'Group' is 'Converted'
df = df[df['Group'] != 'Converted']

# Round the columns to three decimal places
df['nWBV'] = df['nWBV'].round(3)

df['ASF'] = df['ASF'].round(3)

df['SES'] = df['SES'].round(1)

df['CDR'] = df['CDR'].round(1)

# Extract numeric columns for standardization
numeric_columns = ['eTIV']

# Standardize numeric columns using Z-score Standardization
scaler = StandardScaler()
df[numeric_columns] = scaler.fit_transform(df[numeric_columns])

# Now print your DataFrame
print(df)

# Export the updated DataFrame to a new CSV file
df.to_csv(r"C:\Alzheimer's Prediction\data_alzheimer.csv", index=False)
