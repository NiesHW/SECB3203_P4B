# 1.0 Introduction
The discovery of novel drug-target interactions (DTIs) is an important stage in drug discovery and development, allowing for the development of successful treatment regimens and the advancement of personalized medicine. An existing understanding of drug-target interactions might be a good starting point for discovering new DTI candidates. By studying similarities in drug or target properties such as chemical structure, side effects, and illness linkages, it is possible to predict that medications and targets with equivalent qualities may have similar mechanisms of action.

Despite this, the vast drug-target area is a substantial problem. The drug-target interaction matrix has 7,258,230 entries, which represent 2,529 medicines and 2,870 targets. However, known interactions account for just 0.0024 percent of this matrix, with 17,390 interactions accessible from DrugCentral as of June 18, 2021. As a result, Luo et al. created DTINet, a network integration approach for predicting drug-target interactions.

This study aims to increase the accuracy and reliability of DTI predictions by extending existing approaches with a two-stage dimensional reduction strategy. We will utilize Python code snippets to create the main logic of the DTI prediction, leveraging Non-negative Matrix Factorization (NMF) and Matrix Factorization, approaches often used in recommendation systems. We want to improve the efficacy of drug-target interaction predictions by using NMF to reduce the dimensionality of the data, thereby contributing to the identification of novel drug candidates and the development of drug discovery processes.

# 1.1 Problem Background
The primary challenge in drug discovery is the identification of new interactions between drugs and proteins, which is crucial for creating new medicines. However, current dimension reduction techniques may not be fully effective in reducing the dimensionality of drug data while preserving relevant information. This can lead to suboptimal predictions in drug-target interactions. With a vast number of potential drug-protein combinations and only a small fraction discovered, there's a need for improved data analysis methods. Matrix factorization and non-negative matrix factorization (NMF) are promising computational techniques that can help organize and analyze large drug datasets more effectively. By employing these methods, researchers can uncover relationships between drugs and proteins, leading to the prediction of previously undiscovered interactions and the development of new drugs.

# 1.2 Problem Statement
The major goal of this research is to improve the accuracy and dependability of DTI predictions by incorporating a two-stage dimensional reduction technique into current methodologies (Byeungchun Kwon, 2022). We will use Python code snippets to create the main logic of DTI prediction, which will make use of Non-negative Matrix Factorization (NMF) and Matrix Factorization, both of which are frequently used in recommendation systems. Non-Negative Matrix Factorization (NMF or NNMF) is also a linear dimensionality reduction technique that can be used to reduce the dimensionality of the feature matrix (Rukshan Pramoditha, May 6). We want to enhance the performance of drug-target interaction predictions by using NMF to minimize the complexity of the data. This research project intends to aid in the identification of new drug candidates and the advancement of drug development methods. These predictions will be evaluated using metrics such as ROC AUC, which will aid in the identification of novel drug candidates and the progress of drug discovery procedures.

# 1.3 Objectives
- To improve the accuracy and reliability of Drug-Target Interaction predictions by changing existing approaches which is using Singular Value Decomposition into Non-negative Matrix Factorization to reduce the similarity matrix dimensions. 

- To evaluate and compare the accurancy results from the existing approach and our proposed approach.

# 1.4 Scopes
The scopes of the research are:

- Using the dataset of the drug target interaction from the DrugCentral database that is open publicly.

- Using Non-negative Matrix Factorization to reduce similarity matrix dimensions.

- Using the Visual Studio Code platform to code our python project.

# 1.5 Conclusion
To sum up everything, this proposal highlights the two-stage approach aimed at enhancing prediction of how drugs and proteins interact. Our primary goals are to increase the accuracy prediction and at the same time uncovering new interactions between drugs and proteins. By changing third step of DTINet from using the Singular Value Decomposition(SVD) into Non-negative Matrix Factorization(NMF) to reduce similarity matrix dimensions, we hope that we can increase its accuracy to more than 0.5 using roc_auc_score function.

Simultaneously, our research aims to explore and identify potential novel interactions between drugs and proteins. In the context of drug discovery and development, it's crucial to understand how different drugs can interact with specific proteins in the human body. These interactions often determine a drug's effectiveness, potential side effects, and overall safety. These discoveries could also open the doors to new treatment possibilities for medical conditions that were previously uncharted.

Last but not least, our proposal presents a strategy to enhance predictive capabilities and discover new therapeutic prospects. It is important to note that further research and testing are required to determine the effectiveness and practical applications of this approach.

# 2.1 Software & Hardware Requirements
2.1.1 Software
- DrugCentral. DrugCentral is an online drug information resource created and maintained by Division of Translational Informatics at University of New Mexico in collaboration with the IDG. DrugCentral provides information on active ingredients, chemical entities, pharmaceutical products, drug mode of action, indications, pharmacologic actions. “DrugCentral provides the drug information resource. We can download the known drug-target interaction from literature review, drug labels and external data sources. There are 2529 drugs, 2870 targets and 17390 drug-target interactions in the DrugCentral site as of 18 June 2021” (Byeungwon Kwon, 2021).

- GitHub. While GitHub is a code hosting platform for version control and collaboration. We use GitHub as a method to communicate with our client as well as a reference for the previous project, while they use SVD (Singular Value Decomposition) to predict drug-target interaction, we decided to tweak it and use NMF (Non-negative Matrix Factorization) instead. We also use GitHub as a medium for our project for others alike to see gain something from in the near future. In GitHub as well we can find Luo et al., which introduces a network integration approach for drug-target interaction prediction and develops DTINet.

- Nature Communications. Nature Portfolio is used to serve the research community by publishing its most significant discoveries—findings that advance knowledge and address some of the greatest challenges that we face as a society today. An article ‘A network integration approach for drug-target interaction prediction and computational drug repositioning from heterogeneous information’ is used as a reference for our project.

- Anaconda. Anaconda Python is a free, open-source platform that allows you to write and execute code in the programming language Python. It is by continuum.io, a company that specializes in Python development. Specifically PythonAnywhere by Anaconda is being used here for now as our Python programming language compiler and the heart of the project.

- Visual Studio Code (VSC). Visual Studio Code is a code editor redefined and optimized for building and debugging modern web and cloud applications. We initially used VSC for our Python programming.
	
	2.1.2 Hardware

- Personal laptop. We both use our own laptops as our current and only hardware for now. This will help us with Python programming, researching and communicating with our client as well as our lecturer for any external assistance and advice. They say two is better than one, therefore with both of us using our own individual laptops will absolutely make our project finish quickly and without any real challenges others may face.

# 2.3 References 
- Central, D. (2023). About. Drug Central. Retrieved October 19, 2023, from https://drugcentral.org/about

- Kwon, B. (2021, June 23). Drug-Target interaction prediction through Python | by Byeungchun Kwon | Geek Culture. Medium. Retrieved October 15, 2023, from https://medium.com/geekculture/drug-target-interaction-prediction-through-python-4af9e76fc90

- Luo, Y., Zhao, X., Zhou, J., Yang, J., Zhang, Y., & Kuang, W. (2017, September 18). A network integration approach for drug-target interaction prediction and computational drug repositioning from heterogeneous information. https://www.nature.com/articles/s41467-017-00680-8

- Pramoditha, R. (2023, August 24). Non-Negative Matrix Factorization (NMF) for Dimensionality Reduction in Image Data. Towards Data Science. Retrieved October 21, 2023, from https://towardsdatascience.com/non-negative-matrix-factorization-nmf-for-dimensionality-reduction-in-image-data-8450f4cae8fa

- sklearn.decomposition.NMF — scikit-learn 1.3.1 documentation. (n.d.). Scikit-learn. Retrieved October 16, 2023, from https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.NMF.html
