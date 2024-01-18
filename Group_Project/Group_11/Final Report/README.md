![image](https://github.com/NiesHW/SECB3203_P4B/assets/102138196/09709b95-21d0-4326-88c0-8874583f3ed1)![image](https://github.com/NiesHW/SECB3203_P4B/assets/102138196/95438306-4820-41db-a5bb-20972beb2356)# 1.0 Introduction

The discovery of novel drug-target interactions (DTIs) is an important stage in drug discovery and development, allowing for the development of successful treatment regimens and the advancement of personalized medicine. An existing understanding of drug-target interactions might be a good starting point for discovering new DTI candidates. By studying similarities in drug or target properties such as chemical structure, side effects, and illness linkages, it is possible to predict that medications and targets with equivalent qualities may have similar mechanisms of action.

Despite this, the vast drug-target area is a substantial problem. The drug-target interaction matrix has 7,258,230 entries, which represent 2,529 medicines and 2,870 targets. However, known interactions account for just 0.0024 percent of this matrix, with 17,390 interactions accessible from DrugCentral as of June 18, 2021. As a result, Luo et al. created DTINet, a network integration approach for predicting drug-target interactions.

This study aims to enhance the accuracy and reliability of drug-target interaction (DTI) predictions by extending existing approaches with a two-stage dimensional reduction strategy. We will utilize Python code snippets to implement the main logic of the DTI prediction, leveraging Non-negative Matrix Factorization (NMF) and Matrix Factorization, approaches often used in recommendation systems. By integrating Non-negative Matrix Factorization (NMF), we aim to improve the efficacy of drug-target interaction predictions by reducing the dimensionality of the data. Additionally, we will employ Matrix Factorization to further refine the data representation. In this updated framework, we are incorporating a shift from Jaccard distance to Cosine Similarity in the generation of the similarity matrix, enhancing the accuracy of the initial data comparison step. This comprehensive approach contributes to the identification of novel drug candidates and the advancement of drug discovery processes.
## 1.1 Problem Background

The primary challenge in drug discovery is the identification of new interactions between drugs and proteins, which is crucial for creating new medicines. However, current dimension reduction techniques may not be fully effective in reducing the dimensionality of drug data while preserving relevant information. This can lead to suboptimal predictions in drug-target interactions. With a vast number of potential drug-protein combinations and only a small fraction discovered, there's a need for improved data analysis methods. Matrix factorization and non-negative matrix factorization (NMF) are promising computational techniques that can help organize and analyze large drug datasets more effectively. By employing these methods, researchers can uncover relationships between drugs and proteins, leading to the prediction of previously undiscovered interactions and the development of new drugs.

## 1.2 Problem Statement

The primary objective of this research is to enhance the precision and reliability of Drug-Target Interaction (DTI) predictions through the integration of a two-stage dimensional reduction approach into existing methodologies, as suggested by Byeungchun Kwon in 2022. In pursuit of this goal, we will leverage Python code snippets to construct the core logic for DTI prediction, incorporating both Non-negative Matrix Factorization (NMF) and Matrix Factorization, techniques commonly employed in recommendation systems.

Non-Negative Matrix Factorization (NMF or NNMF) is recognized as a linear dimensionality reduction method, valuable for reducing the complexity of the feature matrix, as discussed by Rukshan Pramoditha on May 6. The essence of our research lies in leveraging NMF to streamline the data, thus empowering us to enhance the performance of drug-target interaction predictions. In our refined approach, we will transition from using Jaccard distance to employing Cosine Similarity in the Matrix Factorization stage. This modification aims to further optimize the identification of new drug candidates and contribute to the advancement of drug development techniques.

This research endeavor is poised to contribute to the identification of new drug candidates and the advancement of drug development techniques. The effectiveness of our predictions will be evaluated through metrics such as ROC AUC, which plays a pivotal role in the identification of novel drug candidates and the continual progression of drug discovery procedures.

## 1.3 Objectives

To implement Cosine Similarity distance on the features to improve drug-disease associations. 

To propose Non-Negative Matrix Factorization(NMF )method to effectively reduce the similarity matrix dimensions.

To evaluate and compare the accuracy and efficacy of the proposed two-stage dimensional reduction approach against the established methodologies.

## 1.4 Scopes
The scope of this research encompasses the following key areas:

Utilization of Public Drug-Target Interaction Dataset: The research will leverage publicly available data from the DrugCentral database, specifically the drug-target interaction dataset. This dataset, accessible to the public, will serve as the foundational source for the study's analysis and modeling of drug-target interactions.

Implementation of Cosine Similarity to Generate a Similarity Matrix: The implementation of cosine similarity to generate a similarity matrix is a crucial step in various data analysis and machine learning tasks. Cosine similarity, a measure of similarity between two vectors, has proven to be particularly effective in quantifying the relatedness of data points in high-dimensional spaces. By constructing a similarity matrix, we can effectively represent the pairwise relationships between data points, enabling us to uncover hidden patterns and derive meaningful insights from the underlying data. 

Implementation of Non-negative Matrix Factorization for Dimensionality Reduction: One of the pivotal components of this research involves the application of Non-negative Matrix Factorization (NMF). NMF will be employed as a fundamental technique to reduce the dimensions of the similarity matrix, thereby streamlining the data for more effective analysis and enhanced prediction accuracy.

Utilization of Google Collab as the Development Platform: The research project will be executed using the Google Collab platform. This integrated development environment (IDE) will serve as the coding environment for the implementation of the Python project. The choice of Google Collab reflects the research's commitment to employing modern and versatile development tools to ensure robust and efficient project development and execution.			
# 2.0 Data Collection and Pre - Processing
## 2.1 Importing Dataset

The necessary datasets were retrieved from DrugCentral and stored within the Google Drive environment. Subsequently, the datasets were imported into Google Colaboratory to facilitate data access for the project and the import process employed the following command:

![image](https://github.com/NiesHW/SECB3203_P4B/assets/102138196/546f991e-9f74-4635-9b0d-2b3a9e3866e9)

Figure 3.1.1

From Figure 3.1.1, we can conclude that we are successfully accessing the datasets that we need for our projects.

## 2.2 Generate a similarity matrix using Cosine Similarity

	After successfully generate the datasets, we then start to generate a similarity matrix using Cosine Similarity. First of all, Cosine similarity stands as a fundamental concept in mathematics and computer science, serving as a quantitative measure of the similarity between two vectors in a multidimensional space. It assesses the degree to which two vectors align in their directions, producing a value ranging from -1 to 1 (Crone & Kanungo, 2023).

A cosine similarity value of -1 indicates perfect dissimilarity, implying that the two vectors are pointing in opposite directions (Martin, n.d.). A value of 0 signifies orthogonality, meaning the vectors are perpendicular to each other, and no similarity exists. Conversely, a value of 1 represents perfect similarity, indicating that the vectors align perfectly.

Drug-target interaction (DTI) projects often involve analyzing large datasets of molecular representations. These representations encapsulate the structural and functional information of molecules. Cosine similarity proves to be an invaluable tool in DTI studies due to its ability to effectively handle high-dimensional data and accurately assess molecular similarities (Sohangir & Wang, 2017).

For an overview of on simple understanding on how Cosine Similarity works, here are the formula between 2 vectors:

cos(θ) = (A ⋅ B) / (||A|| ||B||)

where:

A ⋅ B represents the dot product of vectors A and B
||A|| and ||B|| denote the magnitudes of vectors A and B, respectively 

 Those formula represented with this this command for our dataset:
 
 ![image](https://github.com/NiesHW/SECB3203_P4B/assets/102138196/4d971806-ab2a-418f-8741-a18995232c6e)

Figure 3.2.1

Firstly, we initialize a dictionary to store the similarity matrices. The similarity_df dictionary is initialized to store the drug-target and drug-drug similarity matrices. This dictionary will be populated in the following loop. The for loop iterates through the key-value pairs in the raw_df dictionary. Each key represents a type of similarity matrix and the corresponding value represents the data for that matrix. Lastly, we round similarity values to two decimal places The apply method is used to apply the round function to each element of the drug_disease similarity matrix. This rounds the values to two decimal places.

![image](https://github.com/NiesHW/SECB3203_P4B/assets/102138196/ad1ef2c3-e3ba-499c-9b19-0ae84636afc4)

Figure 3.2.2

The above figure shows the output of the similarity matrix from the cosine process.





## 2.3 Reduce similarity matrix dimensions using NMF

After computing all the drug similarity matrices, the code concatenates these separate matrices into a single drug matrix. Each drug matrix has dimensions 708×2832, where the rows represent individual drugs, and the columns correspond to drug interaction, disease, side effect, and drug similarity features. Prior to the concatenation step, a normalization process is applied to ensure consistent scaling of the values across the matrices.

![image](https://github.com/NiesHW/SECB3203_P4B/assets/102138196/c3015656-f206-4d56-8345-b950acabb794)

FIGURE 3.3.1
Not much to say about these codings as they were pretty much similar to the original case study. First things first, the code starts by loading similarity matrices for drugs and proteins from external text files (Similarity_Matrix_Drugs.txt and Similarity_Matrix_Proteins.txt, respectively) into Pandas DataFrames. Followed by the Diffusion Component Analysis (DCA), the calc_dca function is defined to perform Diffusion Component Analysis on the input matrix (df_mat). DCA is an iterative algorithm that computes a diffusion matrix, and the code seems to be iterating through different drug similarity matrices and concatenating them into a single matrix (drug_dca and protein_dca).

![image](https://github.com/NiesHW/SECB3203_P4B/assets/102138196/e74d2914-91b0-49fb-9b2c-ff72dfb6d115)

FIGURE 3.3.2
Next is the Concatenation and Normalization. The resulting matrices (drug_dca and protein_dca) are concatenated along the columns. Additionally, a round function is applied to the resulting DataFrame to round the values to two decimal places.

![image](https://github.com/NiesHW/SECB3203_P4B/assets/102138196/5ebd5761-2152-4f6d-a75c-6cc806285269)

FIGURE 3.3.3

This is the part where the changes occur from SVD to NMF. Before the changes, the original code uses the TruncatedSVD implementation from scikit-learn to perform dimensionality reduction on a given matrix (dca_mtx). While on our end, based on FIGURE 3.2.3, we utilize the NMF, this applies a log transformation and matrix multiplication as preprocessing steps. The resulting reduced representation is stored in the variable result.

![image](https://github.com/NiesHW/SECB3203_P4B/assets/102138196/96536e45-ccc0-4cc4-b108-4c5cc33ff84f)

FIGURE 3.3.4
In this segment of the coding, the code is structured as a function (calc_nmf) that takes a matrix and the number of desired features as input parameters, as opposed to (calc_svd). 

![image](https://github.com/NiesHW/SECB3203_P4B/assets/102138196/41ef47d1-ddf6-4159-9d73-5cee0319a58d)

FIGURE 3.3.5
As seen from FIGURE 3.2.3 and 3.2.4, the output differs. Using NMF, the output is mostly 0s and positive numbers. This may lead to Non-negative factorization, potentially providing more interpretable results. Because we want to focus on additive, non-negative components, NMF might be a better choice. The absence of negative values can make the results more intuitive to interpret. The choice between NMF and SVD was guided by how well the factorized matrices align with the known drug-target interactions. We already evaluate the performance of both methods using appropriate metrics, such as using the roc_auc_score function in Sci-kit learn to compute the area under the ROC curve (ROC AUC). As a result, because negative values are not meaningful or don't align with the nature of our data, NMF is a preferable choice.
## 2.4 Software & Hardware Requirements

### 2.4.1 Software
DrugCentral. DrugCentral is an online drug information resource created and maintained by Division of Translational Informatics at University of New Mexico in collaboration with the IDG. DrugCentral provides information on active ingredients, chemical entities, pharmaceutical products, drug mode of action, indications, pharmacologic actions. “DrugCentral provides the drug information resource. We can download the known drug-target interaction from literature review, drug labels and external data sources. There are 2529 drugs, 2870 targets and 17390 drug-target interactions in the DrugCentral site as of 18 June 2021” (Byeungwon Kwon, 2021).

GitHub. While GitHub is a code hosting platform for version control and collaboration. We use GitHub as a method to communicate with our client as well as a reference for the previous project, while they use SVD (Singular Value Decomposition) to predict drug-target interaction, we decided to tweak it and use NMF (Non-negative Matrix Factorization) instead. We also use GitHub as a medium for our project for others alike to see gain something from in the near future. In GitHub as well we can find Luo et al., which introduces a network integration approach for drug-target interaction prediction and develops DTINet.

Nature Communications. Nature Portfolio is used to serve the research community by publishing its most significant discoveries—findings that advance knowledge and address some of the greatest challenges that we face as a society today. An article ‘A network integration approach for drug-target interaction prediction and computational drug repositioning from heterogeneous information’ is used as a reference for our project.

Google Colab. Google Colab is a free, cloud-based platform that enables you to write and execute Python code collaboratively. It provides an environment similar to Anaconda Python, allowing users to work with Python code seamlessly. PythonAnywhere by Anaconda is being replaced with Google Colab as our Python programming language compiler and the core of the project.

Visual Studio Code (VSC). Visual Studio Code is a code editor redefined and optimized for building and debugging modern web and cloud applications. We initially used VSC for our Python programming.
	
### 2.4.2 Hardware

Personal laptop. We both use our own laptops as our current and only hardware for now. This will help us with Python programming, researching and communicating with our client as well as our lecturer for any external assistance and advice. They say two is better than one, therefore with both of us using our own individual laptops will absolutely make our project finish quickly and without any real challenges others may face.

# 3.0 Flowchart of Proposed Approach

 ![image](https://github.com/NiesHW/SECB3203_P4B/assets/102138196/988951bb-ae9a-4dac-b269-99c68308c59d)

## 3.1 Model Development 

For model development, we did matrix completion to search for a new drug - target interaction. Matrix completion is a mathematical methodology applied in diverse domains, including bioinformatics and drug discovery, to address the challenge of predicting or imputing missing values within a data matrix. In the specific context of uncovering novel drug-target interactions, matrix completion serves as a computational tool to forecast potential interactions where empirical data is incomplete or unavailable.

The representation of drug-target interactions adopts a binary matrix format, wherein rows correspond to distinct drugs, columns to individual targets, and matrix entries denote the presence or absence of observed interactions. The inherent sparsity of this matrix arises from the limited availability of experimental data due to resource constraints and the intricacies of laboratory validation processes.

In the realm of drug discovery, the application of matrix completion for predicting novel drug-target interactions offers a strategic approach to prioritize candidates for experimental validation. By facilitating the identification of potential interactions in a computationally efficient manner, matrix completion accelerates the drug discovery pipeline, mitigating the need for exhaustive and resource-intensive experimental screening processes.
	
![image](https://github.com/NiesHW/SECB3203_P4B/assets/102138196/290a42c0-722c-4940-a9c5-e7e124b38805)

![image](https://github.com/NiesHW/SECB3203_P4B/assets/102138196/260f9b54-11c3-4020-b4e5-8e108b0a303a)

The provided code implements matrix factorization using stochastic gradient descent with the goal of approximating a given matrix R as the product of two lower-rank matrices P and Q. This method is often used in collaborative filtering and recommendation systems. The code utilizes the Numba library for just-in-time (JIT) compilation to improve performance.

The `matrix_factorization` function takes as input the matrix R and initializes matrices P and Q, which are then iteratively updated to minimize the difference between the predicted matrix product of P and Q and the actual values in R. The process involves calculating the error for each observed value, adjusting the elements of P and Q based on the error, and iteratively refining the matrices through multiple steps.

The function takes parameters such as the number of steps for the optimization, the learning rate (alpha), and regularization parameters (beta). The loop structure involves iterating through the rows and columns of R, updating the elements of P and Q accordingly. The optimization continues until a specified convergence criterion is met (in this case, when the error falls below a threshold of 0.001).

Finally, the function returns the optimized matrices P and Q, which together provide an approximation of the original matrix R. The code demonstrates an efficient way to perform matrix factorization for collaborative filtering, with the Numba library contributing to computational speed by compiling the Python code to machine code.


## 3.2 Model Evaluation

In Step 5, the evaluation of the predicted drug-target interactions is performed by comparing the calculated drug-target matrix resulting from the matrix factorization process with the known drug-target matrix. The choice of the ROC AUC (Receiver Operating Characteristic Area Under the Curve) as the evaluation metric indicates the model's ability to discriminate between positive and negative instances in a binary classification context. Specifically, the ROC AUC score quantifies the overall performance of the model in distinguishing true positive interactions from false positive ones.

The ROC AUC score obtained in our experiment is notably high, measuring 0.9976720738570403. This exceptional score suggests that the model, which employs Cosine Similarity in Step 2 and NMF (Non-Negative Matrix Factorization) in Step 3, performs exceptionally well in discriminating between true and predicted drug-target interactions. A ROC AUC score of 1.0 represents perfect classification, indicating that the model has achieved nearly optimal separation between positive and negative instances. The superior performance compared to the previous study, which utilized Jaccard distance in Step 2 and SVD in Step 3, suggests that the modifications made in these steps have led to improved accuracy and precision in predicting drug-target interactions.

This remarkable ROC AUC score indicates that the model's predictions align closely with the true drug-target interactions, and the chosen combination of similarity measure (Cosine Similarity) and matrix factorization technique (NMF) has proven effective in capturing the underlying patterns in the data. The higher ROC AUC score implies enhanced sensitivity and specificity, further supporting the reliability and efficacy of the modified approach in predicting drug-target interactions.

![image](https://github.com/NiesHW/SECB3203_P4B/assets/102138196/14fa0261-79c9-42a0-9f6a-9629b0b67d97)

![image](https://github.com/NiesHW/SECB3203_P4B/assets/102138196/07fb8e10-e20c-44d1-8292-d4f40f11cced)

The first line indicates Import the roc_auc_score function from scikit-learn, which is used to calculate the ROC AUC score.

![image](https://github.com/NiesHW/SECB3203_P4B/assets/102138196/2df1529e-f03f-4c76-91a3-871228edac08)

The variable n_drug_protein seems to contain the predicted drug-target interaction matrix. This matrix is converted to a DataFrame, stacked, and indexed using the drug and target indices. The resulting DataFrame is sorted by the index.

![image](https://github.com/NiesHW/SECB3203_P4B/assets/102138196/12c5a102-12e2-4d39-abe3-4a77206bd17d)
	
The variable R seems to contain the true drug-target interaction matrix. Similar to the predicted interaction matrix, it is converted to a DataFrame, stacked, and indexed. The index is then used to extract the relevant rows from the true interaction matrix. The resulting DataFrame is also sorted by the index.

![image](https://github.com/NiesHW/SECB3203_P4B/assets/102138196/fac09bcd-d91a-48e9-a2c7-d97d5d91f3ed)

Finally, the ROC AUC score is calculated by comparing the true drug-target interaction (r) with the predicted drug-target interaction (rhat). The ROC AUC score is a performance metric commonly used for binary classification problems, and it measures the area under the ROC curve. It provides an overall measure of the model's ability to distinguish between positive and negative instances.
	
![image](https://github.com/NiesHW/SECB3203_P4B/assets/102138196/9c5b64b1-cfc5-4104-8d8e-4da3b23403eb)

Thus, the output is as such.

# 4.0 Feedback from Client

Be more confident during the presentation.
From introduction until conclusion, everything must align and not contradict.
The flow must be consistent.
Dr Zuraini added some comments to improve the final report.
Refine the objectives.
Make the problem to be more related and easy to understand regardless of backgrounds.
State the importance of our project and why we choose to proceed with said topic.
No need to present/show codings during the presentation.

# 5.0 Conclusion 

To sum up everything, this proposal highlights the two-stage approach aimed at enhancing the prediction of how drugs and proteins interact. Our primary goals are to increase the accuracy prediction and at the same time uncover new interactions between drugs and proteins. By changing the third step of DTINet from using Singular Value Decomposition (SVD) into Non-negative Matrix Factorization (NMF) to reduce similarity matrix dimensions, we hope to enhance its accuracy to more than 0.5 using the roc_auc_score function. 

In parallel, our research aims to explore and identify potential novel interactions between drugs and proteins. In the context of drug discovery and development, it's crucial to understand how different drugs can interact with specific proteins in the human body. These interactions often determine a drug's effectiveness, potential side effects, and overall safety. In our refined approach, we are transitioning from using Jaccard distance to employing Cosine Similarity in the process of generating similarity matrices. This modification aims to further optimize our ability to discover new therapeutic prospects. 

Last but not least, our proposal presents a strategy to enhance predictive capabilities and discover new therapeutic prospects. It is important to note that further research and testing are required to determine the effectiveness and practical applications of this approach.

# 6.0 Appendix

Link for Github
https://github.com/NiesHW/SECB3203_P4B/tree/main/Group_Project/Group_11

Link for Google Colab
https://colab.research.google.com/drive/1AC22cu-zrKOyCkb5AltPxiP9LF94r84S

Meeting with Client:
1st Meeting

![image](https://github.com/NiesHW/SECB3203_P4B/assets/102138196/3630aeb0-52da-4bfe-a57e-edf6b2541665)

2nd Meeting

![image](https://github.com/NiesHW/SECB3203_P4B/assets/102138196/9a05b89c-6272-4fac-8546-0c58f768e2da)

3rd Meeting.

![image](https://github.com/NiesHW/SECB3203_P4B/assets/102138196/6cdebdc0-1e40-4dc1-b120-e600ab1054dc)

# 7.0 References

Central, D. (2023). About. Drug Central. Retrieved October 19, 2023, from https://drugcentral.org/about

Crone, N., & Kanungo, N. (2023, August 14). Methods of Similarity. KDB.AI. Retrieved November 26, 2023, from https://kdb.ai/learning-hub/fundamentals/methods-of-similarity/

Kwon, B. (2021, June 23). Drug-Target interaction prediction through Python | by Byeungchun Kwon | Geek Culture. Medium. Retrieved October 15, 2023, from https://medium.com/geekculture/drug-target-interaction-prediction-through-python-4af9e76fc90

Luo, Y., Zhao, X., Zhou, J., Yang, J., Zhang, Y., & Kuang, W. (2017, September 18). A network integration approach for drug-target interaction prediction and computational drug repositioning from heterogeneous information. https://www.nature.com/articles/s41467-017-00680-8

Martin, B. (n.d.). Cosine Similarity – LearnDataSci. LearnDataSci. Retrieved November 26, 2023, from https://www.learndatasci.com/glossary/cosine-similarity/

Pramoditha, R. (2023, August 24). Non-Negative Matrix Factorization (NMF) for Dimensionality Reduction in Image Data. Towards Data Science. Retrieved October 21, 2023, from https://towardsdatascience.com/non-negative-matrix-factorization-nmf-for-dimensionality-reduction-in-image-data-8450f4cae8fa

sklearn.decomposition.NMF — scikit-learn 1.3.1 documentation. (n.d.). Scikit-learn. Retrieved October 16, 2023, from https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.NMF.html

Sohangir, S., & Wang, D. (2017, July 25). Improved sqrt-cosine similarity measurement - Journal of Big Data. Journal of Big Data. Retrieved November 26, 2023, from https://journalofbigdata.springeropen.com/articles/10.1186/s40537-017-0083-6
