# 3.0 Importing Dataset
## 3.1 Understanding the data 
The dataset name is Classification Prediction of Prostate Cancer obtained from the Kaggle Website. 
[4] In this dataset, it has 100 rows and 10 columns [100 x 10]. Most of the data type of this dataset is float64 with 1 string. 

## 3.2 Importing and exporting data in Python
<img src="https://github.com/NiesHW/SECB3203_P4B/blob/cc515a621a5a25f25655b5c10ed6f827bbabb9aa/Group_Project/Group_14/WhatsApp%20Image%202023-12-03%20at%2012.01.38%20AM%20(4).jpeg" alt="Flowchart of System" width="500">

The command from google.colab “import files” along with “files.upload()”  is utilized in Google Colab to facilitate the importing of files from your local system into the Colab environment.

## 3.4 Python packages for Data Science
<img src="https://github.com/NiesHW/SECB3203_P4B/blob/cc515a621a5a25f25655b5c10ed6f827bbabb9aa/Group_Project/Group_14/WhatsApp%20Image%202023-12-03%20at%2012.01.39%20AM.jpeg" alt="Flowchart of System" width="500">
These commands are foundational in data science workflows:

1. Pandas is used for data handling and manipulation.
2. Scikit-Learn provides machine learning algorithms and tools, where StandardScaler helps preprocess data for modeling.
3. NumPy is a core library for numerical computing.
4. The warning suppression can enhance the readability of the code output by ignoring non-critical warnings during execution.

# 4.0 Data Wrangling (Pandas/Numpy)
## 4.1 Identifying and handling missing values
<img src="https://github.com/NiesHW/SECB3203_P4B/blob/cc515a621a5a25f25655b5c10ed6f827bbabb9aa/Group_Project/Group_14/WhatsApp%20Image%202023-12-03%20at%2012.01.38%20AM.jpeg" alt="Flowchart of System" width="500">
Figure 4.1 shows the output after running the command implies that there are no missing values found in the dataset.

The command df.isnull().sum() is used to identify and count missing or null values in a DataFrame df using Pandas, a popular library in Python for data manipulation and analysis.

## 4.2 Data normalization (centering/scaling)
<img src="https://github.com/NiesHW/SECB3203_P4B/blob/cc515a621a5a25f25655b5c10ed6f827bbabb9aa/Group_Project/Group_14/WhatsApp%20Image%202023-12-03%20at%2012.01.38%20AM%20(5).jpeg" alt="Flowchart of System" width="500">
Data normalization is a process to make model training less sensitive to the scale of features. [5] From the dataset, we chose the column with datatype of float64 and create a an object name StandardScaler. Here, we can see that the data inside the csv file have been change to a more numerical number. 

## 4.3 Indicator variables
<img src="https://github.com/NiesHW/SECB3203_P4B/blob/3da583c3c6dd8db716f3e8ef7fd72bc3b430dd8e/Group_Project/Group_14/WhatsApp%20Image%202023-12-03%20at%2012.24.52%20AM.jpeg" alt="Flowchart of System" width="500">
Indicator variables (or dummy variables) are variables that take on only the value of 0 and 1, and are used to indicate whether a given observation belongs to a discrete category in a way that can be used in statistical models. [6]  In this example, we are using the diagnosis_result column to create the dummy variables. Diagnosis_result only have 2 data which is M and B. If the data row contains M data, then the column in diagnosis_result_M will be 1 and vice versa. 

# REFERENCES
1. Lim J, Malek R, Jr S, et al. Prostate cancer in multi-ethnic Asian men: Real-world experience in the Malaysia Prostate Cancer (M-CaP) Study. Cancer Med. 2021;10(22):8020-8028. doi:10.1002/cam4.4319
2. Tang X. The role of artificial intelligence in medical imaging research. BJR Open. 2019;2(1):20190031. Published 2019 Nov 28. doi:10.1259/bjro.20190031
3. Salem H, Soria D, Lund JN, Awwad A. A systematic review of the applications of Expert Systems (ES) and machine learning (ML) in clinical urology. BMC Med Inform Decis Mak. 2021;21(1):223. Published 2021 Jul 22. doi:10.1186/s12911-021-01585-9
4. SHARMA, R. (2023, September 27). Classification prediction of Prostate cancer. Kaggle. Kaggle. Retrieved December 2, 2023, from https://www.kaggle.com/code/rohit265/classification-prediction-of-prostate-cancer/notebook 
5. Educative answers - trusted answers to developer questions. (n.d.). Educative. Retrieved December 2, 2023, from https://www.educative.io/answers/data-normalization-in-python 
6. Using and interpreting indicator (dummy) variables. (n.d.). Using and Interpreting Indicator (Dummy) Variables - Unifying Data Science. Retrieved December 2, 2023, from https://www.unifyingdatascience.org/html/interpreting_indicator_vars.html#:~:text=Indicator%20variables%20%E2%80%93%20sometimes%20also%20referred,be%20used%20in%20statistical%20models. 









