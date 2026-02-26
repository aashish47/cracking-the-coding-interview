# 08 Regularization

## 1. Goal

To prevent **Overfitting** (High Variance) by adding a penalty term to the **Cost Function**. This discourages the model from relying too heavily on any single feature by keeping the weights ($w$) small.

## 2. Techniques

| Feature               | L1 Regularization (Lasso)                         | L2 Regularization (Ridge)                   |
| :-------------------- | :------------------------------------------------ | :------------------------------------------ |
| **Penalty Term**      | Adds absolute value: $\lambda \sum \|w\|$         | Adds squared value: $\lambda \sum w^2$      |
| **Effect on Weights** | Can shrink weights to exactly **zero**.           | Shrinks weights towards zero (not exactly). |
| **Primary Use**       | **Feature Selection** (removes useless features). | Handling **Multicollinearity**.             |
| **Model Complexity**  | Produces "Sparse" models.                         | Produces "Dense" models.                    |

## 3. Elastic Net

A hybrid approach that combines both L1 and L2 penalties. It is useful when there are multiple correlated features.

## 4. The Lambda ($\lambda$) Hyperparameter

The strength of the regularization is controlled by the hyperparameter $\lambda$ (sometimes called `alpha` in libraries like Scikit-Learn).

| Value of $\lambda$  | Effect on Model                        | Result                           |
| :------------------ | :------------------------------------- | :------------------------------- |
| **$\lambda = 0$**   | No regularization.                     | Standard OLS.                    |
| **Small $\lambda$** | Weak penalty on weights.               | **Overfitting** (High Variance). |
| **Large $\lambda$** | Strong penalty; weights approach zero. | **Underfitting** (High Bias).    |

> **Note:** Ordinary Least Squares (OLS) is the standard linear regression method that minimizes the sum of squared errors without any penalty term.

> **Note:** Always perform **Feature Scaling** before applying regularization, as the penalty is applied to the magnitude of the weights.

## 5. Dropout

| Feature     | Description                                                                                                |
| :---------- | :--------------------------------------------------------------------------------------------------------- |
| **Concept** | A Deep Learning technique where a random percentage of neurons are "turned off" during each training step. |
| **Logic**   | Prevents neurons from co-dependency; they must learn robust, independent features.                         |
| **Analogy** | A sports team practicing with random players missing; the rest must become more versatile.                 |

## 6. Early Stopping

| Feature     | Description                                                                                           |
| :---------- | :---------------------------------------------------------------------------------------------------- |
| **Concept** | Halting training as soon as performance on the **Validation Set** starts to degrade.                  |
| **Logic**   | Prevents the model from learning noise (overfitting) by stopping at the point of best generalization. |
| **Trigger** | Monitor validation loss; stop if it doesn't improve for a set number of iterations (**patience**).    |
