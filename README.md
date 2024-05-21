# Student Race Predictor

## By: Leticia Genao
### Course: N.U. ANA680

## Problem Statement
This project aims to predict the race/ethnicity of students based on their academic performance in math, reading, and writing scores. Using a Random Forest Classifier, the project evaluates the ability of these scores to classify students into different race/ethnicity categories effectively. A key aspect of this project is practicing the deployment of machine learning models; thus, it includes deploying the application on Heroku to provide practical experience with real-world model deployment.

## Dataset Description
The dataset includes academic scores and race/ethnicity information for each student, focusing on their performance in three key areas:
- **Math Score**
- **Reading Score**
- **Writing Score**
- **Race/Ethnicity** (Target Variable)

- **Data Source:** [Kaggle)](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams/data)
- **Rows:** Approximately 1000 entries
- **Columns:** 4 (including the target variable 'Race/Ethnicity')

## Methodology

### Data Preprocessing
The categorical target variable 'race/ethnicity' was encoded into numeric labels to facilitate the model's training process. The primary features considered for modeling were the students' scores in math, reading, and writing.

### Model Building
The project utilizes the Random Forest Classifier from Scikit-learn, known for its robustness and effectiveness in handling classification tasks over various types of data distributions:
- **Random Forest Classifier** - Configured to handle imbalanced data using techniques like SMOTE for oversampling the minority classes during training.

### Model Evaluation
The model's performance was assessed using accuracy and a confusion matrix. These metrics helped in understanding the model's effectiveness in predicting the correct race/ethnicity categories.

## Results
The Random Forest model achieved an accuracy of 22%, where the detailed breakdown of performance across different classes is represented in the confusion matrix in the code. This matrix helps illustrate the model's precision and recall for each race/ethnicity category.


## Deployment
The application is deployed on Heroku, allowing users to interact with the model in real-time. This deployment serves as a practical demonstration of how machine learning models can be integrated into web applications and accessed via standard web interfaces.
- **Live Application:** [Visit Heroku App](https://scorebasedethnicitymodel-6b21cd93b475.herokuapp.com/)

## Discussion
The use of the Random Forest Classifier highlights its capability to manage the complexities of multi-class classification in an imbalanced dataset. The performance metrics suggest that while the model performs indequately, there may be room for further optimization or consideration of additional features that could enhance predictive accuracy.

## Conclusion
The project demonstrates the application of a Random Forest Classifier to predict student race/ethnicity based on academic scores. The findings underscore the potential of machine learning in educational data analysis, providing a basis for future explorations into more sophisticated models or feature engineering techniques.
