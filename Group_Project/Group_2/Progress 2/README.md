The dataset employed in this project, denoted as "heart.csv," is sourced from the Kaggle dataset titled "Heart Attack Analysis & Prediction Dataset." This comprehensive dataset comprises a total of 303 instances, each characterized by 14 distinct attributes.

Importing Dataset:

In the realm of data science, the initial step often involves acquiring and importing datasets for analysis. The dataset at the center of our exploration is "heart.csv," sourced from Kaggle's "Heart Attack Analysis & Prediction Dataset." The importation of this dataset into Python lays the foundation for subsequent analysis and model development.


Initially, we utilized the Pandas library for data cleaning and preprocessing. We proceed to load the "heart.csv" dataset by specifying its file path and assigning it to a DataFrame, which we label as df. Finally, we print df.head(20) to showcase the first 20 rows of the DataFrame derived from the "heart.csv" dataset.

According to the figure above, a representation is provided, illustrating 20 rows of the DataFrame extracted from the "heart.csv" file. This Data Frame encompasses 14 columns of data.

print(df.head()): This command prints the first few rows of the DataFrame, typically the top 5 rows by default. It is useful for a quick glance at the dataset.
print(df.info()): This command provides a concise summary of the DataFrame df. It includes information about the data types of each column, the number of non-null values, and the memory usage. It's helpful for understanding the overall structure of the Data Frame
.print(df.describe()): This command generates descriptive statistics of the DataFrame df. It includes measure like count, mean, standard deviation, minimum, 25th percentile, median (50th percentile), 75th percentile, and maximum. It provides insights into the central tendency and spread of the numerical columns in the dataset.

Here, we can understand the data size where it contains 8 rows and 14 column


Data wrangling, using tools: Pandas and Numpy:

Identifying and handling missing values

Handling missing values is a crucial step in data analysis and machine learning because it directly impacts the accuracy and reliability of our results. When data contains gaps or missing information, it can introduce inaccuracies and biases into our analyses, leading to flawed conclusions.To check if our dataset contains null values or not, the syntax is:

print(df.isnull())


The statement " false" indicates that, upon checking each element in the dataset, none of them are identified as null or missing values. In the context of the dataset dimensions [303 rows x 14 columns], it means that across all 303 rows and 14 columns, there are no instances where data is absent or undefined. This is a positive outcome because it implies that our dataset is complete, and we have values for each attribute in every row, making it ready for further analysis without the need to address missing data. It's a reassuring sign of data integrity and completeness in this particular dataset.



By using the syntax print(df.isnull().sum), we performed a more detailed check on each column individually. The result, where each column shows a count of 0, reinforces our earlier finding that there are no null values present in the dataset. This column-wise examination is crucial because it allows us to pinpoint if there are any specific attributes or features that might have missing values.





After checking null values, we checked for duplicate values (duplicate_rows = df[df.duplicate()) in our dataset because duplicate entries can lead to skewed results, affecting the reliability of statistical analyses and machine learning models. When there are duplicate rows, it might give undue weight to certain observations, leading to biased conclusions. Identifying and handling duplicate values is a crucial step in data cleaning and preprocessing.


Figure above shows, there are duplicate values in row 164:


To spot duplicate rows in our dataset,we printed the entire dataset with print(df). Then, to focus on rows 160 to 170 (df_loc[160:170]), we used slicing, like narrowing down our view to a specific group of items. Just as you might notice we found that rows 163 and 164 had exactly the same information.


To enhance the integrity of our dataset, we employed a useful tool called drop_duplicates(). It's like cleaning up duplicates in our collection to keep it neat. In our case, after executing df_no_duplicates = df.drop_duplicates(), the brown (our dataset) now has 302 rows instead of the original 303. It is because those identical rows we identified earlier were successfully removed. This process ensures that our data is more reliable and ready for insightful analysis.








Data formatting

Data formatting ensures that information is presented consistently and correctly. It involves tasks like converting data types, adjusting decimals, or representing dates uniformly.




print(df.dtypes) is for displaying each data types in each column
•	int64 represents integer data type.
•	object represents string (or mixed) data type.
•	float64 represents floating-point data type.

Our decision is to retain the current data types without making any changes. This choice is based on several factors:

No NaN Values:
Since there are no missing values (NaN) in the integer columns,we don't need to convert them to float just to accommodate missing values. This avoids unnecessary conversions.

Compatibility with Algorithms:
Logistic Regression and Gaussian Naive Bayes are flexible algorithms that can handle both integer and float data types.
 


Data Normalization


Before Normalization


![normal](https://drive.google.com/uc?id=1bWFi6qzlx0geIMe55Z9nkWM43fLjJggx)

![normal1](https://drive.google.com/uc?id=1_p-av6KrQkfz6afYKjxp-E8PRIB22BnW)





Count represents the number of non-null (non-missing) values in each column. It indicates the size of the dataset or the number of observations available for analysis in each specific column. 
Mean represents the average (mean) value of each column. It is calculated by summing up all the values in a column and then dividing by the total number of observations. The mean provides a measure of central tendency, giving an idea of the typical value in the dataset.
Std represents the standard deviation, which measures the amount of variation or dispersion in each column. It quantifies how much individual data points differ from the mean. A higher standard deviation indicates greater variability, while a lower standard deviation suggests that the values are closer to the mean.
Min represents the minimum value in each column. It is the smallest observed value and provides insights into the lower bound of the data distribution. For example, the minimum age is 29.
25% (percentile) represents the 25th percentile, also known as the first quartile, is the value below which 25% of the data falls. It is a measure of the data's spread, helping to identify the lower range of the dataset.
50% (percentile) represents the 50th percentile, also known as the median, is the middle point of the data. It separates the lower 50% from the upper 50% of the dataset. The median is less sensitive to extreme values than the mean.
75% (percentile) represents the 75th percentile, also known as the third quartile, is the value below which  75% of the data falls. It represents the upper range of the dataset.
Max represents the maximum value in each column. It is the largest observed value and provides insights into the upper bound of the data distribution. For example, the maximum age is 77.













After Normalization

![normal2](https://drive.google.com/uc?id=19mr4gJ-6HR-OQ5s_r9FIbgqjX_iM3spk)


![normal3](https://drive.google.com/uc?id=1tYnyfJkkCqKzj3_euwzWOEBjxEakOEVy)


Data normalization is a preprocessing technique used in data analysis and machine learning to scale and transform features within a dataset to a common scale. The goal is to ensure that no single feature dominates the learning algorithm due to differences in the scale of the data. Normalization is particularly important for algorithms that rely on distance measures, such as k-nearest neighbors or gradient descent-based optimization algorithms. The data above is normalized by using Min-Max Scaling. 
Min-Max scaling, also known as feature scaling, transforms the values of a numeric column to a specific range, usually [0, 1]. The formula for Min-Max scaling is as follows:

Xnormalized=X−min(X) / max(X)−min(X)
​
Where X is the original value, min(X) is the minimum value in the column, and max(X) is the maximum value in the column. This transformation ensures that all values fall within the specified range as per in the result above.

Binning

Data binning (or bucketing) groups data in bins (or buckets), in the sense that it replaces values contained into a small interval with a single representative value for that interval. Sometimes binning improves accuracy in predictive models.

![binning1](https://drive.google.com/uc?id=1T1veVSH_CPj7uC9DrBo4kk9GFSc_DPnx)




This code performs binning on the 'age' column by categorizing ages into distinct groups. The resulting age groups are defined and labeled in the 'labels' section of the code.

bins: Defines the boundaries for age groups. Each pair of adjacent values in the list represents the lower and upper bounds for an age group. For example, the first age group is 30-39 (inclusive), the second is 40-49, and so on.

labels: Corresponding labels for each age group.

df['age']: Refers to the 'age' column in the DataFrame df.

pd.cut(): This function is used to segment and sort data values into bins. It takes the 'age' column and assigns each value to the appropriate bin based on the specified bins and labels.

bins=bins: Specifies the bin edges.

labels=labels: Specifies the labels to assign to each bin.

right=False: Indicates that the intervals are left-closed, meaning the right bin edge is exclusive. In this case, the intervals are like [29, 39), [39, 49), ..., [89, 99).

![Bin2](https://drive.google.com/uc?id=1CwwV5QYJsoOYyMN9KVpH5Or4-i7msg8T)
This screenshot displays the outcomes of the binning process, revealing the presence of an additional column named 'age_group'.

Indicator variable

We did not perform the indicator variable steps during our data preprocessing because our dataset did not have data with categorical values. We find out that the indicator variables are typically done for categorical data types such as nominal and ordinal that then can be classified into 1 or 0.


