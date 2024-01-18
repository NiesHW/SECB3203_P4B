import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

dataset=pd.read_csv("C:/Users/MY/Downloads/gastric_esophageal_cancer_data.csv")
dataset

print(dataset)

#Check for missing values
missing_values = dataset.isnull().sum()
print(missing_values)

#Visualize missing values
import seaborn as sns
import matplotlib.pyplot as plt

# Creating a sample DataFrame with missing values
df = pd.DataFrame(dataset)

# Create a heatmap to visualize missing values
sns.heatmap(df.isnull(), cbar=False, cmap='viridis')

# Display the plot
plt.show()


#----Handling missing values------

# Dropping missing values
# Drop rows with any missing values
df_cleaned = df.dropna()
print(df_cleaned)

# Check if there are still missing values
missing_values = df_cleaned.isnull().sum()
print(missing_values)


#------------------------------Data Formatting---------------------------------------
from sklearn.preprocessing import MinMaxScaler, StandardScaler

df_cleaned = df_cleaned.copy()  # Create a copy to avoid the SettingWithCopyWarning

# Min-Max Scaling
scaler = MinMaxScaler()
df_cleaned_copy = df_cleaned.copy()
df_cleaned.loc[:, 'BMI'] = scaler.fit_transform(df_cleaned[['BMI']])

print("Original 'BMI' column:")
print(df_cleaned_copy['BMI'])
print("Formatted 'BMI' column:")
print(df_cleaned['BMI'])

# Data Normalization

# Z-score Normalization
scaler = StandardScaler()
df_normalized = pd.DataFrame(scaler.fit_transform(df_cleaned), columns=df.columns)

print("Normalized DataFrame (Z-score Normalization):")
print(df_normalized)


#Binning Data
data = np.array(df_cleaned['Survival_Days'])

bin_edges = [0, 12, 24, 47, 93, 188, 375, 750, 1500, 3000]
bin_indices = np.digitize(data, bins=bin_edges)
bin_labels = ['<13 Days', '<25 Days', '<48 Days', '<94 Days', '<189 Days', '<376 Days', '<751 Days', '<1501 Days', '<3001 Days']

# Handle out-of-bounds indices
binned_column = np.array(bin_labels)[np.clip(bin_indices, 0, len(bin_labels) - 1)]

result_df = pd.DataFrame({'Survival_Days': data, 'Binned_Column': binned_column})
print(result_df)

dataset=pd.read_csv("C:/Users/MY/Downloads/gastric_esophageal_cancer_data.csv")
dataset

# Drop rows with any missing values
df_cleaned = dataset.dropna()

pd.set_option('display.max_columns', 50)
print(df_cleaned)

#---------------------Data analysis---------------------------

# Plateltes
data = {'Values': df_cleaned['Platelets .1']}
df = pd.DataFrame(data)
Platelets = 'Values'

# Calculate minimum, mode, and maximum
minimum_value = df[Platelets].min()
mode_value = df[Platelets].mode().values[0]  
maximum_value = df[Platelets].max()

print(f"Minimum value of Platelets: {minimum_value}")
print(f"Mode value of Platelets: {mode_value}")
print(f"Maximum value of Platelets: {maximum_value}")
print(f" ")

# WBC
data = {'Values': df_cleaned['WBC .1']}
df = pd.DataFrame(data)
WBC = 'Values'

# Calculate minimum, mode, and maximum
minimum_value = df[WBC].min()
mode_value = df[WBC].mode().values[0]  
maximum_value = df[WBC].max()

print(f"Minimum value of WBC: {minimum_value}")
print(f"Mode value of WBC: {mode_value}")
print(f"Maximum value of WBC: {maximum_value}")
print(f" ")

# Albumin
data = {'Values': df_cleaned['Albumin .1']}
df = pd.DataFrame(data)
Albumin = 'Values'

# Calculate minimum, mode, and maximum
minimum_value = df[Albumin].min()
mode_value = df[Albumin].mode().values[0]  
maximum_value = df[Albumin].max()

print(f"Minimum value of Albumin: {minimum_value}")
print(f"Mode value of Albumin: {mode_value}")
print(f"Maximum value of Albumin: {maximum_value}")
print(f" ")

# Creatinine
data = {'Values': df_cleaned['Creatinine .1']}
df = pd.DataFrame(data)
Creatinine = 'Values'

# Calculate minimum, mode, and maximum
minimum_value = df[Creatinine].min()
mode_value = df[Creatinine].mode().values[0]  
maximum_value = df[Creatinine].max()

print(f"Minimum value of Creatinine: {minimum_value}")
print(f"Mode value of Creatinine: {mode_value}")
print(f"Maximum value of Creatinine: {maximum_value}")
print(f" ")

# min, mode, max in table format
variables = ['Platelets', 'WBC', 'Albumin', 'Creatinine']

results_df = pd.DataFrame(columns=['Variable', 'Min', 'Mode', 'Max'])

for variable in variables:
    data = {'Values': df_cleaned[f'{variable} .1']}
    df = pd.DataFrame(data)

    minimum_value = df['Values'].min()
    mode_value = df['Values'].mode().values[0]
    maximum_value = df['Values'].max()

    # Check if results_df is empty
    if results_df.empty:
        results_df = pd.DataFrame({'Variable': [variable],
                                   'Min': [minimum_value],
                                   'Mode': [mode_value],
                                   'Max': [maximum_value]})
    else:
        results_df = pd.concat([results_df, pd.DataFrame({'Variable': [variable],
                                                          'Min': [minimum_value],
                                                          'Mode': [mode_value],
                                                          'Max': [maximum_value]})], ignore_index=True)
        
print(results_df)


# matrix

matrix_values = results_df[['Min', 'Mode', 'Max']].to_numpy()

print("Matrix:")
print(matrix_values)


#-------------------------Descriptive statistics----------------------------

# Plateltes
data = {'Values': df_cleaned['Platelets .1']}
df = pd.DataFrame(data)
Platelets = 'Values'

mean = df[Platelets].mean()
median = df[Platelets].median()  
std = df[Platelets].std()
skewness = df[Platelets].skew()
kurtosis = df[Platelets].kurt()

print(f"Mean of Platelets: {mean}")
print(f"Median of Platelets: {median}")
print(f"Standard Deviation of Platelets: {std}")
print(f"Skewness of Platelets: {skewness}")
print(f"Kurtosis of Platelets: {kurtosis}")
print(f" ")

# WBC
data = {'Values': df_cleaned['WBC .1']}
df = pd.DataFrame(data)
WBC = 'Values'

mean = df[WBC].mean()
median = df[WBC].median()  
std = df[WBC].std()
skewness = df[WBC].skew()
kurtosis = df[WBC].kurt()

print(f"Mean of WBC: {mean}")
print(f"Median of WBC: {median}")
print(f"Standard Deviation of WBC: {std}")
print(f"Skewness of WBC: {skewness}")
print(f"Kurtosis of WBC: {kurtosis}")
print(f" ")

# Albumin
data = {'Values': df_cleaned['Albumin .1']}
df = pd.DataFrame(data)
Albumin = 'Values'

mean = df[Albumin].mean()
median = df[Albumin].median()  
std = df[Albumin].std()
skewness = df[Albumin].skew()
kurtosis = df[Albumin].kurt()

print(f"Mean of Albumin: {mean}")
print(f"Median of Albumin: {median}")
print(f"Standard Deviation of Albumin: {std}")
print(f"Skewness of Albumin: {skewness}")
print(f"Kurtosis of Albumin: {kurtosis}")
print(f" ")

# Creatinine
data = {'Values': df_cleaned['Creatinine .1']}
df = pd.DataFrame(data)
Creatinine = 'Values'

mean = df[Creatinine].mean()
median = df[Creatinine].median()  
std = df[Creatinine].std()
skewness = df[Creatinine].skew()
kurtosis = df[Creatinine].kurt()

print(f"Mean of Creatinine: {mean}")
print(f"Median of Creatinine: {median}")
print(f"Standard Deviation of Creatinine: {std}")
print(f"Skewness of Creatinine: {skewness}")
print(f"Kurtosis of Creatinine: {kurtosis}")
print(f" ")

# mean, median, std, skewness and kurtosis in table format
variables = ['Platelets', 'WBC', 'Albumin', 'Creatinine']

results_df = pd.DataFrame(columns=['Variable', 'Mean', 'Median', 'Std', 'Skewness', 'Kurtosis'])

for variable in variables:
    data = {'Values': df_cleaned[f'{variable} .1']}
    df = pd.DataFrame(data)

    mean = df['Values'].mean()
    median = df['Values'].median()
    std = df['Values'].std()
    skewness = df['Values'].skew()
    kurtosis = df['Values'].kurt()

    # Check if results_df is empty
    if results_df.empty:
        results_df = pd.DataFrame({'Variable': [variable],
                                   'Mean': [mean],
                                   'Median': [median],
                                   'Standard Deviation': [std],
                                   'Skewness': [skewness],
                                   'Kurtosis': [kurtosis]})
    else:
        results_df = pd.concat([results_df, pd.DataFrame({'Variable': [variable],
                                                          'Mean': [mean],
                                                          'Median': [median],
                                                          'Standard Deviation': [std],
                                                          'Skewness': [skewness],
                                                          'Kurtosis': [kurtosis]})], ignore_index=True)
        
print(results_df)

#Import the necessary libraries for ANOVA and Correlation:
from scipy.stats import f_oneway
from scipy.stats import pearsonr

# ANOVA analysis
category_anova = 'BMI'  # actual categorical variable
grouped_data = []

for group_name, group_data in df_cleaned.groupby(category_anova):
    grouped_data.append(group_data['Survival_Days'].values) 

# Perform ANOVA
anova_result = f_oneway(*grouped_data)
print(f"ANOVA Result for {category_anova}: {anova_result}")


# Correlation analysis
variable1 = 'BMI'  
variable2 = 'Survival_Days'  

# Calculate Pearson correlation coefficient and p-value
correlation_coefficient, p_value = pearsonr(df_cleaned[variable1], df_cleaned[variable2])

print(f"Correlation coefficient between {variable1} and {variable2}: {correlation_coefficient}")
print(f"P-value: {p_value}")

# Interpret the correlation coefficient
if correlation_coefficient > 0:
    print("There is a positive correlation.")
elif correlation_coefficient < 0:
    print("There is a negative correlation.")
else:
    print("There is no correlation.")


#-------------------------------------Feature Selection--------------------------------------------
features_to_exclude = ['Stomach ', 'Survival_Days']
features_for_correlation = [col for col in df_cleaned.columns if col not in features_to_exclude]

print("Features for correlation analysis:", features_for_correlation)

# Calculate the correlation matrix
correlation_matrix = df_cleaned[features_for_correlation].corr()

# Plot the heatmap 
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Correlation Matrix')
plt.tight_layout()  
plt.show()

# Select features based on a correlation threshold
correlation_threshold = 0.6
highly_correlated_features = set()

for i in range(len(correlation_matrix.columns)):
    for j in range(i):
        if abs(correlation_matrix.iloc[i, j]) > correlation_threshold:
            colname = correlation_matrix.columns[i]
            highly_correlated_features.add(colname)

# Display highly correlated features
print(f"\nHighly correlated features with a threshold of {correlation_threshold}: {highly_correlated_features}")
selected_features = [col for col in df_cleaned.columns if col in highly_correlated_features]

# Display the selected features
print("\nSelected Features:")
print(selected_features)


#------------------------------Model Development----------------------------------------
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Assuming 'Survival_Days' is the original variable representing survival days
# Create a binary target variable 'Survival_Status'
df_cleaned['Survival_Status'] = (df_cleaned['Survival_Days'] > 365).astype(int)


# Remove trailing spaces from column names
df_cleaned.columns = df_cleaned.columns.str.strip()

# Select the features
features = df_cleaned[selected_features]


target = df_cleaned['Survival_Status']

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Assuming 'df_cleaned' is your cleaned DataFrame with features and target variable

# Separate independent variables (features) and dependent variable (target)
X = df_cleaned[selected_features]
y = df_cleaned['Survival_Status']

# Split the data into train (70%) and test (30%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Scale the independent variables using Standard Scaler
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Initialize a Random Forest Classifier
clf = RandomForestClassifier(random_state=42)

# Train the classifier
clf.fit(X_train, y_train)

# Make predictions on the test set
y_pred = clf.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
classification_report_result = classification_report(y_test, y_pred)

print(f"Accuracy: {accuracy}")
print("Classification Report:")
print(classification_report_result)

from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt


# Assuming 'y_train' contains the actual labels and 'y_pred' contains the predicted labels
y_train_pred = clf.predict(X_train)

# Generate confusion matrix
conf_matrix_train = confusion_matrix(y_train, y_train_pred)

# Plot the confusion matrix using seaborn heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix_train, annot=True, fmt='d', cmap='Blues', cbar=False,
            xticklabels=['Not Survived', 'Survived'], yticklabels=['Not Survived', 'Survived'])
plt.title('Confusion Matrix - Train Set')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()

from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

# Assuming 'y_test' contains the actual labels and 'y_pred' contains the predicted labels on the test set
y_test_pred = clf.predict(X_test)

# Generate confusion matrix
conf_matrix_test = confusion_matrix(y_test, y_test_pred)

# Plot the confusion matrix using seaborn heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix_test, annot=True, fmt='d', cmap='Blues', cbar=False,
            xticklabels=['Not Survived', 'Survived'], yticklabels=['Not Survived', 'Survived'])
plt.title('Confusion Matrix - Test Set')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()

from sklearn.metrics import classification_report

# Assuming 'y_test' contains the actual labels and 'y_pred' contains the predicted labels on the test set
y_pred = clf.predict(X_test)

# Generate classification report
classification_report_test = classification_report(y_test, y_pred)

# Print the classification report
print("Classification Report - Test Set:")
print(classification_report_test)




#---------------------------------Model Evaluation----------------------------------------
from sklearn.model_selection import cross_val_score

# Cross-validation scores
cross_val_scores = cross_val_score(clf, features, target, cv=5)
print(f"Cross-validation scores: {cross_val_scores}")
print(f"Mean Cross-validation score: {np.mean(cross_val_scores)}")


from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import StandardScaler

# Assuming 'df_cleaned' is your cleaned DataFrame with features and target variable

# Remove trailing spaces from column names
df_cleaned.columns = df_cleaned.columns.str.strip()

# Select the features
features = df_cleaned[selected_features]
target = df_cleaned['Survival_Status']

# Separate independent variables (features) and dependent variable (target)
X = features
y = target

# Split the data into train (80%) and test (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale the independent variables using Standard Scaler
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Initial Model
initial_rf_classifier = RandomForestClassifier(random_state=42)

# Train the initial model
initial_rf_classifier.fit(X_train_scaled, y_train)

# Make predictions on the test set
y_pred_initial = initial_rf_classifier.predict(X_test_scaled)

# Evaluate the initial model
accuracy_initial = accuracy_score(y_test, y_pred_initial)
classification_report_initial = classification_report(y_test, y_pred_initial)

print("Initial Model:")
print(f"Accuracy: {accuracy_initial}")
print("Classification Report:")
print(classification_report_initial)


# Grid Search for Hyperparameter Tuning
param_grid = {'n_estimators': [50, 100, 150],
              'max_depth': [None, 10, 20],
              'min_samples_split': [2, 5, 10],
              'min_samples_leaf': [1, 2, 4]}

grid_search = GridSearchCV(estimator=initial_rf_classifier, param_grid=param_grid, cv=5)
grid_search.fit(X_train_scaled, y_train)

# Display the best parameters
best_params = grid_search.best_params_
print(f"Best parameters: {best_params}")

# Use the best parameters from Grid Search to create the refined model
refined_rf_classifier = RandomForestClassifier(random_state=42, **best_params)

# Train the refined model
refined_rf_classifier.fit(X_train_scaled, y_train)

# Make predictions on the test set with the refined model
y_pred_refined = refined_rf_classifier.predict(X_test_scaled)

# Evaluate the refined model
accuracy_refined = accuracy_score(y_test, y_pred_refined)
classification_report_refined = classification_report(y_test, y_pred_refined)

print("Refined Model:")
print(f"Accuracy: {accuracy_refined}")
print("Classification Report:")
print(classification_report_refined)