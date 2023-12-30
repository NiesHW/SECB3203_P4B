<b>Progress 4: Model development</b>

<b>Flowchart:</b>

![import](https://drive.google.com/file/d/1CO4Wpzf333LI_DQ_-hLNwBwpaSAEQO0E/view?usp=drive_link)

<b>Logistic Regression</b>


We need to select the top features for model development.Here we imported the python libraries and update dataset which only remain columns that have p-value < 0.001(features relevant). Next,we separate the independent variable, from the dependent variable which is output column.

Then, split the data into train (70%) and test (30%). After that, scale the independent variable using Standard Scaler.This involves transforming the values of each feature so that they have a mean of 0 and a standard deviation of 1.

Then, we train and test data Logistic regression model using variables.Next, we use SelectKBest, which is feature selection method based on univariate statistics. SelectKBest selects the top k features based on a specified scoring function.The goal of using SelectKBest is to improve the performance of the logistic regression model by selecting the most informative features.

So based irrelevant features in update dataset, This is selected features (feature selection) by the machine learning.These selected features are considered the most informative based on the chi-squared statistical test. The model focuses on these features during training and testing, as they are deemed to have a stronger association with the target variable.

Training data:
Classification report of train set and accuracy score on the train set.


From the classification report, the variables reached an accuracy of 82%.This represents the ratio of correctly predicted instances to the total instances in the training set. It tells us that the model did a good job in discovering the heart attack on train data using Logistic Regression

Test data:

Classification report on test set.


The model achieved an accuracy of 85%.
When the accuracy on the test set is higher than the accuracy on the training set, it may indicate that the model is potentially underfitting to the training data. One possible explanation is that the model might not be complex enough to fully capture the intricacies of the training data, leading to underfitting. Underfitting occurs when the model is too simplistic, failing to grasp the nuances present in the training set. As a result, the model struggles to accurately represent the underlying patterns, and its performance on both the training and test sets may be suboptimal.


<b>Gaussian Naive Bayes</b>


We need to select the top features for model development.Here we imported the python libraries and update dataset which only remain columns that have p-value < 0.001(features relevant). Next,we separate the independent variable, from the dependent variable which is output column.

Then, split the data into train (70%) and test (30%). After that, scale the independent variable using Standard Scaler.This involves transforming the values of each feature so that they have a mean of 0 and a standard deviation of 1.


Then, we train and test data Gaussian Naive Bayes model using variables.Next, we use SelectKBest, which is feature selection method based on univariate statistics. SelectKBest selects the top k features based on a specified scoring function.The goal of using SelectKBest is to improve the performance of the logistic regression model by selecting the most informative features.


So based irrelevant features in update dataset, This is selected features (feature selection) by the machine learning.These selected features are considered the most informative based on the chi-squared statistical test. The model focuses on these features during training and testing, as they are deemed to have a stronger association with the target variable.

Train data:




Classification report and training set for Gaussian Naive Bayes. From the classification report, the variables reached an accuracy of 80%. Only 80% percentange for this model to detect the heart attack. 

Test data:


Classification report and testing set for Gaussian Naive Bayes.Both training and test accuracies are balanced, indicating a good fit.The model shows slightly better performance on Class 1 (presence of a heart disease) in terms of precision and recall.The F1-score considers both precision and recall and is a good balance metric.The model appears to generalize well to the test set, as the performance is consistent between training and test sets.
