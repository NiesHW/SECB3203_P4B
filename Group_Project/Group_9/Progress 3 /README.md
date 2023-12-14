# Project Progress: Phase 3

## 4.0 Analysis of Variance (ANOVA)

In this phase of our project, we are actively engaged in conducting an Analysis of Variance (ANOVA) to explore potential differences among groups for our carefully selected variables. ANOVA, a robust statistical technique, allows us to discern whether there are significant variations in means across multiple groups. This analysis is instrumental in uncovering insights that contribute to the refinement of our Alzheimer's disease prediction model.

## 4.1 Selected Variables

We have carefully chosen specific variables that are deemed relevant to our Alzheimer's disease prediction study. These variables include Group(Demented/Non-Demented), Mini-Mental State Examination (MMSE), Normalize Whole Brain Volume (nWBV), Estimated Total Intracranial Volume (eTIV), Atlas Scaling Factor (ASF) and Clinical Dementia Rating (CDR). The selected variable serves a distinct purpose in contributing to our understanding of cognitive health and its potential relationship with Alzheimer's disease.

## 4.2 Rationale for ANOVA

ANOVA is a useful tool for our thorough investigation of Alzheimer's disease prediction since it is especially effective at evaluating mean differences across several groups. In this instance, ANOVA helps to provide a more complex understanding of the differences between individuals classified as Demented and Non-Demented in several important variables, such as MMSE scores, Estimated Total Intracranial Volume (eTIV), Clinical Dementia Rating (CDR), Atlas Scaling Factor (ASF), and Normalise Whole Brain Volume (nWBV).

Our goal is to determine whether the means of the defined groups differ statistically significantly by using ANOVA on these various factors. The ANOVA results indicate significant differences that may be important in differentiating between different states of cognitive health and offer important insights into potential predictors of Alzheimer's disease.

## 4.3 Applying ANOVA

We are utilizing the scipy.stats library in Python to perform the ANOVA tests. The one-way ANOVA will allow us to examine the differences in means among the groups for each variable independently. 

```python
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



