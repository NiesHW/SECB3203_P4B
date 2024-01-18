import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Load the dataset
path = 'D:\\Python\\diabetes.csv'
df = pd.read_csv(path)

#Descriptive Statistic
descriptive_stats = df.describe().transpose()
print(descriptive_stats)

# Calculate correlation matrix excluding 'Outcome'
correlation_matrix_no_outcome = df.drop(columns='Outcome').corr()

# Create a heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix_no_outcome, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Matrix Heatmap (Excluding Outcome)')
plt.show()

