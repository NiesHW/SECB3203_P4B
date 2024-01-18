import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor



# Load dataset
path = 'C:\\Python Programs\\diabetes.csv'
df = pd.read_csv(path)

# Selecting features and target
features = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']
X = df[features]
y = df['Outcome']  # Assuming 'Outcome' is a classification target variable

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model Fitting: Fit KNN with varying neighbor values (n_neighbors)
neighbor_values = [1, 3, 5, 7, 10, 15, 20]  # Different neighbor values for KNN
train_scores = []
test_scores = []

for n in neighbor_values:
    knn = KNeighborsRegressor(n_neighbors=n)
    knn.fit(X_train, y_train)
    
    # Evaluate on training set
    train_score = knn.score(X_train, y_train)
    train_scores.append(train_score)
    
    # Evaluate on test set
    test_score = knn.score(X_test, y_test)
    test_scores.append(test_score)

# Plotting
plt.figure(figsize=(8, 6))
plt.plot(neighbor_values, train_scores, label='Training Score', marker='o')
plt.plot(neighbor_values, test_scores, label='Test Score', marker='o')
plt.xlabel('Number of Neighbors (n_neighbors)')
plt.ylabel('Score')
plt.title('Overfitting/Underfitting for KNN')
plt.legend()
plt.show()


# Model Fitting: Fit SVM with varying C values
C_values = [0.001, 0.01, 0.1, 1, 10, 100]  # Different C values for SVM
train_scores = []
test_scores = []

for c in C_values:
    svm = SVR(kernel='linear', C=c)
    svm.fit(X_train, y_train)
    
    # Evaluate on training set
    train_score = svm.score(X_train, y_train)
    train_scores.append(train_score)
    
    # Evaluate on test set
    test_score = svm.score(X_test, y_test)
    test_scores.append(test_score)

# Plotting
plt.figure(figsize=(8, 6))
plt.plot(np.log10(C_values), train_scores, label='Training Score', marker='o')
plt.plot(np.log10(C_values), test_scores, label='Test Score', marker='o')
plt.xlabel('log10(C)')
plt.ylabel('Score')
plt.title('Overfitting/Underfitting for SVM')
plt.legend()
plt.show()

# Model Fitting: Fit Random Forest with varying n_estimators
n_estimators_values = [10, 50, 100, 150, 200]  # Different n_estimators values for Random Forest
train_scores = []
test_scores = []

for n in n_estimators_values:
    rf = RandomForestRegressor(n_estimators=n, random_state=42)
    rf.fit(X_train, y_train)
    
    # Evaluate on training set
    train_score = rf.score(X_train, y_train)
    train_scores.append(train_score)
    
    # Evaluate on test set
    test_score = rf.score(X_test, y_test)
    test_scores.append(test_score)

# Plotting
plt.figure(figsize=(8, 6))
plt.plot(n_estimators_values, train_scores, label='Training Score', marker='o')
plt.plot(n_estimators_values, test_scores, label='Test Score', marker='o')
plt.xlabel('Number of Estimators (n_estimators)')
plt.ylabel('Score')
plt.title('Overfitting/Underfitting for Random Forest')
plt.legend()
plt.show()