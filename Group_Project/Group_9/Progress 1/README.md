# PROJECT PROGRESS 1

In Project Progress 1, we outline the essential software and hardware requirements for our endeavor, "Analysis of Machine Learning Algorithms for Alzheimer's Disease Prediction Based on Clinical Data." Additionally, we will present a flowchart of our proposed approach to provide a visual overview of the project's direction and structure.

## 2.1 SOFTWARE & HARDWARE REQUIREMENTS

### 2.1.1 SOFTWARE

- **Programming Language**: Python
- **Development Environment (IDE)**: Visual Studio Code
- **Database Management**: MySQL
- **Version Control**: Git
- **Project Management Tools**: Github

### 2.1.2 HARDWARE

- **Operating System**: Windows 10
- **Computer/Server**:
  - CPU: AMD Ryzen 7
  - RAM: 8.00 GB
  - Storage: 512 GB
- **Cloud Services**: Google Cloud

## 2.2 FLOWCHART OF PROPOSED APPROACH

Our proposed approach is by using machine learning to detect early-stage Alzheimer's disease. The flowchart of our proposed approach is shown below along with our reference flowchart.

[Insert Flowchart Image Here]


In our proposed flowchart, we chose to use clinical data of Alzheimer's disease patients as our primary dataset for this project due to its critical significance in advancing our understanding of the disease and improving early diagnosis. Clinical data contains valuable information about patient demographics, cognitive assessments, medical history, and biomarker measurements, allowing us to employ machine learning algorithms to develop predictive models that can aid in early Alzheimer's disease detection and, ultimately, support better patient care and research outcomes.

In the data preprocessing pipeline, we first addressed missing values to ensure the integrity of our clinical data for Alzheimer's disease prediction. Imputation techniques were applied to fill in these gaps, allowing us to maintain a complete dataset. Subsequently, we delved into data analysis, where we examined various features and their relationships. To enhance the comparability of our features, Z-score normalization was employed, standardizing the data distribution. Finally, we conducted ANOVA (Analysis of Variance) to assess the significance of different variables and their potential impact on Alzheimer's disease prediction. These steps have laid the foundation for robust and reliable data analysis as we progress with our project.

Moving into the feature selection process, we incorporated the use of the correlation coefficient to identify and retain the most relevant variables for our Alzheimer's disease prediction model. By quantifying the strength and direction of relationships between features, we were able to pinpoint those with the highest correlations to our target variable. This approach enables us to streamline our model and focus on the most influential factors, enhancing the accuracy and interpretability of our predictive algorithm.

For the classification phase of our project, we implemented several algorithms, including Random Forest, Support Vector Machine (SVM), Decision Tree, and ElasticNet algorithm, the powerful ensemble method known for its effectiveness in predictive modeling. We divided our dataset into two crucial components: the training data and the testing data. The training data was used to teach our machine learning model to recognize patterns and relationships within the clinical data, while the testing data served as a completely independent set for evaluating the model's performance. This rigorous separation allows us to assess the accuracy and reliability of our Alzheimer's disease prediction model when applied to new, unseen data, a pivotal step in ensuring the model's real-world applicability.

Lastly, in the evaluation phase of our project, we employed statistical tests by calculating p-values to assess the significance of our results. By comparing the model's predictions with ground truth data, we observed key performance metrics, including accuracy, precision, F1 score, and recall. These metrics provide a comprehensive view of our model's effectiveness in Alzheimer's disease prediction. A low p-value signifies the model's significance, while accuracy, precision, F1, and recall metrics help us gauge its overall performance in terms of correctness, predictive power, and the ability to identify true positive cases and minimize false negatives. This robust evaluation process ensures the reliability and utility of our machine learning model for clinical applications.
