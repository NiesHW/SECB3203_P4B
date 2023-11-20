### Project Progress 2

Project Progress 2 is a crucial phase in our Alzheimer's disease prediction project, focusing on preparing and optimizing our dataset for efficient analysis. This step involves careful handling of missing values, ensuring proper data formatting, and applying statistical techniques to establish the foundation for precise forecasts. Proficiency in Python data handling and the use of key Data Science tools further strengthen our ability to extract valuable insights from the dataset. As we delve into Data Wrangling, actions like data normalization and indicator variable creation become critical, enhancing the accuracy of our prediction models. Project Progress 2 is more than just data preparation; it's a pivotal step toward unlocking valuable insights that contribute to the understanding and prediction of Alzheimer's disease.

### Data Preparation 
The dataset chosen is a raw dataset of Alzheimer’s disease patients which contains 10 columns and 374 rows. The dataset is inconsistent and redundant, which can affect the accuracy of the algorithms. Before evaluating the machine learning algorithms, the data should be clean as we need to remove all the redundancy, missing values and unwanted attributes.

The provided Python code is a comprehensive data preprocessing script tailored for Alzheimer's disease prediction. 
- The script begins by importing essential libraries such as pandas for data manipulation, numpy for numerical operations, and scikit-learn's StandardScaler for data standardization.
- The dataset is loaded from a specified file path, and missing values in numeric columns are filled with the mean, rounded to one decimal place.
- A gender indicator column is created, replacing the original 'M/F' column.
- Age values are binned into groups ('60-70', '70-80', '80-90', '90-100'), and a new column 'Age Group' is added.
- Rows where the 'Group' column is labeled 'Converted' are filtered out, focusing on Demented and Nondemented groups. Selected numeric columns ('nWBV', 'ASF', 'SES', 'CDR') are rounded to three decimal places for clarity.
- The 'eTIV' column is standardized using Z-score normalization.
- Finally, the updated DataFrame is displayed, and the modified dataset is exported to a new CSV file named 'data_alzheimer.csv'.

This script encapsulates a range of preprocessing techniques, setting the stage for subsequent analysis and machine learning model training in Alzheimer's disease prediction.

### Data Analysis
Data analysis is becoming a critical discipline in today's world with an abundance of data in order to derive useful insights from these complicated datasets. It includes the systematic method of examining, cleaning, manipulating, and modeling data in order to uncover information, trends, and patterns that may be concealed. Data analysis is a key component of data-driven decision-making because it may convert unprocessed data into insights that can be used to drive strategic initiatives and promote creativity. 

From this process, we manage to obtain the statistical measure such as mean, median, mod and max from each variable in the dataset before and after the data preparation process.

| Variable | Max | Mean | Median |
|----------|-----|------|--------|
| EDUC     | 7   | 22   | 14.2   |
| SES      | 2   | 6    | 2.3    |
| MMSE     | 16  | 30   | 26.2   |
| CDR      | 0   | 1    | 0.3    |
| eTIV     | 1120| 1990 | 1450   |
| nWBV     | 0.55| 0.81 | 0.7    |
| ASF      | 0.87| 1.43 | 1.3    |

  Figure 1.6 : Data analysis of original dataset

| Variable | Max  | Mean  | Median |
|----------|------|-------|--------|
| EDUC     | 23   | 14.50 | 14     |
| SES      | 5    | 2.54  | 2.5    |
| MMSE     | 30   | 27.20 | 29     |
| CDR      | 2    | 0.29  | 0      |
| eTIV     | 2.853491907 | 1.19E-11 | -0.09075716 |
| nWBV     | 0.837| 0.730 | 0.731  |
| ASF      | 1.587| 1.19  | 1.19   |

  Figure 1.7 : Data analysis of clean dataset
