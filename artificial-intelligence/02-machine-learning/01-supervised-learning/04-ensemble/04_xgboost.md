# 04 XGBoost (Extreme Gradient Boosting)

**XGBoost** is an optimized, high-performance implementation of Gradient Boosting. Since its release, it has become the "state-of-the-art" for structured or tabular data, largely due to its speed and predictive power.

## 1. Why is it "Extreme"?

XGBoost isn't just a different algorithm; it is a highly engineered system designed to be efficient, flexible, and portable. It improves upon standard Gradient Boosting in several key ways:

### A. Regularization

Standard GBM (Gradient Boosting Machine) has no built-in regularization. XGBoost includes **L1 (Lasso)** and **L2 (Ridge)** regularization in its cost function, which penalizes complex trees and significantly helps prevent overfitting.

### B. Handling Sparse Data

XGBoost has a "sparsity-aware" split-finding algorithm. If it encounters a missing value or a zero, it automatically learns the best default direction (left or right) to send that data point through the tree.

### C. Parallel Processing

While boosting is sequential, XGBoost parallelizes the **tree construction** process by sorting the data in "blocks" across CPU cores. This makes it orders of magnitude faster than traditional GBM.

## 2. Mathematical Optimization: Second-Order Derivatives

Most boosting algorithms use the first derivative (the gradient) to minimize the loss. XGBoost uses a **Taylor Expansion** to calculate both the first derivative (**gradient**) and the second derivative (**hessian**). This provides more information about the curvature of the loss function, allowing the model to reach the minimum faster and more accurately.

## 3. Key Hyperparameters

XGBoost has a vast array of parameters, often categorized as:

- **General Parameters:** Which booster to use (usually `gbtree`).
- **Booster Parameters:**
- `eta` (Learning Rate): Typical values: 0.01–0.3.
- `max_depth`: How deep each tree can grow.
- `gamma`: A "Lagrangian multiplier" used for pruning; a split is only made if it reduces the loss by at least $\gamma$.
- `lambda` (L2) and `alpha` (L1): Regularization terms.

- **Learning Task Parameters:** Defines the objective (e.g., `binary:logistic` for classification).

## 4. Summary Table: Random Forest vs. GBM vs. XGBoost

| Feature            | Random Forest        | Gradient Boosting     | XGBoost                   |
| ------------------ | -------------------- | --------------------- | ------------------------- |
| **Strategy**       | Bagging (Parallel)   | Boosting (Sequential) | Boosting (Optimized)      |
| **Main Goal**      | Low Variance         | Low Bias              | Low Bias + Regularization |
| **Regularization** | No                   | No                    | **Yes (L1 & L2)**         |
| **Missing Values** | Needs pre-processing | Needs pre-processing  | **Built-in Handling**     |
| **Speed**          | Fast                 | Slow                  | **Very Fast**             |
