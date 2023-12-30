<b>Progress 4: Model development</b>

<b>Flowchart:</b>

![Image](https://drive.google.com/uc?id=1CO4Wpzf333LI_DQ_-hLNwBwpaSAEQO0E)


<b>Logistic Regression</b>

![ImageA](https://drive.google.com/uc?id=15YJ5xi6xVvseDoQXOUL9RIExNaTWQIhU)

We need to select the top features for model development.Here we imported the python libraries and update dataset which only remain columns that have p-value < 0.001(features relevant). Next,we separate the independent variable, from the dependent variable which is output column.

![ImageB](https://drive.google.com/uc?id=1O4stvtLgDUsVKjZ3aa4VOBhZQ_ERFB89)

Then, split the data into train (70%) and test (30%). After that, scale the independent variable using Standard Scaler.This involves transforming the values of each feature so that they have a mean of 0 and a standard deviation of 1.

![ImageC](https://drive.google.com/uc?id=15Nqjszwy55Xfe38bJHZGByCSISsfLDYO)

Then, we train and test data Logistic regression model using variables.Next, we use SelectKBest, which is feature selection method based on univariate statistics. SelectKBest selects the top k features based on a specified scoring function.The goal of using SelectKBest is to improve the performance of the logistic regression model by selecting the most informative features.

![ImageD](https://drive.google.com/uc?id=1y_oO-MjBSFr7Hz1bZbSvGtul31yYsGzE)

So based irrelevant features in update dataset, This is selected features (feature selection) by the machine learning.These selected features are considered the most informative based on the chi-squared statistical test. The model focuses on these features during training and testing, as they are deemed to have a stronger association with the target variable.

Training data:

![ImageE](https://drive.google.com/uc?id=1GWZf3P2eqRVzlQ-vRQEMGgHCNu_jJNdF)

Classification report of train set and accuracy score on the train set.

![ImageF](https://drive.google.com/uc?id=1C4j4C7BveS5a1mAUpLlx3YTaY2C4dhJ5)

From the classification report, the variables reached an accuracy of 82%.This represents the ratio of correctly predicted instances to the total instances in the training set. It tells us that the model did a good job in discovering the heart attack on train data using Logistic Regression

Test data:

![ImageG](https://drive.google.com/uc?id=1VI9MF3V4K7iMq9I7yI9avYu7zehRWno3)

Classification report on test set.

![ImageH](https://drive.google.com/uc?id=1lB1BK6s_5zU1iNWEiifS1zJuVxmOQKNU)

The model achieved an accuracy of 85%.
When the accuracy on the test set is higher than the accuracy on the training set, it may indicate that the model is potentially underfitting to the training data. One possible explanation is that the model might not be complex enough to fully capture the intricacies of the training data, leading to underfitting. Underfitting occurs when the model is too simplistic, failing to grasp the nuances present in the training set. As a result, the model struggles to accurately represent the underlying patterns, and its performance on both the training and test sets may be suboptimal.


<b>Gaussian Naive Bayes</b>

![ImageI](https://drive.google.com/uc?id=1FN7I2oUyqpQGe_jRs6fKy4Vl1yWbaeBa)

We need to select the top features for model development.Here we imported the python libraries and update dataset which only remain columns that have p-value < 0.001(features relevant). Next,we separate the independent variable, from the dependent variable which is output column.

![ImageJ](https://drive.google.com/uc?id=1RJrdutbsNWUcivhbsJDJ0FdiSZDcxhdA)

Then, split the data into train (70%) and test (30%). After that, scale the independent variable using Standard Scaler.This involves transforming the values of each feature so that they have a mean of 0 and a standard deviation of 1.

![ImageK](https://drive.google.com/uc?id=1Fo21ew-qc3RpqrrTMN_PQEswCvaJHHZn)

Then, we train and test data Gaussian Naive Bayes model using variables.Next, we use SelectKBest, which is feature selection method based on univariate statistics. SelectKBest selects the top k features based on a specified scoring function.The goal of using SelectKBest is to improve the performance of the logistic regression model by selecting the most informative features.

![ImageL](https://drive.google.com/uc?id=1RinJa-MtDp5j-azxGe_DWmzweVnIC6fe)

So based irrelevant features in update dataset, This is selected features (feature selection) by the machine learning.These selected features are considered the most informative based on the chi-squared statistical test. The model focuses on these features during training and testing, as they are deemed to have a stronger association with the target variable.

Train data:

![ImageM](https://drive.google.com/uc?id=1IKw6vRxyel5zNnJnx0c95WwLaT0PIWbJ)

![ImageN](https://drive.google.com/uc?id=1U34pg4pJZThR4aIHRPJ1ZOy-50X6rUrV)

Classification report and training set for Gaussian Naive Bayes. From the classification report, the variables reached an accuracy of 80%. Only 80% percentange for this model to detect the heart attack. 

Test data:

![ImageO](https://drive.google.com/uc?id=1c7OGQnd0j9Gp-KunlrPuZ-ljRZuccH2A)

![ImageP](https://drive.google.com/uc?id=1ow2ImZ4ETwdrSYh0z273JuGJWfQCKh7G)

Classification report and testing set for Gaussian Naive Bayes.Both training and test accuracies are balanced, indicating a good fit.The model shows slightly better performance on Class 1 (presence of a heart disease) in terms of precision and recall.The F1-score considers both precision and recall and is a good balance metric.The model appears to generalize well to the test set, as the performance is consistent between training and test sets.
