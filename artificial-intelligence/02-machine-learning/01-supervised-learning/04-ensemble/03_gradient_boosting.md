# 03 Gradient Boosting

**Gradient Boosting** is a sequential ensemble technique where each new tree is built to correct the errors (residuals) of the previous trees. Unlike Random Forest, where trees are independent, Gradient Boosting trees are built one after another.

## 1. The Core Idea: Learning from Residuals

Instead of predicting the actual target $y$ directly, each subsequent tree predicts the **residual error** (the difference between the actual value and the current prediction) of the combined ensemble.

### The Process:

1. **Start with a Base Model:** Usually a simple constant value (like the mean of all $y$ values).
2. **Calculate Residuals:** Find the error ($y - \hat{y}$) for every data point.
3. **Train a Weak Learner:** Build a small tree (often called a "stump") to predict those residuals.
4. **Update Predictions:** Add the new tree's prediction to the previous total.
5. **Repeat:** Continue this process for $N$ iterations until the error is minimized.

## 2. The Math: Why "Gradient"?

The term "Gradient" comes from the fact that this algorithm is essentially performing **Gradient Descent** in the functional space.

- In Logistic Regression, we change weights ($w$) to minimize Loss.
- In Gradient Boosting, we add new trees ($f(x)$) to minimize Loss.

The residuals we are predicting are actually the **negative gradients** of the Loss Function.

## 3. Key Hyperparameters

- **Learning Rate ($\eta$):** A small value (e.g., 0.1) that scales the contribution of each new tree. This is crucial for preventing overfitting—it ensures the model doesn't "rush" toward a solution.
- **n_estimators:** The number of sequential trees. Because boosting learns from errors, adding too many trees **can** lead to overfitting (unlike Random Forest).
- **Subsample:** The fraction of samples used for fitting the individual base learners.

## 4. Comparison: Bagging vs. Boosting

| Feature               | Random Forest (Bagging)          | Gradient Boosting                    |
| --------------------- | -------------------------------- | ------------------------------------ |
| **Tree Construction** | Parallel (Independent).          | Sequential (Dependent).              |
| **Goal**              | Reduce Variance (Overfitting).   | Reduce Bias (Underfitting).          |
| **Risk**              | Hard to overfit by adding trees. | Overfits if trees are too many/deep. |
| **Error Handling**    | Averages out errors.             | Targets and fixes errors.            |
