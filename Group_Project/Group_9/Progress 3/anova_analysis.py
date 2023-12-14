import pandas as pd
from scipy.stats import f_oneway

# Read data_alzheimer.csv
df = pd.read_csv(r"C:\Alzheimer's Prediction\data_alzheimer.csv")

# Variables of interest
variables_of_interest = ['MMSE', 'nWBV', 'eTIV', 'ASF', 'CDR']
groups = df['Group'].unique()

# Create dictionaries to store scores for each variable and group
variable_by_group = {variable: {group: df[df['Group'] == group][variable] for group in groups} for variable in variables_of_interest}

# Perform one-way ANOVA for CDR
CDR_statistic, CDR_p_value = f_oneway(*variable_by_group['CDR'].values())

# Print the results for CDR
print("ANOVA Statistic for CDR:", CDR_statistic)
print("P-value for CDR:", CDR_p_value)

# Check significance for CDR
alpha = 0.05
if CDR_p_value < alpha:
    print("Reject the null hypothesis. There are significant differences in CDR between group means.")
else:
    print("Fail to reject the null hypothesis. There is not enough evidence to suggest significant differences in CDR.")

# Repeat the process for other variables 

