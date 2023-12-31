1.0 Introduction

The discovery of novel drug-target interactions (DTIs) is an important stage in drug discovery and development, allowing for the development of successful treatment regimens and the advancement of personalized medicine. An existing understanding of drug-target interactions might be a good starting point for discovering new DTI candidates. By studying similarities in drug or target properties such as chemical structure, side effects, and illness linkages, it is possible to predict that medications and targets with equivalent qualities may have similar mechanisms of action.

Despite this, the vast drug-target area is a substantial problem. The drug-target interaction matrix has 7,258,230 entries, which represent 2,529 medicines and 2,870 targets. However, known interactions account for just 0.0024 percent of this matrix, with 17,390 interactions accessible from DrugCentral as of June 18, 2021. As a result, Luo et al. created DTINet, a network integration approach for predicting drug-target interactions.

This study aims to enhance the accuracy and reliability of drug-target interaction (DTI) predictions by extending existing approaches with a two-stage dimensional reduction strategy. We will utilize Python code snippets to implement the main logic of the DTI prediction, leveraging Non-negative Matrix Factorization (NMF) and Matrix Factorization, approaches often used in recommendation systems. By integrating Non-negative Matrix Factorization (NMF), we aim to improve the efficacy of drug-target interaction predictions by reducing the dimensionality of the data. Additionally, we will employ Matrix Factorization to further refine the data representation. In this updated framework, we are incorporating a shift from Jaccard distance to Cosine Similarity in the generation of the similarity matrix, enhancing the accuracy of the initial data comparison step. This comprehensive approach contributes to the identification of novel drug candidates and the advancement of drug discovery processes.

1.1 Problem Background

The primary challenge in drug discovery is the identification of new interactions between drugs and proteins, which is crucial for creating new medicines. However, current dimension reduction techniques may not be fully effective in reducing the dimensionality of drug data while preserving relevant information. This can lead to suboptimal predictions in drug-target interactions. With a vast number of potential drug-protein combinations and only a small fraction discovered, there's a need for improved data analysis methods. Matrix factorization and non-negative matrix factorization (NMF) are promising computational techniques that can help organize and analyze large drug datasets more effectively. By employing these methods, researchers can uncover relationships between drugs and proteins, leading to the prediction of previously undiscovered interactions and the development of new drugs.

1.2 Problem Statement

The primary objective of this research is to enhance the precision and reliability of Drug-Target Interaction (DTI) predictions through the integration of a two-stage dimensional reduction approach into existing methodologies, as suggested by Byeungchun Kwon in 2022. In pursuit of this goal, we will leverage Python code snippets to construct the core logic for DTI prediction, incorporating both Non-negative Matrix Factorization (NMF) and Matrix Factorization, techniques commonly employed in recommendation systems.

Non-Negative Matrix Factorization (NMF or NNMF) is recognized as a linear dimensionality reduction method, valuable for reducing the complexity of the feature matrix, as discussed by Rukshan Pramoditha on May 6. The essence of our research lies in leveraging NMF to streamline the data, thus empowering us to enhance the performance of drug-target interaction predictions. In our refined approach, we will transition from using Jaccard distance to employing Cosine Similarity in the Matrix Factorization stage. This modification aims to further optimize the identification of new drug candidates and contribute to the advancement of drug development techniques.

This research endeavor is poised to contribute to the identification of new drug candidates and the advancement of drug development techniques. The effectiveness of our predictions will be evaluated through metrics such as ROC AUC, which plays a pivotal role in the identification of novel drug candidates and the continual progression of drug discovery procedures.

1.3 Objectives

1. To effectively reduce the dimensions of the similarity matrix transitioning from the conventional Singular Value Decomposition (SVD) and Jaccard Distance  approach to the utilization of Non-negative Matrix Factorization (NMF) and Cosine Similarity. 

2. To evaluate and compare the accuracy and efficacy of the proposed two-stage dimensional reduction approach against the established methodologies.
