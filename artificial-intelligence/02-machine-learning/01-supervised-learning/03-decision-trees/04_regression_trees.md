# 04 Regression Trees

Decision trees can also predict continuous numerical values (e.g., predicting a house price or a person’s age). This version is called a **Regression Tree**.

## 1. How it Works: Regional Means

Instead of assigning a "Class" to a leaf node, a regression tree assigns a **numeric value**. This value is typically the **mean (average)** of all the training observations that fall into that specific leaf.

- **Splitting:** The tree divides the feature space into distinct, non-overlapping regions ($R_1, R_2, ... R_n$).
- **Prediction:** For any new input falling into region $R_j$, the model predicts the average of the training targets in $R_j$.

## 2. Splitting Criterion: Sum of Squared Errors (SSE)

In classification, we use Entropy or Gini. In regression, we aim to minimize the variance within each leaf. The most common metric is the **Sum of Squared Errors (SSE)** or **Mean Squared Error (MSE)**.

For a potential split, the tree calculates:

$$SSE = \sum_{i \in \text{Left}} (y^{(i)} - \bar{y}_{\text{Left}})^2 + \sum_{i \in \text{Right}} (y^{(i)} - \bar{y}_{\text{Right}})^2$$

- **$\bar{y}_{\text{Left/Right}}$:** The mean of the target values in the resulting child nodes.
- The algorithm chooses the split point that results in the **lowest SSE** across the two new regions.

## 3. Visualizing the Prediction

Unlike Linear Regression, which produces a smooth, continuous line, a Regression Tree produces a **step function**.

- If the tree is shallow, the "steps" are large and few.
- If the tree is deep, the steps become smaller and more numerous, eventually potentially overfitting the noise in the data.

## 4. Comparison: Classification vs. Regression Trees

| Feature             | Classification Tree         | Regression Tree                  |
| ------------------- | --------------------------- | -------------------------------- |
| **Output**          | Categorical (Class Label).  | Continuous (Numeric Value).      |
| **Criteria**        | Entropy or Gini Impurity.   | Sum of Squared Errors (SSE/MSE). |
| **Leaf Prediction** | Mode (Most frequent class). | Mean (Average of values).        |
