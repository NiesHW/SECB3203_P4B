import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
path = 'D:\\Python\\diabetes.csv'
df = pd.read_csv(path)

# Selecting features and target
features = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']
X = df[features]
y = df['Outcome']  # 'Outcome' is a classification target variable

# Splitting the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Random Forest Classifier
rf_model = RandomForestClassifier(random_state=42)
rf_model.fit(X_train, y_train)
y_pred_rf = rf_model.predict(X_test)
acc_rf = accuracy_score(y_test, y_pred_rf)
print(f"Random Forest Accuracy: {acc_rf}")
print(classification_report(y_test, y_pred_rf))

# Plot Confusion Matrix for Random Forest
plt.figure(figsize=(4, 3))
sns.heatmap(confusion_matrix(y_test, y_pred_rf), annot=True, fmt='d', cmap='Blues', cbar=False)
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix - Random Forest')
plt.show()

# SVM Classifier
svm_model = SVC()
svm_model.fit(X_train, y_train)
y_pred_svm = svm_model.predict(X_test)
acc_svm = accuracy_score(y_test, y_pred_svm)
print(f"SVM Accuracy: {acc_svm}")
print(classification_report(y_test, y_pred_svm))

# Plot Confusion Matrix for SVM
plt.figure(figsize=(4, 3))
sns.heatmap(confusion_matrix(y_test, y_pred_svm), annot=True, fmt='d', cmap='Blues', cbar=False)
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix - SVM')
plt.show()

# KNN Classifier
knn_model = KNeighborsClassifier()
knn_model.fit(X_train, y_train)
y_pred_knn = knn_model.predict(X_test)
acc_knn = accuracy_score(y_test, y_pred_knn)
print(f"KNN Accuracy: {acc_knn}")
print(classification_report(y_test, y_pred_knn))

# Plot Confusion Matrix for KNN
plt.figure(figsize=(4, 3))
sns.heatmap(confusion_matrix(y_test, y_pred_knn), annot=True, fmt='d', cmap='Blues', cbar=False)
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix - KNN')
plt.show()

# Assuming new_data contains the features for prediction
new_data = pd.DataFrame([
    [2, 120, 80, 30, 45, 30, 0.4, 50],
    [4, 160, 90, 35, 75, 35, 0.6, 60]
], columns=features)

# Predictions using Random Forest
rf_predictions = rf_model.predict(new_data)
print("Random Forest Predictions:")
print(rf_predictions)

# Predictions using SVM
svm_predictions = svm_model.predict(new_data)
print("SVM Predictions:")
print(svm_predictions)

# Predictions using KNN
knn_predictions = knn_model.predict(new_data)
print("KNN Predictions:")
print(knn_predictions)