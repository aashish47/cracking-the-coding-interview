# 07 Bias vs. Variance

## 1. Definitions

The goal of any model is to generalize well to new data. Failure to do so usually comes from one of two errors:

- **Bias:** Error due to overly simplistic assumptions (e.g., fitting a straight line to curved data).
- **Variance:** Error due to excessive sensitivity to small fluctuations in the training set (e.g., fitting the noise).

## 2. The Trade-off

| State            | Bias | Variance | Symptom                               | Solution                                          |
| :--------------- | :--- | :------- | :------------------------------------ | :------------------------------------------------ |
| **Underfitting** | High | Low      | High Training Error, High Test Error. | Increase model complexity, add features.          |
| **Overfitting**  | Low  | High     | Low Training Error, High Test Error.  | Get more data, Regularization, Feature selection. |
| **Optimal**      | Low  | Low      | Low Training Error, Low Test Error.   | -                                                 |
