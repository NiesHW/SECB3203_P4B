import pandas as pd

# Replace 'your_dataset.csv' with the actual file path of your CSV dataset
file_path_1 = r'C:\SECB3203 PROJECT\oasis_longitudinal.csv'

file_path_2 = r'C:\SECB3203 PROJECT\alzheimer_dataset.csv'


# Read the CSV file into a DataFrame
df_1 = pd.read_csv(file_path_1)
df_2 = pd.read_csv(file_path_2)

selected_variables = ['EDUC', 'SES', 'MMSE', 'CDR', 'eTIV', 'nWBV', 'ASF']

selected_df_1 = df_1[selected_variables]
selected_df_2 = df_2[selected_variables]

# Display the maximum, mean, and median for each variable
summary_stats_1 = selected_df_1.agg(['max', 'mean', 'median']).transpose()
print(summary_stats_1)

summary_stats_2 = selected_df_2.agg(['max', 'mean', 'median']).transpose()
print(summary_stats_2)
