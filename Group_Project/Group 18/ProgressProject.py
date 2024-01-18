import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, accuracy_score

# Load the dataset
path = 'C:\\Python Programs\\diabetes.csv'
df = pd.read_csv(path)

# Select the specified features
features = ['Pregnancies', 'SkinThickness', 'Insulin', 'BMI', 'Age']
X = df[features]
y = df['Outcome']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Random Forest with grid search
param_grid_rf = {
    'n_estimators': [50, 100, 200],
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 5, 10]
}

grid_search_rf = GridSearchCV(RandomForestClassifier(random_state=42), param_grid_rf, cv=5, scoring='accuracy')
grid_search_rf.fit(X_train, y_train)

# Best hyperparameters for Random Forest
best_params_rf = grid_search_rf.best_params_

# SVM with grid search
param_grid_svm = {
    'C': [0.1, 1, 10],
    'kernel': ['linear', 'rbf']
}

grid_search_svm = GridSearchCV(SVC(probability=True, random_state=42), param_grid_svm, cv=5, scoring='accuracy')
grid_search_svm.fit(X_train, y_train)

# Best hyperparameters for SVM
best_params_svm = grid_search_svm.best_params_

# KNN with grid search
param_grid_knn = {
    'n_neighbors': [3, 5, 7],
    'weights': ['uniform', 'distance']
}

grid_search_knn = GridSearchCV(KNeighborsClassifier(), param_grid_knn, cv=5, scoring='accuracy')
grid_search_knn.fit(X_train, y_train)

# Best hyperparameters for KNN
best_params_knn = grid_search_knn.best_params_

# Random Forest model with best hyperparameters
rf_model = RandomForestClassifier(random_state=42, **best_params_rf)
rf_model.fit(X_train, y_train)

# Predictions on the test set for Random Forest
y_pred_rf = rf_model.predict(X_test)

# Evaluate the Random Forest model
print("Random Forest Metrics:")
print(classification_report(y_test, y_pred_rf))
accuracy_rf = accuracy_score(y_test, y_pred_rf)
print(f"Accuracy: {accuracy_rf}")

# Define the parameter grid for SVM
param_grid_svm = {
    'C': [0.1, 1, 10],
    'kernel': ['linear', 'rbf']
}

# Perform grid search for SVM
grid_search_svm = GridSearchCV(SVC(probability=True, random_state=42), param_grid_svm, cv=5, scoring='accuracy')
grid_search_svm.fit(X_train, y_train)

# Best hyperparameters for SVM
best_params_svm = grid_search_svm.best_params_

# SVM model with best hyperparameters
svm_model = SVC(probability=True, **best_params_svm)
svm_model.fit(X_train, y_train)

# Predictions on the test set for SVM
y_pred_svm = svm_model.predict(X_test)

# Evaluate the SVM model
print("\nSVM Metrics:")
print(classification_report(y_test, y_pred_svm))
accuracy_svm = accuracy_score(y_test, y_pred_svm)
print(f"Accuracy: {accuracy_svm}")

# Define the parameter grid for KNN
param_grid_knn = {
    'n_neighbors': [3, 5, 7],
    'weights': ['uniform', 'distance']
}

# Perform grid search for KNN
grid_search_knn = GridSearchCV(KNeighborsClassifier(), param_grid_knn, cv=5, scoring='accuracy')
grid_search_knn.fit(X_train, y_train)

# Best hyperparameters for KNN
best_params_knn = grid_search_knn.best_params_

# KNN model with best hyperparameters
knn_model = KNeighborsClassifier(**best_params_knn)
knn_model.fit(X_train, y_train)

# Predictions on the test set for KNN
y_pred_knn = knn_model.predict(X_test)

# Evaluate the KNN model
print("\nKNN Metrics:")
print(classification_report(y_test, y_pred_knn))
accuracy_knn = accuracy_score(y_test, y_pred_knn)
print(f"Accuracy: {accuracy_knn}")

# Compare accuracies
accuracies = {'Random Forest': accuracy_rf, 'SVM': accuracy_svm, 'KNN': accuracy_knn}
best_model = max(accuracies, key=accuracies.get)
print(f"\nBest Model: {best_model} with Accuracy: {accuracies[best_model]}")
