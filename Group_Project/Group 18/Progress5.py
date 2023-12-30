import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_score, validation_curve, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier

# Load dataset
path = 'D:\\Python\\diabetes.csv'
df = pd.read_csv(path)

# Selecting features and target
features = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']
X = df[features]
y = df['Outcome']  # Assuming 'Outcome' is a classification target variable

# Splitting the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Random Forest Classifier
rf_model = RandomForestClassifier(random_state=42)

# Perform cross-validation
cv_scores_rf = cross_val_score(rf_model, X, y, cv=5)  # 5-fold cross-validation
print("Cross-Validation Scores - Random Forest:")
print(cv_scores_rf)
print(f"Mean CV Score - Random Forest: {cv_scores_rf.mean()}")

# Validation Curve for Random Forest (n_estimators)
param_range = [10, 50, 100, 150]  # Example parameter values for n_estimators
train_scores, test_scores = validation_curve(
    RandomForestClassifier(random_state=42), X, y, param_name="n_estimators",
    param_range=param_range, cv=5, scoring="accuracy", n_jobs=-1
)

# Plotting
plt.figure(figsize=(8, 6))
plt.title("Validation Curve - Random Forest")
plt.xlabel("n_estimators")
plt.ylabel("Accuracy")
plt.plot(param_range, np.mean(train_scores, axis=1), label="Training Score", color="blue")
plt.plot(param_range, np.mean(test_scores, axis=1), label="Cross-validation Score", color="red")
plt.legend()
plt.show()

# Grid Search for Random Forest
param_grid_rf = {'n_estimators': [50, 100, 150], 'max_depth': [None, 10, 20]}
grid_search_rf = GridSearchCV(RandomForestClassifier(random_state=42), param_grid_rf, cv=5)
grid_search_rf.fit(X, y)

print("Best Parameters (Random Forest):", grid_search_rf.best_params_)

# SVM Classifier
svm_model = SVC(random_state=42)

# Perform cross-validation for SVM
cv_scores_svm = cross_val_score(svm_model, X, y, cv=5)  # 5-fold cross-validation
print("Cross-Validation Scores - SVM:")
print(cv_scores_svm)
print(f"Mean CV Score - SVM: {cv_scores_svm.mean()}")

# Validation Curve for SVM (C parameter)
param_range_svm = [0.1, 1, 10, 100]  # Example parameter values for C
train_scores_svm, test_scores_svm = validation_curve(
    SVC(random_state=42), X, y, param_name="C",
    param_range=param_range_svm, cv=5, scoring="accuracy", n_jobs=-1
)

# Plotting Validation Curve for SVM
plt.figure(figsize=(8, 6))
plt.title("Validation Curve - SVM")
plt.xlabel("C parameter")
plt.ylabel("Accuracy")
plt.semilogx(param_range_svm, np.mean(train_scores_svm, axis=1), label="Training Score", color="blue")
plt.semilogx(param_range_svm, np.mean(test_scores_svm, axis=1), label="Cross-validation Score", color="red")
plt.legend()
plt.show()

# Grid Search for SVM
param_grid_svm = {'C': [0.1, 1, 10, 100], 'gamma': [1, 0.1, 0.01, 0.001], 'kernel': ['rbf', 'linear']}
grid_search_svm = GridSearchCV(SVC(), param_grid_svm, cv=5)
grid_search_svm.fit(X, y)

print("Best Parameters (SVM):", grid_search_svm.best_params_)

# KNN Classifier
knn_model = KNeighborsClassifier()

# Perform cross-validation for KNN
cv_scores_knn = cross_val_score(knn_model, X, y, cv=5)  # 5-fold cross-validation
print("Cross-Validation Scores - KNN:")
print(cv_scores_knn)
print(f"Mean CV Score - KNN: {cv_scores_knn.mean()}")

# Validation Curve for KNN (n_neighbors parameter)
param_range_knn = np.arange(1, 20)  # Example parameter values for n_neighbors
train_scores_knn, test_scores_knn = validation_curve(
    KNeighborsClassifier(), X, y, param_name="n_neighbors",
    param_range=param_range_knn, cv=5, scoring="accuracy", n_jobs=-1
)

# Plotting Validation Curve for KNN
plt.figure(figsize=(8, 6))
plt.title("Validation Curve - KNN")
plt.xlabel("n_neighbors")
plt.ylabel("Accuracy")
plt.plot(param_range_knn, np.mean(train_scores_knn, axis=1), label="Training Score", color="blue")
plt.plot(param_range_knn, np.mean(test_scores_knn, axis=1), label="Cross-validation Score", color="red")
plt.legend()
plt.show()

# Grid Search for KNN
param_grid_knn = {'n_neighbors': np.arange(1, 20)}
grid_search_knn = GridSearchCV(KNeighborsClassifier(), param_grid_knn, cv=5)
grid_search_knn.fit(X, y)

print("Best Parameters (KNN):", grid_search_knn.best_params_)

