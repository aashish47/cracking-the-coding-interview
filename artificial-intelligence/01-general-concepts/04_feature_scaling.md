# 04 Feature Scaling

## 1. Why Scale?

- Algorithms based on **distance** (KNN, K-Means, SVM) or **Gradient Descent** (Linear/Logistic Regression, Neural Networks) perform poorly if features have vastly different ranges.
- **Tree-based models** (Decision Trees, Random Forest) generally do **not** require scaling.

## 2. Techniques

| Method                        | Formula                                      | Range          | Use Case                                                                          |
| :---------------------------- | :------------------------------------------- | :------------- | :-------------------------------------------------------------------------------- |
| **Normalization (Min-Max)**   | $X' = \frac{X - X_{min}}{X_{max} - X_{min}}$ | [0, 1]         | When data doesn't follow a Gaussian distribution (e.g., Image pixel intensities). |
| **Standardization (Z-Score)** | $X' = \frac{X - \mu}{\sigma}$                | No fixed range | When data follows a Gaussian distribution; handles outliers better than Min-Max.  |
| **Robust Scaling**            | $X' = \frac{X - Q2}{IQR}$                    | No fixed range | When data contains **significant outliers** that would distort Mean/Std Dev.      |

## 3. Important: Avoiding Data Leakage

When scaling, always follow these steps to prevent information from the test set "leaking" into the training process:

1.  **Fit** the scaler only on the **Training Data** (calculate $\mu, \sigma, min, max$).
2.  **Transform** both the Training and Test data using those calculated values.
3.  **Never** fit the scaler on the entire dataset before splitting.
