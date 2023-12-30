## Project Progress 4

### Flowchart
Project Progress 4 encompasses a comprehensive model development flowchart that includes the implementation of diverse algorithms such as simple and multiple linear regression, Support Vector Machine (SVM), Random Forest, Decision Tree, and ElasticNet. The flowchart seamlessly integrates evaluation metrics, including accuracy, precision, recall, and F1 score, to provide a holistic assessment of classification model performance. This structured approach ensures a thorough exploration of the models' capabilities, aiding in data-driven decision-making for Alzheimer's disease prediction based on clinical data.

![Image Alt Text](https://drive.google.com/uc?id=1xrxqz4pR1do9fywHUTolCqbMwI7ymdzT)

### Model Development Code
In our model development process, we've chosen regression analysis to understand the connection between two key factors: 'Group' and 'MMSE' (Mini-Mental State Examination). These are the features we're focusing on, with 'Group' as the independent factor and 'MMSE' as the dependent one. The goal is to see how changes in the 'Group' variable might influence 'MMSE' scores—a critical measure of cognitive function in Alzheimer's patients. Through regression models, we aim to quantify and visualize these relationships, gauging how well 'Group' predicts 'MMSE' outcomes.

![Image Alt Text](https://drive.google.com/uc?id=19wl0ffwxtesCFTwzWQZS54s8CWqaWjLA)

The code begins by defining the independent variable ('Group') as X and the dependent variable ('MMSE') as y. To assess the model's performance, the data is split into training and testing sets using the train_test_split function, with 80% designated for training and 20% for testing. The inclusion of random_state ensures reproducibility in the split, allowing for consistent results in subsequent executions of the code.
