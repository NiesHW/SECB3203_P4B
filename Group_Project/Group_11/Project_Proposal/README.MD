# 1.0 Introduction
- The discovery of novel drug-target interactions (DTIs) is an important stage in drug discovery and development, allowing for the development of successful treatment regimens and the advancement of personalized medicine. Existing understanding of drug-target interactions might be a good starting point for discovering new DTI candidates. By studying similarities in drug or target properties such as chemical structure, side effects, and illness linkages, it is possible to predict that medications and targets with equivalent qualities may have similar mechanisms of action.

- Despite this, the vast drug-target area is a substantial problem. The drug-target interaction matrix has 7,258,230 entries, which represent 2,529 medicines and 2,870 targets. However, known interactions account for just 0.0024 percent of this matrix, with 17,390 interactions accessible from DrugCentral as of June 18, 2021. As a result, Luo et al. created DTINet, a network integration approach for predicting drug-target interactions.

- This study aims to increase the accuracy and reliability of DTI predictions by extending existing approaches with a two-stage dimensional reduction strategy. We will utilize Python code snippets to create the main logic of the DTI prediction, leveraging Non-negative Matrix Factorization (NMF) and Matrix Factorization, approaches often used in recommendation systems. We want to improve the efficacy of drug-target interaction predictions by using NMF to reduce the dimensionality of the data, thereby contributing to the identification of novel drug candidates and the development of drug discovery processes.

# 1.1 Problem Background
- The identification of new drug-target interactions (DTIs) is critical to the creation of effective treatment regimens and the progress of personalized medicine  (Byeungchun Kwon, 2022). While current understanding of drug-target interactions might be a useful starting point for uncovering novel DTI candidates, the huge drug-target space remains a significant hurdle. The drug-target interaction matrix has 7,258,230 entries for 2,529 medicines and 2,870 targets, although only 0.0024 percent of this space is occupied by the known 17,390 interactions accessible from DrugCentral as of June 18, 2021. As a result, there is an urgent need for novel computational tools that can successfully explore this large environment and forecast probable connections.

# 1.2 Problem Statement
- The major goal of this research is to improve the accuracy and dependability of DTI predictions by incorporating a two-stage dimensional reduction technique into current methodologies (Byeungchun Kwon, 2022). We will use Python code snippets to create the main logic of DTI prediction, which will make use of Non-negative Matrix Factorization (NMF) and Matrix Factorization, both of which are frequently used in recommendation systems. Non-Negative Matrix Factorization (NMF or NNMF) is also a linear dimensionality reduction technique that can be used to reduce the dimensionality of the feature matrix (Rukshan Pramoditha, May 6). We want to enhance the performance of drug-target interaction predictions by using NMF to minimize the complexity of the data. This research project intends to aid in the identification of new drug candidates and the advancement of drug development methods. These predictions will be evaluated using metrics such as ROC AUC, which will aid in the identification of novel drug candidates and the progress of drug discovery procedures.

# 1.3 Objectives
-  1. To increase the accuracy and reliability of Drug-Target Interaction predictions by
extending existing approaches with a two-stage dimensional reduction strategy.

- 2. To identify novel Drug-Target Interaction.


# 1.4 Scopes
The scopes of the research are:

(a) Using the dataset of the drug target interaction from DrugCentral database that is open
publicly.

(b) Using Non-negative Matrix Factorization to reduce similarity matrix dimensions.

(c) Using VIrtual Studio Code platform to code our python project.


# 1.5 Conclusion
- To sum up everything, this proposal highlight the two-stage approach aimed at enhancing
prediction on how drugs and proteins interact. Our primary goals are to increase the accurancy
prediction and at the same time uncovering the new interactions between drugs and proteins. By
changing third step of DTINet from using the Singular Value Decomposition(SVD) into
Non-negative Matrix Factorization(NMF) to reduce similarity matrix dimensions, we hope that
we can increase its accuracy to more than 0.5 using roc_auc_score function.

- Simultaneously, our research aims to explore and identify potential novel interactions between
drugs and proteins. In the context of drug discovery and development, it's crucial to understand
how different drugs can interact with specific proteins in the human body. These interactions
often determine a drug's effectiveness, potential side effects, and overall safety. These
discoveries also could open the doors to new treatment possibilities for medical conditions that
were previously uncharted.

- Last but not least, our proposal presents a strategy to enhance predictive capabilities and discover
new therapeutic prospects. It is important to note that further research and testing are required to
determine the effectiveness and practical applications of this approach.


# 1.6 References
Central, D. (2023). About. Drug Central. Retrieved October 19, 2023, from
https://drugcentral.org/about

Kwon, B. (2021, June 23). Drug-Target interaction prediction through Python | by Byeungchun
Kwon | Geek Culture. Medium. Retrieved October 15, 2023, from
https://medium.com/geekculture/drug-target-interaction-prediction-through-python-4af9e
76fc90

Luo, Y., Zhao, X., Zhou, J., Yang, J., Zhang, Y., & Kuang, W. (2017, September 18). A network
integration approach for drug-target interaction prediction and computational drug
repositioning from heterogeneous information.
https://www.nature.com/articles/s41467-017-00680-8

Pramoditha, R. (2023, August 24). Non-Negative Matrix Factorization (NMF) for
Dimensionality Reduction in Image Data. Towards Data Science. Retrieved October 21,
2023, from
https://towardsdatascience.com/non-negative-matrix-factorization-nmf-for-dimensionalit
y-reduction-in-image-data-8450f4cae8fa7

sklearn.decomposition.NMF — scikit-learn 1.3.1 documentation. (n.d.). Scikit-learn. Retrieved
October 16, 2023, from
https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.NMF.htm

