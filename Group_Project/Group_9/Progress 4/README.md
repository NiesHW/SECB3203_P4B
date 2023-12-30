## Project Progress 4

### Flowchart
Project Progress 4 encompasses a comprehensive model development flowchart that includes the implementation of diverse algorithms such as simple and multiple linear regression, Support Vector Machine (SVM), Random Forest, Decision Tree, and ElasticNet. The flowchart seamlessly integrates evaluation metrics, including accuracy, precision, recall, and F1 score, to provide a holistic assessment of classification model performance. This structured approach ensures a thorough exploration of the models' capabilities, aiding in data-driven decision-making for Alzheimer's disease prediction based on clinical data.

![Image Alt Text](https://drive.google.com/uc?id=1xrxqz4pR1do9fywHUTolCqbMwI7ymdzT)

### Model Development Code
In our model development process, we've chosen regression analysis to understand the connection between two key factors: 'Group' and 'MMSE' (Mini-Mental State Examination). These are the features we're focusing on, with 'Group' as the independent factor and 'MMSE' as the dependent one. The goal is to see how changes in the 'Group' variable might influence 'MMSE' scores—a critical measure of cognitive function in Alzheimer's patients. Through regression models, we aim to quantify and visualize these relationships, gauging how well 'Group' predicts 'MMSE' outcomes.

![Image Alt Text](https://drive.google.com/uc?id=19wl0ffwxtesCFTwzWQZS54s8CWqaWjLA)

The code begins by defining the independent variable ('Group') as X and the dependent variable ('MMSE') as y. To assess the model's performance, the data is split into training and testing sets using the train_test_split function, with 80% designated for training and 20% for testing. The inclusion of random_state ensures reproducibility in the split, allowing for consistent results in subsequent executions of the code.

![Image Alt Text](https://drive.google.com/uc?id=1__RjtKOLv_rK1ySzI8Ip53TixTqDhHfU)

It then prints the shapes of both the training and testing sets, providing a visual confirmation of the successful split. This verification step is crucial for ensuring that the data has been partitioned correctly and aids in confirming the appropriateness of the training and testing subsets for subsequent model training and evaluation.

![Image Alt Text](https://drive.google.com/uc?id=1fCFt4UiAwmo9rqHIR74j3pYuD9kS3WNM)

The code establishes a polynomial regression model with a degree of 2 by employing a pipeline. Within this pipeline, the process involves the transformation of features into polynomial features, facilitating the capture of quadratic relationships, followed by the fitting of a linear regression model.

![Image Alt Text](https://drive.google.com/uc?id=1ZNuxJMFD6qAyUq3p7khIGDK9wLif5HeD)

The script applies the trained regression models to generate predictions on the testing set. Subsequently, it computes the R-squared (r2) and mean squared error (mse) metrics to assess the performance of both the linear and polynomial regression models. These metrics provide quantitative insights into how well the models generalize to unseen data, with R-squared indicating the proportion of variance explained and mean squared error measuring the average squared difference between predicted and actual values.

![Image Alt Text](https://drive.google.com/uc?id=1VZZk2jn8fANpXhG7dELzVvZCG0Z5US1z)

This code utilizes Matplotlib to create two scatter plot visualizations comparing actual and predicted values from two regression models—simple linear regression and polynomial regression. The first visualization showcases the alignment between actual 'MMSE' values and predicted values from the simple linear regression model, while the second visualization presents a similar comparison for the polynomial regression model with a specified degree. These visualizations aim to provide a visual understanding of how well both regression models predict 'MMSE' scores based on the 'Group' variable.

![Image Alt Text](https://drive.google.com/uc?id=1sj9EFc54gN3_IDGYYMS2POApRYFldZbK)

The results indicate that the linear regression model accounts for approximately 48.4% of the variance in MMSE scores on the testing set, with a mean squared error of 8.66. Similarly, the polynomial regression model of degree 2 achieves a comparable R-squared value of approximately 48.6%, with a slightly lower mean squared error of 8.62, suggesting modest improvements in capturing the non-linear relationships within the Alzheimer's patient dataset.
