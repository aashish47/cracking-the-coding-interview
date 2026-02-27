# 01 Introduction to Ensemble Learning

**Ensemble Learning** is a machine learning paradigm where multiple models (often called "weak learners") are trained to solve the same problem and combined to get better results. The main hypothesis is that a collection of models will perform better, on average, than any individual model.

## 1. The Core Philosophy

The "Wisdom of the Crowd" applies here. While a single decision tree might be prone to noise or specific errors, an ensemble of trees can cancel out each other's mistakes.

## 2. Why Ensembles? (The Bias-Variance Trade-off)

Ensembles are primarily designed to address two main issues in machine learning:

- **High Variance (Overfitting):** Models that are too complex and sensitive to training data.
- **High Bias (Underfitting):** Models that are too simple to capture the underlying patterns.

## 3. The Three Main Ensemble Techniques

### A. Bagging (Bootstrap Aggregating)

- **Goal:** Reduce **Variance**.
- **How:** Train multiple versions of the same model independently on different "bootstrap" samples (random subsets with replacement) of the data.
- **Final Result:** Averages the results (for regression) or takes a majority vote (for classification).
- **Example:** Random Forest.

### B. Boosting

- **Goal:** Reduce **Bias**.
- **How:** Train models **sequentially**. Each new model attempts to correct the errors made by the previous models.
- **Final Result:** A weighted sum of all the models.
- **Example:** AdaBoost, Gradient Boosting, XGBoost.

### C. Stacking

- **Goal:** Improve overall predictive power.
- **How:** Train different types of models (e.g., a KNN, a SVM, and a Tree) and then use a "meta-model" to decide how to best combine their outputs.

## 4. Key Terminology

- **Weak Learner:** A model that performs only slightly better than random guessing (e.g., a shallow decision tree).
- **Strong Learner:** The final ensemble model that achieves high accuracy.
- **Bootstrap:** The process of random sampling with replacement.
