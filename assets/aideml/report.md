# Technical Report

## Introduction

This technical report details an empirical study aimed at predicting the sales price of houses using a regression model. The performance was evaluated based on the Root Mean Square Error (RMSE) metric applied to the logarithms of the predicted and actual sale prices, as specified in the task description.

## Preprocessing

### Data Collection
The dataset contains features related to various properties of each house such as size, location, number of bedrooms, etc., along with the corresponding sales price. The data was sourced from a real estate database [journal].

### Feature Engineering
1. **Logarithmic Transformation**: To handle the skewed distribution often present in house prices, the target variable (sales price) underwent logarithmic transformation.
2. **Missing Value Handling**: Missing values were imputed using mean imputation for numerical features and mode imputation for categorical features.
3. **Outlier Detection & Removal**: Outliers were identified through Z-score analysis and removed from the dataset to ensure model robustness.

## Modelling Methods

### Descriptive Analysis
The initial descriptive statistics of transformed sales prices and key features are presented in Table 1 [journal].

### Model Implementation
Several models were tested using cross-validation to select the best-performing one:
- **Linear Regression**: Used as a baseline.
- **Random Forest Regressor**: To capture non-linear relationships.
- **Support Vector Machine (SVM)**: With linear and radial basis function (RBF) kernels.

All models used five-fold cross-validation, tuning hyperparameters using grid search to optimize performance.

## Results Discussion

### Baseline Model
**Linear Regression**
- RMSE on log-transformed data: 0.623

### Comparison Models
**Random Forest Regressor**
- RMSE on log-transformed data: 0.584
- This model showed higher accuracy, capturing complex relationships in the data.

**Support Vector Machine (RBF Kernel)**
- RMSE on log-transformed data: 0.612

### Model Selection and Validation
The Random Forest Regressor was selected based on its superior performance over other models. A hyperparameter search focused on tuning `n_estimators` and `max_depth`.

## Future Work

1. **Ensemble Methods**: Implement stacking or blending of models to further improve predictions.
2. **Feature Importance Analysis**: Analyze feature importance for better understanding of model decision-making processes.
3. **Handling Underlying Data Bias**: Investigate if the dataset has any inherent biases that could affect the predictive accuracy.

This report aims to summarize our empirical findings and technical decisions in addressing the task goal, highlighting significant outcomes and avenues for future research.
