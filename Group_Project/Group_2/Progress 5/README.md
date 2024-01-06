<b>Model: Logistic Regression</b>

<b>Training Set:</b>

#Calculate accuracy score on the training set
accuracy_train = accuracy_score(y_train, y_train_pred)
print(f"Accuracy Score on Training Set: {accuracy_train:.2f}")

#Generate confusion matrix for training set
cm_train = confusion_matrix(y_train, y_train_pred)
print("Confusion Matrix on Training Set:\n", cm_train)

#Generate classification report for the training set
report_train = classification_report(y_train, y_train_pred)
print("Classification Report on Training Set:\n", report_train)

#Visualize confusion matrices
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
sns.heatmap(cm_train, annot=True, fmt="d", cmap="Blues", cbar=False, ax=axes[0])
axes[0].set_title('Confusion Matrix (Training Set)')
axes[0].set_xlabel('Predicted')
axes[0].set_ylabel('Actual')

![import1](https://drive.google.com/uc?id=1muZb56sj8M8nahIV25U_ySLWR6AEUXVC)

![import1](https://drive.google.com/uc?id=1_UpP0OW42U_ZysEIAF9kIsQcOawF3Cb4)

![import1](https://drive.google.com/uc?id=13h5HYPpEylyLeeg1NWcGHJZGJqHRgG8V)


<b>Test Set:</b>

#Calculate accuracy score on the test set
accuracy_test = accuracy_score(y_test, y_test_pred)
print(f"\nAccuracy Score on Test Set: {accuracy_test:.2f}")

#Generate confusion matrix for test set
cm_test = confusion_matrix(y_test, y_test_pred)
print("Confusion Matrix on Test Set:\n", cm_test)

#Generate classification report for the test set
report_test = classification_report(y_test, y_test_pred)
print("Classification Report on Test Set:\n", report_test)

#Visualize confusion matrices
sns.heatmap(cm_test, annot=True, fmt="d", cmap="Blues", cbar=False, ax=axes[1])
axes[1].set_title('Confusion Matrix (Test Set)')
axes[1].set_xlabel('Predicted')
axes[1].set_ylabel('Actual')

![import1](https://drive.google.com/uc?id=1w7MU55fOXMYw9-60tJdI6UZknUmHh3A6)

![import1](https://drive.google.com/uc?id=12NBvipS7LSJoOfpqmZbEQdpUv3kRyOPx)

![import1](https://drive.google.com/uc?id=12vy6Edlc0NlThjKS-r0z7FKqHlxdGlVf)


<b>Model: Gaussian Naive Bayes</b>

<b>Training Set</b>

#Calculate accuracy score on the test set
accuracy_test = accuracy_score(y_test, y_test_pred)
print(f"\nAccuracy Score on Test Set: {accuracy_test:.2f}")

#Confusion matrix
from sklearn.metrics import confusion_matrix  
cm = confusion_matrix(y_test, y_test_pred) 
print(cm)

mtp.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='g', cmap='Greens', cbar=False,
            xticklabels=['0', '1'],
            yticklabels=['0', '1'])
mtp.title('Confusion Matrix (Test Set)')
mtp.xlabel('Predicted')
mtp.ylabel('Actual')
mtp.show()

#Generate classification report for the test set
report_test = classification_report(y_test, y_test_pred)
print("Classification Report on Test Set:\n", report_test)

#Generate classification report for the test set
report_test = classification_report(y_test, y_test_pred, output_dict=True)

#Extract metrics from the classification report
metrics = report_test['weighted avg']
precision = metrics['precision']
recall = metrics['recall']
f1_score = metrics['f1-score']

#Plotting the metrics on a bar graph
labels = ['Accuracy', 'Precision', 'Recall', 'F1-Score']
values = [accuracy_test, precision, recall, f1_score]

mtp.figure(figsize=(8, 6))
sns.barplot(x=labels, y=values, palette='viridis')
mtp.title('Model Metrics (Testing)')
mtp.xlabel('Metric Value')
mtp.show()

![import1](https://drive.google.com/uc?id=13395Umd5Nihfs15K9hpeV4tuZn3mP12A)

![import1](https://drive.google.com/uc?id=1mf_nH0YJ8ujQJKFELpM2siJuzivspg9e)

![import1](https://drive.google.com/uc?id=1PCDxnSAhN2KkdbMJYuB6hyHW9CcYEs0c)


<b>Testing:</b>

#Calculate accuracy score on the training set
accuracy_train = accuracy_score(y_train, y_train_pred)
print(f"Accuracy Score on Training Set: {accuracy_train:.2f}")

#Confusion matrix
from sklearn.metrics import confusion_matrix  
cm_train = confusion_matrix(y_train, y_train_pred) 
print(cm_train)

mtp.figure(figsize=(8, 6))
sns.heatmap(cm_train, annot=True, fmt='g', cmap='Greens', cbar=False,
            xticklabels=['0', '1'],
            yticklabels=['0', '1'])
mtp.title('Confusion Matrix (Training Set)')
mtp.xlabel('Predicted')
mtp.ylabel('Actual')
mtp.show()

#Generate classification report for the training set
report_train = classification_report(y_train, y_train_pred)
print("Classification Report on Training Set:\n", report_train)

#Generate classification report for the test set
report_test = classification_report(y_train, y_train_pred, output_dict=True)

#Extract metrics from the classification report
metrics = report_test['weighted avg']
precision = metrics['precision']
recall = metrics['recall']
f1_score = metrics['f1-score']

#Plotting the metrics on a bar graph
labels = ['Accuracy', 'Precision', 'Recall', 'F1-Score']
values = [accuracy_train, precision, recall, f1_score]

mtp.figure(figsize=(8, 6))
sns.barplot(x=labels, y=values, palette='viridis')
mtp.title('Model Metrics (Training)')
mtp.xlabel('Metric Value')
mtp.show()

![import1](https://drive.google.com/uc?id=1u1I7gvosKDCVNfJkMXSqcCZOkfLhmiqD)

![import1](https://drive.google.com/uc?id=1SVC73bw-WQ90NoAgQW2oOSq1lMr7fkkL)

![import1](https://drive.google.com/uc?id=1tc0fVrJxsIYO3AAH1ZmDQTK9g0BePLHS)


Based on the test set of Logistic Regression and Gaussian Naive Bayes, both achieve the accuracy scores of 82%. The overall accuracy of 
both models shows the same value, thus both are capable of classifying heart attack cases. The error rate for both models shows the 
same, 18% indicating room for improvement but not a significant performance gap. However, there are several factors to consider.
The confusion matrix shows that the Logistic Regression had more false positives (8) compared to Gaussian Naive Bayes (11), potentially 
leading to unnecessary interventions. Conversely, Gaussian Naive Bayes had more false negatives (11) which could miss critical cases.
Gaussian Naive Bayes shows slightly better recall for the "heart attack" class (0.88) compared to Logistic Regression (0.84), meaning it 
identifies a higher proportion of true heart attacks. On the other hand, Logistic Regression exhibits slightly higher precision for both 
classes (0.81 and 0.84) compared to Gaussian Naive Bayes (0.77 and 0.88), indicating a lower rate of false positives. Since the accuracy 
of both training and testing sets is the same for Logistic Regression, it shows that the model is optimal whereas the accuracy of the 
testing set shows more than the training set in Gaussian Naive Bayes. 

In conclusion, Logistic Regression is considered the best algorithm for analyzing heart attack detection because it will avoid 
unnecessary interventions due to false positives in terms of errors. Logistic Regression is robust to irrelevant features and handles
non-linear relationships to some extent. Gaussian Naive Bayes assumes feature independence and normality of data, which might not
always hold true for medical data. Logistic Regression provides coefficients that offer insights into the features' relative importance
in predicting heart attacks. Gaussian Naive Bayes is less interpretable and might be a "black box" model.  
