
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt
import pandas as pd

# Load dataset
path = 'C:\\Python Programs\\diabetes.csv'
df = pd.read_csv(path)

# Selecting features and target
features = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']
X = df[features]
y = df['Outcome']  # Assuming 'Outcome' is a classification target variable

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

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
