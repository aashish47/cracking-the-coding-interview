# 09 Hyperparameter Tuning

## 1. Parameters vs. Hyperparameters

| Feature      | Parameters                            | Hyperparameters                                   |
| :----------- | :------------------------------------ | :------------------------------------------------ |
| **Source**   | Learned by the model during training. | Set by the human _before_ training.               |
| **Examples** | Weights ($w$), Biases ($b$).          | Learning Rate ($\alpha$), $K$ in KNN, Tree Depth. |
| **Goal**     | Minimize the Cost Function.           | Optimize the learning process/architecture.       |

## 2. Tuning Methods

| Method                    | Description                                                    | Pros                                          | Cons                                       |
| :------------------------ | :------------------------------------------------------------- | :-------------------------------------------- | :----------------------------------------- |
| **Grid Search**           | Brute-force checking every combination of a preset list.       | Guaranteed to find the best within the grid.  | Extremely slow; computationally expensive. |
| **Random Search**         | Randomly samples combinations from a distribution.             | Faster; often finds a "good enough" solution. | May miss the absolute optimal point.       |
| **Bayesian Optimization** | Uses probability to choose the next set based on past results. | Very efficient; focuses on promising areas.   | More complex to implement.                 |

## 3. The Tuning Workflow

1.  **Define the Space:** Choose which hyperparameters to tune and their ranges.
2.  **Select Search Strategy:** Pick Grid, Random, or Bayesian.
3.  **Cross-Validation:** Evaluate each combination using K-Fold to ensure results are robust.
4.  **Evaluate:** Compare performance on the **Validation Set**.

> **Note:** Hyperparameter tuning is often the final step in the ML workflow to squeeze out the last bit of performance after feature engineering is complete.

## 4. Common Hyperparameters by Model

- **Linear/Logistic Regression:** $\lambda$ (Regularization strength).
- **Decision Trees:** `max_depth`, `min_samples_split`.
- **Neural Networks:** `learning_rate`, `batch_size`, `epochs`, `dropout_rate`.
