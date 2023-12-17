<b>Descriptive statistic</b>

Descriptive statistics typically involve calculating various measures to describe the data's central tendency, 
variability, and distribution. By transposing the DataFrame using transpose(), 
you'll be able to see all columns with their respective statistics.

# Display basic statistics of the dataset
summary_statistics = df.describe().transpose()
print(summary_statistics)

![import1](https://drive.google.com/file/d/1s0eXihy7XYkpyhycCs0ABRMgPr9jJwSP/view?usp=sharing)


<b>Basic Grouping</b>

The basics of grouping in data analysis involve dividing a dataset into groups based on one or more categorical variables and performing operations independently on each group. So, since the objective is to compare the performance of the machine learning models (Gaussian Naïve Bayes and Logistic Regression) in terms of accuracy, precision, recall, and F1-score for heart attack detection we are grouping by the output(0= less chance of heart attack while 1= more chance of heart attack). This could help analyze the model's performance in distinguishing what factors led to getting a heart attack.

grouped_data = df.groupby(output).mean()
print(grouped_data)

![import1](https://drive.google.com/file/d/1_GZOPt2Xt_xP4Q39ed60dMlSv-bGz9_R/view?usp=drive_link)

So for further explanation, we can see the average age for a chance of getting a heart attack is 52.49 while the average age for not getting a heart attack is 56.60.

As our data is numerical and our objective is to compare Linear Regression and Gaussian Naïve Bayes, we will focus on using Pearson collection instead of the ANOVA test.

<b>Correlation Matrix with Numbers Heatmap</b>

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.show()

![import1](https://drive.google.com/file/d/19SCcqrUiqa--_AYHJtGb3iqPodI2EnaZ/view?usp=drive_link)

<b>Numeric Feature Analysis</b>

-> Bivariate data analysis with scatter plot

Pairplot allows us to plot pairwise relationships between variables within a dataset. This creates a nice visualization and helps us understand the data by summarizing a large amount of data in a single figure.

![import1](https://drive.google.com/file/d/1jGu-E_FwLAix8v6h5CyToCYUcYoPEQuO/view?usp=drive_link)

![import1](https://drive.google.com/file/d/1-hiXBTJJvSV09d3qoVGgVQGzo12vKYah/view?usp=drive_link)
![import1](https://drive.google.com/file/d/1QlC58xNsINn9taau0yj5TCwKYCZjtZcA/view?usp=drive_link)

The dataset shows the relationships between pairs of six numeric variables: age, trtbps (resting blood pressure), chol (cholestoral), thalachh (maximum heart rate achieved), oldpeak (ST segment depression), and output (the target variable, which is 0 for less chance of heart attack and 1 for more chance of heart attack).

Each row and column of the plot corresponds to one of the numeric variables. The diagonal plots in the middle of the chart are density plots (kde plots) that show the distribution of each variable. The off-diagonal plots are scatter plots that show the relationship between each pair of variables. The color of the points in the scatter plots corresponds to the target variable (output), with red indicating a higher chance of a heart attack and blue indicating a lower chance.

The observations from the pairplot are as follows:

-> Age vs. trtbps: There is a weak positive correlation, suggesting that as age increases, resting blood pressure tends to slightly increase as well.
-> Age vs. thalachh: There is a weak negative correlation, indicating that as age increases, maximum heart rate tends to slightly decrease.
-> trtbps vs. thalachh: There is a weak negative correlation, suggesting that individuals with higher resting blood pressure tend to have lower maximum heart rates.
-> thalachh vs. oldpeak: There is a weak positive correlation, indicating that individuals with higher maximum heart rates tend to have slightly higher ST segment depression.
-> chol vs. oldpeak: There is a weak positive correlation, suggesting that individuals with higher cholesterol tend to have slightly higher ST segment depression.

<b>Pearson Correlation</b>

The Pearson Correlation measures the linear dependence between two variables X and Y. The resulting coefficient is a value between -1 and 1 inclusive, where:

  -> 1: Total positive linear correlation.
  -> 0: No linear correlation, the two variables most likely do not affect each other.
  -> -1: Total negative linear correlation.

Pearson Correlation is the default method of the function "corr"

numeric_columns = df.select_dtypes(include=['float64', 'int64'])
correlation_matrix = numeric_colums.corr()
print(correlation_matrix)

![import1](https://drive.google.com/file/d/1JIisPHVklTAbST3g0UnVCbgW1y27Xzpg/view?usp=drive_link)

<b>P-value:</b>

The P-value is the probability value that the correlation between these two variables is statistically significant. Normally, we choose a significance level of 0.05, which means that we are 95% confident that the correlation between the variables is significant.

By convention, when 

-> the p-value is <0.001: we say there is strong evidence that the correlation is significant.
-> the p-value is < 0.05: there is moderate evidence that the correlation is significant.
-> the 0.05 < p-value is < 0.1: there is weak evidence that the correlation is significant.
-> the p-value is > 0.1: there is no evidence that the correlation is significant.

Here we compare the p-value of the output(classification of getting a heart attack) with other features

![import1](https://drive.google.com/file/d/1jdoKa1BrqkcuqNZ48L3O7fGgfWiQBqdj/view?usp=drive_link)
![import1](https://drive.google.com/file/d/1K1llWx7yX040HdpnxC2ocSUWQ3Fggm_G/view?usp=drive_link)

Result:

![import1](https://drive.google.com/file/d/1PqUI-JcznGnhAcck1dmiUho3H-9ZXVKI/view?usp=drive_link)

'age' and 'output':
-> Correlation: -0.2215 (moderate negative correlation)
-> P-value: 0.0001 (highly significant)

'sex' and 'output':
-> Correlation: -0.2836 (moderate negative correlation)
-> P-value: 5.4024e-07 (highly significant)

'cp' and 'output':
-> Correlation: 0.4321 (strong positive correlation)
-> P-value: 3.6274e-15 (highly significant)

'trtbs' and 'output':
-> Correlation: -0.1463 (weak negative correlation)
-> P-value: 0.0109 (significant)

'chol' and 'output':
-> Correlation: -0.0814 (weak negative correlation)
-> P-value: 0.1580 (not significant)

'fbs' and 'output':
-> Correlation: -0.0268 (very weak negative correlation)
-> P-value: 0.6424 (not significant)

'restecg' and 'output':
-> Correlation: 0.1349 (weak positive correlation)
-> P-value: 0.0190 (significant)

'thalachh' and 'output':
-> Correlation: 0.4200 (strong positive correlation)
-> P-value: 2.4761e-14 (highly significant)

'exng' and 'output':
-> Correlation: -0.4356 (strong negative correlation)
-> P-value: 2.0465e-15 (highly significant)

 'oldpeak' and 'output':
-> Correlation: -0.4291 (strong negative correlation)
-> P-value: 5.8146e-15 (highly significant)

'slp' and 'output':
-> Correlation: 0.3439 (moderate positive correlation)
-> P-value: 8.2214e-10 (highly significant)

'caa' and 'output':
-> Correlation: -0.4090 (strong negative correlation)
-> P-value: 1.3173e-13 (highly significant)

'thall' and 'output':
-> Correlation: -0.3431 (moderate negative correlation)
-> P-value: 9.0890e-10 (highly significant)

<b>Conclusion</b>

We now have a better idea of what our data looks like and which variables are important to take into account when predicting heart attack detection. We have narrowed it down to the following variables:

●     age
●     sex
●     cp
●     thalachh
●     exng
●     oldpeak
●     slp
●     caa
●     thall 

As we now move into building machine learning models to automate our analysis, feeding the model with variables that meaningfully affect our target variable will improve our model's prediction performance.
